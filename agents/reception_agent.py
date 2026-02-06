from google.adk.agents import LlmAgent
from tools.artifacts import save_pdf_artifact

reception_agent = LlmAgent(
    name="reception_agent",
    description="Saves PDFs as Artifacts",
    model="gemini-2.5-flash",
    instruction="The user will send one or more PDF file paths. Call save_pdf_artifact to save the file as an artifact for each file path. When saving, append the common course code of the current batch to the beginning of each file name. Once all saving is complete, tell the user how many PDFs were saved for each course.",
    tools=[save_pdf_artifact]
)
