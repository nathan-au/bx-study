# bx-study: Agentic AI Study Planner
<img width="1624" height="1094" alt="Screenshot 2026-02-08 at 10 32 20" src="https://github.com/user-attachments/assets/b21a169e-adc7-4d28-8e99-00ce20147f2b" />

## Project Overview

b(x) Study is an automated, multi-agent pipeline that transforms course materials into structured study schedules. By orchestrating specialized LLM agents, this system parses textbooks, cross-references midterm coverage, estimates workload, and generates a day-by-day study plan.

## Key Features

- **Automated PDF Processing**: Extracts and analyzes textbooks and midterm overview documents.
- **Table of Contents Extraction**: Intelligently parses textbook structure using PyMuPDF.
- **Workload Estimation**: Calculates study time requirements based on section length and difficulty.
- **Smart Scheduling**: Distributes study tasks evenly across available days before exams.
- **Multi-Course Support**: Handles multiple courses and exams simultaneously.


## Architecture

The system uses a sequential architecture where each agent processes data and passes structured outputs to the next agent in the pipeline. Here's the complete workflow:

### 1. Reception Agent
The Reception Agent acts as the gateway for the system. It handles the initial file I/O and organizes the session workspace.

**Process**:
1. Identifies unique PDF file paths from user input.
2. Extracts course codes (e.g., 'MATH 101') from filenames or folder names.
3. Saves each PDF file exactly once using the `save_pdf_artifact` tool.
4. Verifies successful storage and tracks each artifact by name.

**Output**: `SavedArtifacts` schema containing:
- Total number of successfully saved artifacts.
- List of artifacts with course codes and unique artifact names.

### 2. Analysis Agent
The Analysis Agent is the "brain" that connects course materials to exam requirements.

**Process**:
1. Reads `SavedArtifacts` from the Reception Agent.
2. Classifies each artifact as either a textbook or midterm overview.
3. **For textbooks**:
   - Calls `extract_table_of_contents` to get structured chapter/section data.
   - If table of contents extraction succeeds, uses the structured list.
   - If extraction fails (status: "fallback"), analyzes the first 24 pages as Markdown to manually identify chapters and page numbers.
4. **For midterm overviews**:
   - Calls `convert_pdf_to_md` to convert the PDF to Markdown.
   - Extracts the exam date and list of covered chapters/topics.
5. Cross-references midterm coverage against textbook table of contents.
6. Filters and stores only relevant sections that match the exam coverage, grouped by course code.

**Output**: `Midterms` schema containing for each course:
- Course code.
- Midterm exam date.
- Coverage description.
- List of relevant textbook sections (title and start page).

### 3. Estimation Agent
The Estimation Agent quantifies the effort required for the identified study material.

**Process**:
1. Reads `Midterms` output from the Analysis Agent.
2. For each course, examines all relevant textbook sections.
3. Calculates page count by finding the difference between consecutive section start pages.
4. Estimates study time in minutes based on:
   - **Page count**: More pages = more time.
   - **Topic difficulty**: Inferred from section titles (e.g., "Advanced Calculus" vs "Introduction").
5. Generates time estimates for each individual section.

**Output**: `StudyWorkload` schema containing:
- For each course: list of sections with titles and time estimates (in minutes).

### 4. Planning Agent
The Planning Agent synthesizes all previous data into a final, executable study schedule.

**Process**:
1. Reads `Midterms` and `StudyWorkload` from previous agents.
2. Calls `get_current_datetime` to determine today's date.
3. Calculates the number of days available between today and each midterm exam date.
4. Distributes study sections evenly across available days, balancing workload.
5. Generates a CSV-formatted schedule with columns: Date, Course, Section, Workload (minutes).

**Output**: CSV string with daily study tasks including:
- Date (YYYY-MM-DD format).
- Course code.
- Section/chapter title.
- Estimated study time in minutes.

## Tech Stack

* **Python** - Core programming language for all backend logic.
* **Google ADK** - Agent Development Kit for multi-agent orchestration and workflow management.
* **Google Generative AI** - Gemini model integration for intelligent document analysis and planning.
* **LiteLLM** - Unified interface supporting multiple LLM providers (Ollama, OpenAI, etc.).
* **PyMuPDF** - PDF parsing, text extraction, and table of contents analysis.
* **pymupdf4llm** - LLM-optimized PDF to Markdown conversion for document processing.
* **Pydantic** - Data validation and schema definition for structured agent outputs.

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/nathan-au/bx-study.git
cd bx-study
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate       # macOS / Linux
.venv\Scripts\activate          # Windows
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Configure your models in `config.py`:
```python
RECEPTION_MODEL = "gemini-2.5-flash-lite"
ANALYSIS_MODEL = "gemini-2.5-flash"
ESTIMATION_MODEL = "gemini-2.5-flash"
PLANNING_MODEL = "gemini-2.5-flash"
```

### 5. Set up your Google AI API key (if using Gemini models):
  Create a .env file in the root folder and place your API key like so:
```bash
GOOGLE_API_KEY=YOUR_API_KEY_HERE
```

### 6. Run the ADK Web Developer UI 
```bash
adk web
```

Once the UI is running, you can prompt the agent by providing the file path for your midterm overview and the file path for the course textbook. For example:
```
/path/to/MATH101_Textbook.pdf
/path/to/MATH101_Midterm_Overview.pdf
```

The final output is a CSV-formatted study plan:
```
Date,Course,Section,Workload
2026-02-10,MATH 101,Chapter 1: Introduction,45
2026-02-11,MATH 101,Chapter 2: Derivatives,60
...
```

# Next Steps

- **Web Interface**: Build a user-friendly web UI for uploading PDFs and viewing generated study plans.
- **Calendar Integration**: Export study plans to Google Calendar or Outlook.
- **Progress Tracking**: Add functionality to mark sections as completed and adjust remaining schedule.
- **Difficulty Adjustment**: Allow users to provide feedback on time estimates to improve future predictions.
