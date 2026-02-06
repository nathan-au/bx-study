from google.adk.agents import SequentialAgent
from agents.saver_agent import saver_agent


root_agent = SequentialAgent(
    name="pdf_summary_pipeline",
    sub_agents=[
        saver_agent,
    ],
)