from google.adk.agents import LlmAgent
from config import PLANNING_MODEL
from pydantic import BaseModel, Field
from tools.planning_tools import get_current_datetime

class StudyTask(BaseModel):
    date: str = Field(description="Task due date in YYYY-MM-DD format")
    course_code: str = Field(description="The academic course code, e.g., 'MATH 101'")
    section: str = Field(description="The chapter or section title")
    hours: float = Field(description="Estimated study hours")

class StudyPlan(BaseModel):
    schedule: list[StudyTask]

planning_agent = LlmAgent(
    name="planning_agent",
    description="Creates a study plan based on midterm info and workload estimates.",
    model=PLANNING_MODEL,
    instruction="""
        Goal: Create a structured study plan for the upcoming midterm exams based on the study workload.

        1. Read 'Midterms' and 'StudyWorkload' from the previous agents.
        2. Get the current date and time using 'get_current_datetime'.
        3. Equally distribute the sections across the days between today and the midterm exam date.
        4. Generate the final output in comma-separated value format with the first column 'Date', the second column 'Course', the third column 'Section', and the final column 'Workload' (as in the estimated time to study/review the section in minutes) where each row is separated by a new line character.
    """,
    tools=[get_current_datetime],
    # output_schema=StudyPlan,
    output_key="plan"
    
)