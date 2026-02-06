from google.adk.tools import ToolContext
from google.genai import types

async def save_pdf_artifact(tool_context: ToolContext, file_path: str, filename: str):

    with open(file_path, "rb") as file:
        pdf_bytes = file.read()
    pdf_mime_type = "application/pdf"

    pdf_artifact_part = types.Part(
        inline_data=types.Blob(
            data=pdf_bytes, 
            mime_type=pdf_mime_type
        )
    )

    await tool_context.save_artifact(filename, pdf_artifact_part)



async def list_uploaded_pdfs(tool_context: ToolContext) -> list[str]:
    """
    Returns artifact filenames for uploaded PDFs in the current session/user scope.
    """

    artifact_names = await tool_context.list_artifacts()

    pdfs = [
        name for name in artifact_names
        if name.lower().endswith(".pdf")
    ]

    return pdfs