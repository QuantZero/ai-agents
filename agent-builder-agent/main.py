"""Main entry point for Agent Builder agent."""

import os
import sys
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import schedule
import time

from graph import build_graph
from tools import get_existing_agents

load_dotenv(override=True)


def run_daily_agent_build():
    """Execute the daily agent building workflow."""
    print(f"\n{'='*60}")
    print(f"Agent Foundry - Daily Build")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")
    
    # Get repository root
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Get existing agents to avoid duplicates
    existing_agents = get_existing_agents(repo_root)
    print(f"Found {len(existing_agents)} existing agents")
    
    # Count agents to determine number
    agents_dir = Path(repo_root) / "agents"
    if agents_dir.exists():
        agent_count = len([d for d in agents_dir.iterdir() if d.is_dir()])
    else:
        agent_count = 0
    
    # Initialize state
    initial_state = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "existing_agents": existing_agents,
        "idea": None,
        "implementation": None,
        "agent_dir": None,
        "registry_readme_path": "README.md",
        "idea_generated": False,
        "implementation_created": False,
        "files_written": False,
        "registry_updated": False,
        "git_committed": False,
        "email_sent": False,
        "errors": [],
        "agent_count": agent_count,
        "registry_content": "",
    }
    
    # Build and run graph
    graph = build_graph()
    
    try:
        print("Starting workflow...")
        final_state = graph.invoke(initial_state)
        
        # Print summary
        print(f"\n{'='*60}")
        print("Workflow Summary")
        print(f"{'='*60}")
        print(f"Idea Generated: {final_state.get('idea_generated', False)}")
        print(f"Implementation Created: {final_state.get('implementation_created', False)}")
        print(f"Files Written: {final_state.get('files_written', False)}")
        print(f"Registry Updated: {final_state.get('registry_updated', False)}")
        print(f"Git Committed: {final_state.get('git_committed', False)}")
        print(f"Email Sent: {final_state.get('email_sent', False)}")
        
        if final_state.get("idea"):
            idea_name = final_state["idea"].get("name", "Unknown")
            print(f"\nAgent Built: {idea_name}")
            if final_state.get("agent_dir"):
                print(f"Location: {final_state['agent_dir']}")
        
        if final_state.get("errors"):
            print(f"\nErrors:")
            for error in final_state["errors"]:
                print(f"  - {error}")
        
        print(f"{'='*60}\n")
        
        # Check if run was successful
        if (final_state.get("idea_generated") and 
            final_state.get("implementation_created") and 
            final_state.get("files_written") and 
            final_state.get("registry_updated")):
            print("✅ Daily agent build completed successfully!")
            return 0
        else:
            print("❌ Daily agent build completed with errors")
            return 1
    
    except Exception as e:
        print(f"\n❌ Fatal error: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1


def main():
    """Main entry point."""
    # Check for required environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please set OPENAI_API_KEY in your .env file or environment.")
        sys.exit(1)
    
    # Check if running in scheduled mode or one-time mode
    if len(sys.argv) > 1 and sys.argv[1] == "--schedule":
        # Scheduled mode - run at the same time every day
        run_time = os.getenv("DAILY_RUN_TIME", "09:00")
        print(f"Agent Builder scheduled to run daily at {run_time}")
        print("Press Ctrl+C to stop")
        
        schedule.every().day.at(run_time).do(run_daily_agent_build)
        
        # Run once immediately if it's past the scheduled time
        current_time = datetime.now().strftime("%H:%M")
        if current_time >= run_time:
            run_daily_agent_build()
        
        # Keep running
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    else:
        # One-time execution
        exit_code = run_daily_agent_build()
        sys.exit(exit_code)


if __name__ == "__main__":
    main()

