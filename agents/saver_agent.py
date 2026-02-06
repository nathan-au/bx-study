from google.adk.agents import LlmAgent
from tools.artifacts import save_pdf_artifact

saver_agent = LlmAgent(
    name="saver_agent",
    description="Saves PDFs as Artifacts",
    model="gemini-2.5-flash",
    instruction="The user will send one or more PDF file paths. Call save_pdf_artifact to save the file as an artifact for each file path. Keep the filenames as the original while saving",
    tools=[save_pdf_artifact]
)