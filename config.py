from google.adk.models.lite_llm import LiteLlm

# MODEL=LiteLlm(model="ollama_chat/granite4:latest") 
MODEL=LiteLlm(model="ollama_chat/qwen3:latest")

RECEPTION_MODEL=ANALYSIS_MODEL=ESTIMATION_MODEL=PLANNING_MODEL=MODEL

# RECEPTION_MODEL="gemini-2.5-flash-lite"
# ANALYSIS_MODEL=ESTIMATION_MODEL=PLANNING_MODEL="gemini-2.5-flash"
