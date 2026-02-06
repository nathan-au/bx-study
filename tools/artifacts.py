from google.adk.tools.tool_context import ToolContext
from google.genai import types

async def save_pdf_artifact(tool_context: ToolContext, file_path: str, filename: str = None):
    with open(file_path, "rb") as file:
        pdf_bytes = file.read()

    artifact_part = types.Part(inline_data=types.Blob(mime_type="application/pdf", data=pdf_bytes))
    await tool_context.save_artifact(filename, artifact_part)