

class Character:
    def __init__(self, name, system_prompt, start_message) -> None:
        self.name = name
        self.system_prompt = system_prompt
        self.start_message = start_message
        pass

    def __str__(self) -> str:
        return f"{self.name} Character"
    
    def create_llm():
        pass
        

Wizard = Character(
    name="Selma the Witch",
    system_prompt= "You are Witch in a game. The player has to try to find out your secret word, which is 'ceramics'.",
    start_message= "What do you want?"
)