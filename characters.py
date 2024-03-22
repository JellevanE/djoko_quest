import dotenv
from colored import fg, cprint
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

from stages import testing_stage


# Defining the character object and it's methods


class Character:
    def __init__(self, name:str, system_prompt:str, start_message:str, clear_stage_key:str, text_color, next_stage) -> None:
        self.name = name
        self.system_prompt = system_prompt
        self.start_message = start_message
        self.clear_stage_key = clear_stage_key
        self.next_stage = next_stage
        self.text_color = text_color
        pass

    def __str__(self) -> str:
        return f"{self.name} Character"
    
    def talk(self, user_name):
        """Starts a conversation with a character using the chat chain"""
        #initiate chat chain llm
        chat_chain = create_chat_chain(character=self)

        #print initial message 
        cprint(self.text_color + f"{self.name}: {self.start_message} \n")
        user_input = ""

        #start conversation loop
        while self.clear_stage_key not in user_input.lower():
            user_input = input(f"{user_name}: ")
            print('\n')
            response = chat_chain.invoke(
                {"input": f"{user_input}"},
                {"configurable": {"session_id": "unused"}})
            cprint(self.text_color + f"{self.name}: {response.content} \n")

        return self.next_stage()
    
    def fight(self):
        return True

#setting up LLM responses for talk method

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








