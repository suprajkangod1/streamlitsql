
from langchain.memory import ConversationBufferMemory

def get_memory():
    """
    Returns a LangChain ConversationBufferMemory instance.
    Attach to agent chain to enable context retention.
    """
    return ConversationBufferMemory(memory_key="chat_history", return_messages=True)
