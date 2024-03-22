import dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

from characters import Character

#load api key
dotenv.load_dotenv()


def create_llm(max_tokens=None):
    """Initiates an OpenAI chat completions llm"""
    return ChatOpenAI(model= "gpt-3.5-turbo-0125", temperature=0.7, max_tokens=max_tokens)


def create_chat_prompt(character:Character):
    """Creates a system prompt for a specific character"""
    system_prompt = character.system_prompt
    start_message = character.start_message
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"{system_prompt}",
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            ('ai', f"{start_message}"),
            ('human', "{input}")
        ]
    )


def create_chat_chain(character:Character):
    """Initiates a chat chain with conversation memory"""
    llm = create_llm()
    prompt = create_chat_prompt(character=character)
    chain = prompt | llm
    chat_history = ChatMessageHistory()
    return RunnableWithMessageHistory(
        chain,
        lambda session_id: chat_history,
        input_messages_key="input",
        output_messages_key="output",
        history_messages_key="chat_history"
        )