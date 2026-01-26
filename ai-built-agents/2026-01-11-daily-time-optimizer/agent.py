import os
import logging
from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
from schemas import ScheduleInput, OptimizedScheduleOutput
from graph import optimize_schedule

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

# Initialize APScheduler
scheduler = BackgroundScheduler()
scheduler.start()

@app.post("/optimize")
def optimize_daily_schedule(schedule_input: ScheduleInput):
    """
    Endpoint to optimize daily schedule.
    """
    try:
        optimized_schedule = optimize_schedule(schedule_input)
        return OptimizedScheduleOutput(schedule=optimized_schedule)
    except Exception as e:
        logger.error(f"Error optimizing schedule: {str(e)}")
        return {"error": "Failed to optimize schedule. Please try again later."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
