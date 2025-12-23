import os
import streamlit as st
from pathlib import Path
from dotenv import load_dotenv
import zipfile
import io

# Import builder functions
from main import (
    build_prototype,
    load_builder_prompt,
    generate_tech_stack_and_architecture,
    generate_implementation_plan,
    AVAILABLE_MODELS,
    create_llm,
    get_model_pricing,
    format_pricing_info,
)

load_dotenv(override=True)

# Page configuration
st.set_page_config(
    page_title="MVP Builder Agent",
    page_icon="🔨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Dark theme CSS
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #0e1117;
    }
    .main {
        background-color: #0e1117;
    }
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #64b5f6;
        text-align: center;
        margin-bottom: 2rem;
    }
    .step-box {
        background-color: #1e3a5f;
        border-left: 4px solid #64b5f6;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
        color: #ffffff;
    }
    .success-box {
        background-color: #1e3a52;
        border-left: 4px solid #81c784;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
        color: #ffffff;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }
    .stMarkdown {
        color: #ffffff !important;
    }
    .stTextArea>div>div>textarea {
        color: #ffffff !important;
        background-color: #1e1e1e !important;
    }
    .stButton>button {
        background-color: #4caf50;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = "input"
    st.session_state.builder_prompt = ""
    st.session_state.architecture = None
    st.session_state.implementation_plan = None
    st.session_state.build_progress = []
    st.session_state.output_dir = "generated_prototype"
    st.session_state.build_complete = False
    st.session_state.provider = "openai"
    st.session_state.model = "gpt-4o"


def reset_session():
    """Reset the session"""
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.session_state.step = "input"
    st.session_state.builder_prompt = ""
    st.session_state.architecture = None
    st.session_state.implementation_plan = None
    st.session_state.build_progress = []
    st.session_state.output_dir = "generated_prototype"
    st.session_state.build_complete = False
    st.session_state.provider = "openai"
    st.session_state.model = "gpt-4o"


def create_zip(output_dir: str) -> bytes:
    """Create a zip file of the generated prototype"""
    zip_buffer = io.BytesIO()
    output_path = Path(output_dir)
    
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for file_path in output_path.rglob('*'):
            if file_path.is_file():
                arcname = file_path.relative_to(output_path)
                zip_file.write(file_path, arcname)
    
    zip_buffer.seek(0)
    return zip_buffer.read()


def main():
    # Header
    st.markdown('<div class="main-header">🔨 MVP Builder Agent</div>', unsafe_allow_html=True)
    st.markdown("---")

    # Sidebar
    with st.sidebar:
        st.header("Controls")
        if st.button("🔄 Start Over", use_container_width=True):
            reset_session()
            st.rerun()
        
        st.markdown("---")
        st.markdown("### Progress")
        steps_map = {
            "input": "1️⃣ Input Prompt",
            "architecture": "2️⃣ Architecture",
            "plan": "3️⃣ Implementation Plan",
            "building": "4️⃣ Building",
            "complete": "5️⃣ Complete"
        }
        current_step = st.session_state.step
        for step_key, step_label in steps_map.items():
            if step_key == current_step:
                st.markdown(f"🔄 {step_label}")
            elif list(steps_map.keys()).index(step_key) < list(steps_map.keys()).index(current_step):
                st.markdown(f"✅ {step_label}")
            else:
                st.markdown(f"⏳ {step_label}")
        
        st.markdown("---")
        with st.expander("💰 View Pricing Table"):
            st.markdown("### OpenAI Models")
            st.markdown("""
            | Model | Input | Output | Cached |
            |-------|-------|--------|--------|
            | GPT-5.2 Pro | $21.00 | $168.00 | N/A |
            | GPT-5.2 Thinking | $1.75 | $14.00 | $0.175 |
            | GPT-5.2 Instant | $0.25 | $2.00 | $0.025 |
            | **GPT-4o** ⭐ | **$2.50** | **$10.00** | **$0.25** |
            | GPT-4o-mini | $0.15 | $0.60 | $0.015 |
            | GPT-4-turbo | $10.00 | $30.00 | $1.00 |
            | GPT-4 | $30.00 | $60.00 | $3.00 |
            | GPT-3.5-turbo | $0.50 | $1.50 | $0.05 |
            """)
            
            st.markdown("### Anthropic Models")
            st.markdown("""
            | Model | Input | Output | Cached |
            |-------|-------|--------|--------|
            | Claude 4.5 Opus | $5.00 | $25.00 | $0.50 |
            | Claude 4.5 Sonnet | $3.00 | $15.00 | $0.30 |
            | Claude 4.5 Haiku | $1.00 | $5.00 | $0.10 |
            | **Claude 3.5 Sonnet** ⭐ | **$3.00** | **$15.00** | **$0.30** |
            | Claude 3 Opus | $15.00 | $75.00 | $1.50 |
            | Claude 3 Sonnet | $3.00 | $15.00 | $0.30 |
            | Claude 3 Haiku | $0.25 | $1.25 | $0.025 |
            """)
            
            st.markdown("### Ollama Models")
            st.markdown("**🆓 All models: Free (runs locally)**")
            
            st.caption("Prices are per million tokens. ⭐ = Recommended for coding.")

    # Main content
    if st.session_state.step == "input":
        st.markdown("### 📤 Provide Builder Prompt")
        st.markdown("Upload a builder prompt from MVP Planner Agent or paste it directly.")
        
        # File upload
        uploaded_file = st.file_uploader(
            "Upload builder prompt file",
            type=["txt", "md"],
            help="Upload the builder_prompt.txt from MVP Planner Agent"
        )
        
        if uploaded_file is not None:
            st.session_state.builder_prompt = uploaded_file.read().decode("utf-8")
            st.success("✅ Builder prompt loaded from file!")
        
        # Or paste directly
        st.markdown("---")
        st.markdown("### Or Paste Prompt Directly")
        prompt_input = st.text_area(
            "Builder Prompt:",
            value=st.session_state.builder_prompt,
            height=400,
            placeholder="Paste the builder prompt here..."
        )
        
        if prompt_input:
            st.session_state.builder_prompt = prompt_input
        
        # Model selection
        st.markdown("---")
        st.markdown("### 🤖 Model Selection")
        
        col_provider, col_model = st.columns(2)
        
        with col_provider:
            provider = st.selectbox(
                "Provider:",
                options=["openai", "anthropic", "ollama"],
                index=["openai", "anthropic", "ollama"].index(st.session_state.provider) if st.session_state.provider in ["openai", "anthropic", "ollama"] else 0,
                help="Choose the LLM provider"
            )
            st.session_state.provider = provider
        
        with col_model:
            available_models = AVAILABLE_MODELS.get(provider, [])
            current_model = st.session_state.model if st.session_state.model in available_models else available_models[0]
            model = st.selectbox(
                "Model:",
                options=available_models,
                index=available_models.index(current_model) if current_model in available_models else 0,
                help="Choose the specific model"
            )
            st.session_state.model = model
        
        # Show pricing info
        pricing_info = format_pricing_info(model)
        st.markdown(f"**💰 Pricing:** {pricing_info}")
        
        # Show model info
        if provider == "openai":
            st.info("💡 OpenAI models require OPENAI_API_KEY in .env")
        elif provider == "anthropic":
            st.info("💡 Anthropic models require ANTHROPIC_API_KEY in .env")
        elif provider == "ollama":
            st.info("💡 Ollama requires local installation. Make sure Ollama is running on localhost:11434")
        
        # Output directory
        st.markdown("---")
        output_dir = st.text_input(
            "Output Directory:",
            value=st.session_state.output_dir,
            help="Directory where the prototype will be generated"
        )
        st.session_state.output_dir = output_dir
        
        if st.button("🚀 Start Building", type="primary", use_container_width=True):
            if st.session_state.builder_prompt.strip():
                st.session_state.step = "architecture"
                st.rerun()
            else:
                st.error("Please provide a builder prompt first.")

    elif st.session_state.step == "architecture":
        st.markdown("### 📐 Step 1: Generating Architecture")
        st.info(f"🤖 Using: {st.session_state.provider.upper()} - {st.session_state.model}")
        
        with st.spinner("Analyzing builder prompt and generating tech stack..."):
            try:
                llm_instance = create_llm(st.session_state.provider, st.session_state.model)
                st.session_state.architecture = generate_tech_stack_and_architecture(
                    st.session_state.builder_prompt,
                    llm_instance
                )
                st.session_state.step = "plan"
                st.rerun()
            except Exception as e:
                st.error(f"Error generating architecture: {e}")
                if st.button("← Back to Input"):
                    st.session_state.step = "input"
                    st.rerun()

    elif st.session_state.step == "plan":
        # Show architecture
        if st.session_state.architecture:
            st.markdown("### ✅ Architecture Generated")
            with st.expander("View Architecture", expanded=True):
                st.json(st.session_state.architecture)
        
        st.markdown("### 📋 Step 2: Generating Implementation Plan")
        
        with st.spinner("Creating detailed implementation plan..."):
            try:
                llm_instance = create_llm(st.session_state.provider, st.session_state.model)
                phases = generate_implementation_plan(
                    st.session_state.builder_prompt,
                    st.session_state.architecture,
                    llm_instance
                )
                st.session_state.implementation_plan = {"phases": phases}
                st.session_state.step = "building"
                st.rerun()
            except Exception as e:
                st.error(f"Error generating implementation plan: {e}")
                if st.button("← Back"):
                    st.session_state.step = "architecture"
                    st.rerun()

    elif st.session_state.step == "building":
        # Show architecture and plan
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📐 Architecture")
            if st.session_state.architecture:
                st.json(st.session_state.architecture)
        
        with col2:
            st.markdown("### 📋 Implementation Plan")
            if st.session_state.implementation_plan:
                st.json(st.session_state.implementation_plan)
        
        st.markdown("---")
        st.markdown("### 🔨 Step 3: Building Prototype")
        st.info("This may take several minutes. The agent is generating code files step by step...")
        
        if st.button("🚀 Start Building Files", type="primary", use_container_width=True):
            try:
                output_path = build_prototype(
                    st.session_state.builder_prompt,
                    st.session_state.output_dir,
                    provider=st.session_state.provider,
                    model=st.session_state.model,
                )
                st.session_state.build_complete = True
                st.session_state.output_path = str(output_path)
                st.session_state.step = "complete"
                st.rerun()
            except Exception as e:
                st.error(f"Error building prototype: {e}")
                st.exception(e)

    elif st.session_state.step == "complete":
        st.markdown("### 🎉 Build Complete!")
        
        if st.session_state.build_complete and hasattr(st.session_state, 'output_path'):
            output_path = Path(st.session_state.output_path)
            
            st.success(f"✅ Prototype generated at: `{output_path.absolute()}`")
            
            # Show file tree
            st.markdown("### 📁 Generated Files")
            files = list(output_path.rglob('*'))
            file_count = len([f for f in files if f.is_file()])
            st.info(f"Total files created: {file_count}")
            
            with st.expander("View File Tree"):
                for file_path in sorted(files):
                    if file_path.is_file():
                        rel_path = file_path.relative_to(output_path)
                        st.code(str(rel_path), language=None)
            
            # Download as zip
            st.markdown("---")
            st.markdown("### 📥 Download Prototype")
            try:
                zip_data = create_zip(str(output_path))
                st.download_button(
                    label="📦 Download as ZIP",
                    data=zip_data,
                    file_name=f"{output_path.name}.zip",
                    mime="application/zip",
                    type="primary",
                    use_container_width=True
                )
            except Exception as e:
                st.warning(f"Could not create zip: {e}")
            
            # Show README if exists
            readme_path = output_path / "README.md"
            if readme_path.exists():
                st.markdown("---")
                st.markdown("### 📝 Generated README")
                with st.expander("View README", expanded=False):
                    st.markdown(readme_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    # Check for API key
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        st.error("⚠️ OPENAI_API_KEY is not set. Please add it to a .env file in the mvp-builder-agent directory.")
        st.stop()
    
    main()

