from google.adk.agents import LlmAgent
from config import MODEL
from pydantic import BaseModel, Field
from tools.time import get_current_datetime

class StudyTask(BaseModel):
    date: str = Field(description="Task due date in YYYY-MM-DD format")
    course_code: str = Field(description="The academic course code, e.g., 'MATH 101'")
    section: str = Field(description="The chapter or section title")
    hours: float = Field(description="Estimated study hours")

class StudyPlan(BaseModel):
    schedule: list[StudyTask]

planning_agent = LlmAgent(
    name="planning_agent",
    description="Creates a study plan based on midterm and textbook content",
    model=MODEL,
    instruction="""

        Goal: Create a structured study plan for the upcoming midterm exams by analyzing textbook section lengths.

        1. Read 'Midterms' from the previous agent
        2. Predict how many hours it will take for the user to study/review each section based on the number of pages between the section start page and the following section start page.
        3. Get the current date and time using 'get_current_datetime'.
        4. Equally distribute the sections across the days between today and the midterm exam date.
        5. Generate the final output matching the provided 'StudyPlan' schema.
        6. Print the final output for the user.

    """,
    tools=[get_current_datetime],
    output_schema=StudyPlan,
    output_key="plan"
    
)