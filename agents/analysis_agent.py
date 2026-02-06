from google.adk.agents import LlmAgent
from tools.pdf import get_table_of_contents, read_pdf_to_md

analysis_agent = LlmAgent(
    name="analysis_agent",
    description="Filters textbook TOC based on midterm coverage and merges data.",
    model="gemini-2.5-flash",
    instruction="""
        You are an academic analyzer. 
        
        GOAL:
        Extract midterm details and filter the textbook Table of Contents (TOC) to show ONLY the chapters and sub-sections relevant to the midterm.
        
        LOGIC:
        1. Identify the 'Midterm Overview' and 'Textbook' artifacts for each course.
        2. Get coverage from the Midterm Overview (e.g., 'Chapters 1-6').
        3. Use 'get_table_of_contents' to get the textbook TOC.
        4. FILTER the TOC: Include only the entries that fall within the midterm coverage.
        5. MERGE everything into one entry per course code.
        
        OUTPUT FORMAT EXAMPLE:
        {
          "PHYS 234": {
            "midterm_date": "February 26, 2026",
            "midterm_coverage": "Chapters 1-6",
            "filtered_toc": [
                {"level": 1, "title": "1 Stern-Gerlach Experiments", "page": 25},
                {"level": 2, "title": "1.1 Stern-Gerlach Experiment", "page": 25},
                ... (only chapters 1 through 6) ...
            ]
          }
        }
        
        Return ONLY valid JSON.
    """,
    tools=[get_table_of_contents, read_pdf_to_md],
)