from google.adk.agents import LlmAgent
from tools.artifacts import list_uploaded_pdfs
from tools.pdf import get_table_of_contents
from tools.pdf import analyze_midterm_overview

analysis_agent = LlmAgent(
    name="analysis_agent",
    description="Analyzes uploaded PDFs and extracts structure or exam coverage",
    model="gemini-3-flash",
    instruction="""
You have access to uploaded PDFs.

Steps:
1. Call list_uploaded_pdfs
2. For each PDF:
   a. Decide whether it is a textbook or a midterm overview or a syllabus
   b. If textbook → call get_table_of_contents
   c. If midterm overview → call analyze_midterm_overview
   d. If syllabus -> do nothing with it and move on to next PDF
3. Produce structured result with section/chapter names and start pages for only the chapters that are covered on the midterm in JSON format
""",
    tools=[
        list_uploaded_pdfs,
        get_table_of_contents,
        analyze_midterm_overview,
    ],
    output_key="analysis_results"
)