from google.adk.tools import ToolContext
from google.genai import types

async def save_pdf_artifact(tool_context: ToolContext, file_path: str, artifact_name: str) -> dict:

    """
        Saves a local PDF file to session Artifact storage.

        Args: 
            tool_context: The ADK context used to interact with Artifact storage.
            file_path: The local filesystem path to the PDF.
            artifact_name: The unique filename to use when saving file as Artifact.
        
        Returns:
            A dictionary with 'status' ("success" or "error") and a 'details' (the Artifact name (if success) or an error message (if error))
    """

    try:
        with open(file_path, "rb") as file:
            pdf_bytes = file.read()

        pdf_artifact = types.Part(
            inline_data=types.Blob(
                data=pdf_bytes, 
                mime_type="application/pdf"
            )
        )

        await tool_context.save_artifact(artifact_name, pdf_artifact)
        return {
            "status": "success",
            "details": artifact_name
        }

    except Exception as e:
        return {
            "status": "error",
            "details": str(e)
        } 
