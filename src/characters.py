import dotenv
import pprint
from colored import fg, cprint
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

from src.utils.utils import fancy_print
from src.utils.healthbar import Healthbar


# Defining the character object and it's methods

class Character:
    def __init__(self, name:str, hp:int, damage:int) -> None:
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
        pass

    def attack(self, target):
        target.hp -= self.damage
        target.hp = max(target.hp, 0)
        target.health_bar.update()
        fancy_print(f"{self.name} dealt {self.damage} damage to {target.name}")


class Player(Character):
    def __init__(self, name:str, starting_location, max_hp=10):
        super().__init__(name=name, hp=max_hp, damage=2)
        self.current_location = starting_location
        self.inventory = []
        self.health_bar = Healthbar(self, color="green")

    def move_to(self, new_location):
        self.current_location = new_location
        print(f"{self.name} has moved to {new_location}.")

    def add_to_inventory(self, item:str):
        self.inventory.append(item)
        print(f"{item} has been added to your inventory.")

    def check_inventory(self):
        pprint.pprint(f"Your inventory contains: {self.inventory}")



class NPC(Character):
    def __init__(self, name:str, max_hp:int, damage:int, description:str, system_prompt:str, start_message:str, clear_stage_key:str, text_color, text_speed:float, next_stage) -> None:
        super().__init__(name=name, hp=max_hp, damage=damage)
        self.description = description
        self.system_prompt = system_prompt
        self.start_message = start_message
        self.clear_stage_key = clear_stage_key
        self.next_stage = next_stage
        self.text_color = text_color
        self.text_speed = text_speed
        self.health_bar = Healthbar(self, color="red")
        pass

    def __str__(self) -> str:
        return f"{self.name} Character"
    
    def talk(self, user_name):
        """Starts a conversation with a character using the chat chain"""
        #initiate chat chain llm
        chat_chain = create_chat_chain(character=self)

        #print initial message
        fancy_print(text=f"\t{self.name}: {self.start_message}", color=self.text_color, speed=self.text_speed) 
        user_input = ""

        #start conversation loop
        while self.clear_stage_key not in user_input.lower():
            user_input = input(f"\t{user_name}: ")
            response = chat_chain.invoke(
                {"input": f"{user_input}"},
                {"configurable": {"session_id": "unused"}})
            fancy_print(text=f"\t{self.name}: {response.content}", speed=self.text_speed, color=self.text_color)

        return self.next_stage()
    
    def inspect(self):
        print(f"You look at {self.name} more closely...")
        return fancy_print(self.description)

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