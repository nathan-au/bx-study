from google.adk.models.lite_llm import LiteLlm

# MODEL=LiteLlm(model="ollama_chat/qwen3:latest")


RECEPTION_MODEL="gemini-2.5-flash-lite"
ANALYSIS_MODEL=ESTIMATION_MODEL=PLANNING_MODEL="gemini-2.5-flash"


# Mistral family
mistral_small = LiteLlm(model="ollama_chat/mistral-small3.2:latest") #too slow
mistral_nemo = LiteLlm(model="ollama_chat/mistral-nemo:latest") #json invalid, artifacts saved
mistral_standard = LiteLlm(model="ollama_chat/mistral:latest") #invalid json

# Qwen family
qwen2 = LiteLlm(model="ollama_chat/qwen2:latest") #saved both artifacts twice and then error
qwen2_5 = LiteLlm(model="ollama_chat/qwen2.5:latest") #lots of thoughts but no final output
qwen3 = LiteLlm(model="ollama_chat/qwen3:latest") #produced a csv output but did not get section titles and took a long time

# Llama family
llama3_1 = LiteLlm(model="ollama_chat/llama3.1:latest") #only saved 1 artifact
llama3_2 = LiteLlm(model="ollama_chat/llama3.2:latest") #invalid json

# Specialized & Other models
lfm_thinking = LiteLlm(model="ollama_chat/lfm2.5-thinking:latest") #too much thinking
granite4 = LiteLlm(model="ollama_chat/granite4:latest") #only saved 1 artifact


# MODEL=mistral_standard
# RECEPTION_MODEL=ANALYSIS_MODEL=ESTIMATION_MODEL=PLANNING_MODEL=MODEL


# DOES NOT SUPPORT TOOLS

gemma3 = LiteLlm(model="ollama_chat/gemma3:latest")
deepseek_r1 = LiteLlm(model="ollama_chat/deepseek-r1:latest")
phi4 = LiteLlm(model="ollama_chat/phi4:latest")

