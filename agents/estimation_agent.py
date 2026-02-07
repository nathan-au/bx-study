from google.adk.agents import LlmAgent
from config import ESTIMATION_MODEL
from pydantic import BaseModel, Field

class WorkloadSection(BaseModel):
    title: str = Field(description="The chapter or section title")
    time_estimate: int = Field(description="The estimated time to study/review the section in minutes")

class WorkloadCourse(BaseModel):
    sections: list[WorkloadSection]

class StudyWorkload(BaseModel):
    courses: list[WorkloadCourse]


estimation_agent = LlmAgent(
    name="estimation_agent",
    description="Estimates study time required based on textbook section lengths and difficulty.",
    model=ESTIMATION_MODEL,
    instruction="""
        Goal: Analyze textbook data to determine the study workload in minutes for each section.

        1. Read 'Midterms' from the previous agent and for each course, look at the textbook sections.
        2. For each textbook section, predict how many minutes it will take the user to study/review each section based on the number of pages between the section start page and the following section start page as well as the topic difficulty based on the section title.
        3. Generate the final output matching the provided 'StudyWorkload' schema.
    """,
    output_schema=StudyWorkload,
    output_key="workload"
)