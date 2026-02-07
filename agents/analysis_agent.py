from google.adk.agents import LlmAgent
from tools.analysis_tools import extract_table_of_contents, convert_pdf_to_md
from config import ANALYSIS_MODEL
from pydantic import BaseModel, Field

class TableOfContentsSection(BaseModel):
    title: str = Field(description="The chapter or section title")
    start_page: int = Field(description="The page number where the section starts")

class CourseMidtermInfo(BaseModel):
    course_code: str = Field(description="The academic course code, e.g., 'MATH 101'")
    midterm_date: str = Field(description="Extracted date of the exam")
    midterm_coverage: str = Field(description="The chapters or topics covered on the exam")
    relevant_sections: list[TableOfContentsSection] = Field(description="List of sections from the textbook that match the midterm coverage")

class Midterms(BaseModel):
    courses: list[CourseMidtermInfo]

analysis_agent = LlmAgent(
    name="analysis_agent",
    description="Analyzes documents and filters midterm information.",    
    model=ANALYSIS_MODEL,
    instruction="""
        Goal: Produce a structured summary of midterm exam requirements by extracting data from midterm overviews and textbooks.

        1. Read 'SavedArtifacts' from the previous agent and classify each Artifact as either a textbook or a midterm overview.
        2. Gather data using tools based on the Artifact type.
            a. If the Artifact is a textbook, call 'extract_table_of_contents' and if the 'status' is "success" then use the structured list, but if the 'status' is "fallback" analyze the markdown document preview for chapter/section titles and start pages.
            b. If the Artifact is a midterm overview, call 'convert_pdf_to_md' and extract the exam date and the list of covered chapters.
        3. Cross-reference the midterm coverage against the corresponding textbook table of contents and store only the chapters/sections that fall within the midterm coverage grouped by course code.
        4. Generate the final output matching the provided 'MidtermInfo' schema.
    """,
    tools=[extract_table_of_contents, convert_pdf_to_md],
    output_schema=Midterms,
    output_key="midterms"
)