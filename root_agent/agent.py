from google.adk.agents import SequentialAgent
from agents.reception_agent import reception_agent
from agents.analysis_agent import analysis_agent
from agents.estimation_agent import estimation_agent
from agents.planning_agent import planning_agent

root_agent = SequentialAgent(
    name="root_agent",
    sub_agents=[
        reception_agent,
        analysis_agent,
        estimation_agent,
        planning_agent,
    ],
)