from langchain_ollama import ChatOllama

# https://docs.langchain.com/oss/python/integrations/chat/ollama

def check_gender(is_man: bool):
    """Is the user a man?
    Args:
    is_man (bool): yes user is man
    """
    return True


llm = ChatOllama(
    model="qwen3:0.6b",
).bind_tools([check_gender])

message = [
    ("system", "You are a tax accountant"),
    ("human", "I am a woman.")
]

output = llm.invoke(message)
print(output.content)
print(output.tool_calls)