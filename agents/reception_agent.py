from google.adk.agents import LlmAgent
from tools.reception_tools import save_pdf_artifact
from config import RECEPTION_MODEL
from pydantic import BaseModel, Field

class SavedArtifact(BaseModel):
    course_code: str = Field(description="The academic course code, e.g., 'MATH 101'")
    artifact_name: str = Field(description="The unique name assigned to the saved Artifact")

class SavedArtifacts(BaseModel):
    total_artifacts: int = Field(description="The total number of successfully saved Artifacts")
    artifacts: list[SavedArtifact]

reception_agent = LlmAgent(
    name="reception_agent",
    description="Saves local PDFs as session Artifacts.",
    model=RECEPTION_MODEL,
    instruction="""
        Goal: Process the provided PDF file paths and store them as session Artifacts.

        1. Identify each unique PDF file path from the user.
        2. Determine the course code (e.g., 'MATH 101') from the filename or the folder name.
        3. Save each file exactly once using 'save_pdf_artifact'.
        4. Verify the tool output and only include files where 'status' is "success".
        5. Generate the final output matching the provided 'SavedArtifacts' schema.
    """,
    tools=[save_pdf_artifact],
    output_schema=SavedArtifacts,
    output_key="artifacts"
)
