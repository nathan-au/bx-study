from google.adk.agents import SequentialAgent
from agents.reception_agent import reception_agent

root_agent = SequentialAgent(
    name="pdf_summary_pipeline",
    sub_agents=[
        reception_agent,
    ],
)