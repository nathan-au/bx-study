import pymupdf
import pymupdf.layout
import pymupdf4llm
from google.adk.tools import ToolContext


async def get_table_of_contents(tool_context: ToolContext, filename: str):
    pdf_artifact_part = await tool_context.load_artifact(filename=filename)
    pdf_bytes = pdf_artifact_part.inline_data.data
    pymupdf.TOOLS.mupdf_display_errors(False)
    try:
        with pymupdf.open(stream=pdf_bytes, filetype="pdf") as document:
            table_of_contents = document.get_toc(simple=True)
            if (table_of_contents):
                return table_of_contents
            else:
                md_text = pymupdf4llm.to_markdown(document, pages=list(range(0, 24)))
                return md_text
    except Exception as e:
        print("Error: " + str(e))

async def read_pdf_to_md(tool_context: ToolContext, filename: str):
    pdf_artifact_part = await tool_context.load_artifact(filename=filename)
    pdf_bytes = pdf_artifact_part.inline_data.data
    try:
        with pymupdf.open(stream=pdf_bytes, filetype="pdf") as document:
            md_text = pymupdf4llm.to_markdown(document)
            return md_text
    except Exception as e:
        print("Error: " + str(e))        
