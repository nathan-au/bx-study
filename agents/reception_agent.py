from google.adk.agents import LlmAgent
from tools.artifacts import save_pdf_artifact

reception_agent = LlmAgent(
    name="reception_agent",
    description="Saves PDFs as Artifacts",
    model="gemini-2.5-flash",
    instruction="""

        1. Receive PDF file paths from the user.
        2. Extract the course code (e.g., MATH 205) from the context or file path.
        3. Call 'save_pdf_artifact' for each file and prefix the filename with the course code if it's not already there.
        4. Once complete, output a FINAL_MANIFEST in the following format:
            {
                "total_files": count,
                "files": [{"course": "code", "artifact_name": "name"}]
            }
        """,
    tools=[save_pdf_artifact]
)
