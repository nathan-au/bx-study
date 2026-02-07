import pymupdf
import pymupdf.layout
import pymupdf4llm
from google.adk.tools import ToolContext

async def extract_table_of_contents(tool_context: ToolContext, artifact_name: str) -> dict:

    """
        Extracts the table of contents from a PDF file stored as an Artifact.

        Args: 
            tool_context: The ADK context used to interact with Artifact storage.
            artifact_name: The unique filename of the Artifact to load.
        
        Returns:
            A dictionary with 'status' ("success" (if table of contents found), "fallback" (if table of contents not found but Markdown preview provided), or "error") and 'details' (a list of table of contents entries (if success), a Markdown string (if fallback), or an error message (if error).

    """

    try:
        pymupdf.TOOLS.mupdf_display_errors(False)

        pdf_artifact = await tool_context.load_artifact(filename=artifact_name)
        pdf_bytes = pdf_artifact.inline_data.data

        with pymupdf.open(stream=pdf_bytes, filetype="pdf") as document:
            table_of_contents = document.get_toc(simple=True)

            if (table_of_contents):
                return {
                    "status": "success",
                    "details": table_of_contents,
                } 
            else:
                document_preview = pymupdf4llm.to_markdown(document, pages=list(range(0, 24)))
                return {
                    "status": "fallback",
                    "details": document_preview
                }
    
    except Exception as e:
        return {
            "status": "error",
            "details": str(e)
        } 

async def convert_pdf_to_md(tool_context: ToolContext, artifact_name: str) -> dict:

    """
        Converts a PDF file stored as an Artifact into Markdown text.

        Args: 
            tool_context: The ADK context used to interact with Artifact storage.
            artifact_name: The unique filename of the Artifact to load.
        
        Returns:
            A dictionary with 'status' ("success" or "error") and 'details' (a Markdown string (if success) or an error message (if error).
    """
    try:
        pdf_artifact = await tool_context.load_artifact(filename=artifact_name)
        pdf_bytes = pdf_artifact.inline_data.data

        with pymupdf.open(stream=pdf_bytes, filetype="pdf") as document:
            markdown_text = pymupdf4llm.to_markdown(document, pages=[0])
            return {
                "status": "success",
                "details": markdown_text
            }
        
    except Exception as e:
        return {
            "status": "error",
            "details": str(e)
        } 