import dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


#load api key
dotenv.load_dotenv()


def create_llm(max_tokens=None):
    """Initiates an OpenAI chat completions llm"""
    return ChatOpenAI(model= "gpt-3.5-turbo-0125", temperature=1, max_tokens=max_tokens)


chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "{system_prompt}"),
        ("user", "{user_prompt}"),
    ]
)


def chat_prompt(system_prompt, user_prompt):
    return chat_template.format_messages(system_prompt=system_prompt, user_prompt=user_prompt)


def generate_text(system_prompt, user_prompt) -> str:
    """generate an llm response by providing the role of the model and the question"""
    prompt = chat_prompt(system_prompt=system_prompt, user_prompt=user_prompt)
    llm = create_llm()
    return llm.invoke(prompt).content