from colored import fg

class Character:
    def __init__(self, name, system_prompt, start_message, clear_stage_key, text_color) -> None:
        self.name = name
        self.system_prompt = system_prompt
        self.start_message = start_message
        self.clear_stage_key = clear_stage_key
        self.text_color = text_color
        pass

    def __str__(self) -> str:
        return f"{self.name} Character"
        

Wizard = Character(
    name="Selma the Witch",
    system_prompt= "You are Witch in a game. The player has to try to find out your secret word, which is 'ceramics'.",
    start_message= "What do you want?",
    clear_stage_key= 'ceramics',
    text_color= fg('88')
)