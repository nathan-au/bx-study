from google.adk.agents import LlmAgent

summary_agent = LlmAgent(
    name="summary_agent",
    description="Summarizes a short uploaded PDF",
    model="gemini-2.5-flash",
    instruction="The user will upload a short PDF. The PDF text will appear in your input. Your task: Read the content, Produce a concise summary (50 words).",
    # tools=[get_current_time],
)