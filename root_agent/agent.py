from google.adk.agents import LlmAgent, SequentialAgent

# saver_agent = LlmAgent(
#     name="pdf_saver_agent",
#     model="gemini-2.5-flash",
#     description="Saves all uploaded PDFs as artifacts",
#     instruction="""
# Your task:
# 1. Call find_uploaded_pdfs.
# 2. If the list is empty, return an empty list.
# 3. Otherwise, call save_pdf_artifacts with the full list.
# 4. Return ONLY the list of artifact IDs.
# """,
#     tools=[find_uploaded_pdfs, save_pdf_artifacts],
#     output_key="pdf_artifact_ids",
# )

# summary_agent = LlmAgent(
#     name="summary_agent",
#     description="Summarizes a short uploaded PDF",
#     model="gemini-2.5-flash",
#     instruction="The user will upload a short PDF. The PDF text will appear in your input. Your task: Read the content, Produce a concise summary (50 words).",
#     # tools=[get_current_time],
# )

# root_agent = SequentialAgent(
#     name="pdf_summary_pipeline",
#     sub_agents=[
#         summary_agent,
#     ],
# )

# def find_uploaded_pdfs(context):



# def find_uploaded_pdfs(context) -> list[dict]:
#     """
#     Finds all uploaded PDFs in the agent input.
#     Returns a list of {filename, data}.
#     """
#     pdfs = []

#     for part in context.input_parts:
#         if part.mime_type == "application/pdf":
#             pdfs.append({
#                 "filename": part.inline_data.filename or "uploaded.pdf",
#                 "data": part.inline_data.data,
#             })

#     return pdfs

# from google.adk.artifacts import Artifact

# def save_pdf_artifacts(pdfs: list[dict], context) -> list[str]:
#     """
#     Saves multiple PDFs and returns their artifact IDs.
#     """
#     artifact_ids = []

#     for pdf in pdfs:
#         artifact = Artifact.from_bytes(
#             data=pdf["data"],
#             mime_type="application/pdf",
#             name=pdf["filename"],
#         )
#         artifact_id = context.artifact_service.save(artifact)
#         artifact_ids.append(artifact_id)

#     return artifact_ids



from google.adk.agents import LlmAgent
from google.adk.tools.tool_context import ToolContext
from google.genai import types
import os
from pathlib import Path

async def save_report_artifacts(tool_context: ToolContext, file_path: str, filename: str = None):
    
    # Check if file_path is a directory
    if os.path.isdir(file_path):
        # Read all PDF files from the directory
        pdf_files = list(Path(file_path).glob('*.pdf'))
        
        if not pdf_files:
            raise ValueError(f"No PDF files found in directory: {file_path}")
        
        # Process each PDF file
        for pdf_file in pdf_files:
            with open(pdf_file, 'rb') as f:
                pdf_bytes = f.read()
            
            # Save as a PDF artifact
            artifact_part = types.Part(
                inline_data=types.Blob(mime_type='application/pdf', data=pdf_bytes)
            )
            await tool_context.save_artifact(pdf_file.name, artifact_part)
    else:
        # Read the single file if directory doesn't exist
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File or directory not found: {file_path}")
        
        with open(file_path, 'rb') as f:
            pdf_bytes = f.read()

        # Save as a PDF artifact
        artifact_part = types.Part(
            inline_data=types.Blob(mime_type='application/pdf', data=pdf_bytes)
        )
        await tool_context.save_artifact(filename, artifact_part)
    


root_agent = LlmAgent(
    name = "first_agent",
    description = "This is my first agent",
    instruction= """
        You are an assistant that manages artifacts.
        If the user asks to save a document, 
        call 'save_report_artifacts' to save the files as an artifacts.
        You don't need to ask for the filename from the user and please keep the 
        filename as the original file while saving.
        """ ,
    model="gemini-2.5-flash",
    tools = [save_report_artifacts]
    
)