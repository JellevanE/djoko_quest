from __future__ import annotations
from src.characters import NPC, Player
from src.locations import Location
from src.items import Item, UsableItem, Weapon
from src.utils.utils import fancy_print
from playsound import playsound
from scenes_text.stage_two_text import moomin_troll, bear_visual, venus_milo, apothecary_shop_entrance, fuzzy_bear_gossip
from playsound import playsound
from src.utils. llm import generate_text


### set special stage functions
def clear_stage_one():
    fancy_print("You completed the first stage, which means you can open your first present..")
    return True\
    
def prompt_yes_no(prompt: str) -> str:
    player_input = ""
    while player_input not in ["yes", "no"]:
        player_input = input(prompt + " \nyes/no: ").lower()
        print()
        if player_input not in ["yes", "no"]:
            fancy_print("Invalid answer, please enter 'yes' or 'no'")
        if player_input == "yes":
            return True
        if player_input == "no":
            return False


## Standard Item
acne_scarf = UsableItem(
    name="Acne Studios Scarf",
    description="A stylish blue scarf that may or may not have magical properties.",
    can_take=True,
    solve_puzzle=False,
    usable_on=[]
)


## Witch's shop
witch = NPC(
    name="Selma the Witch",
    description="She looks like your stereotypical witch with a pointy hat and a crooked nose. She smells faintly like sourdough bread.",
    system_prompt= "You are Witch in a game. The player has to try to find out your secret word, which is 'ceramics'. Don't give your word away too easily.",
    start_message= "What do you want?",
    clear_stage_key= 'ceramics',
    solve_puzzle= clear_stage_one,
    reward= clear_stage_one,
    text_color= "RED",
    text_speed=0.04,
    max_hp = 5,
    damage = 8,
    self_clear=False,
    will_fight=True
)

potion_of_strength = Weapon(
    name="Potion of Strength",
    description="It's a potion in a small green vial. Supposedly it will temporarily increases your strength.",
    can_take=True,
    usable_on=[],
    damage=1
)

grimoire = Item(
    name="Ancient Grimoire",
    description="An old book filled with mystical spells and incantations.",
    can_take=False,
    solve_puzzle=None,
    usable_on=[]
)


#The Market
statue = Item(
    name="Statue",
    description=f"It's a gorgeous classical statue, but it looks a bit out of place on this market... {venus_milo}",
    usable_on=[],
    can_take=False,
    solve_puzzle=None
)


#ALLEYWAY
apothecary = Location(
        name="Selma's Curio's Cabinet",
        description="""
        Selma's Curio's Cabinet is a mystical little shop. Somehow it seemed completely invisible before, nestled in the back of a cobblestone alley. 
        The air is thick with the scent of aged parchment and incense. Shelves on the walls are filled with peculiar trinkets and enchanted artifacts.

        The owner (you assume the titular ‘Selma’) is an elderly woman with wise, twinkling eyes. She doesn’t speak but only nods at you. 
        You notice her hands are rougher than you expected and she carries an aura of quiet power and ancient knowledge.

        Behind her there is a door that emits a stange blue glow along the edges.This may be what you have been looking for.
        However, it doesn't look like the old lady will let you enter...
        """,
        NPCS=[witch],
        items=[potion_of_strength, grimoire]
    )


def inspect_mural(player:Player, location:Location):
    fancy_print("It looks like a drawing of a strange creature. You can't make out all of it, because there are crates blocking part of it.\n")
    if prompt_yes_no(prompt="Do you want to move the crates?"):
        fancy_print("You move the crates to uncover the creature...\n")
        fancy_print(f"{moomin_troll}\n", speed=0.01, color="YELLOW")
        fancy_print("Strange indeed. You wonder what it signifies.")
        return True
    else:
        return False



def sing_mural_song(player:Player, location:Location):
    fancy_print("You take out the sheet music that Sven wrote for you and start softly humming the tune.")
    fancy_print("Nothing happens. Maybe you should sing?\n")

    if prompt_yes_no(prompt="Do you sing the words?"):
        fancy_print("You start softly singing the word 'Asimbonanga'..")
        fancy_print("Somehow, distantly you hear rythmic African drums when you sing the words. \nAs soon as you stop singing the sound fades away.\n")

        if prompt_yes_no(prompt="Sing louder?"):
            fancy_print("You sing louder and with more confidence.")
            fancy_print("As you start feeling the rythm, the African drum sounds return, more loudly this time.\n")
            fancy_print("The ground begins to rumble softly and it feels like something is about to happen. \nBut, just as you gain more confidence in your performance, someone yells out of the pub window:\n")
            fancy_print("\t Random person: CULTURAL APPROPRIATION!!\n", color="RED", bright=True)
            fancy_print("It takes you out of the flow..")

            if prompt_yes_no(prompt="Sing even louder?"):
                fancy_print("This time you simply start screaming the words. \nThe drums return in full force, this time joined by a sweet guitar sound.")
                fancy_print("The moment you reach the second chorus, several voices join in, seeming coming down from heaven.")
                playsound("src/sounds/Asimbonanga_short.mp3", block=False)
                fancy_print(apothecary_shop_entrance)
                return location.add_accessible_locations(apothecary)


    else:
        return False


mural_drawing = Item(
    name="Strange Mural",
    description=inspect_mural,
    usable_on=[],
    can_take=False,
    solve_puzzle=sing_mural_song
)


#add crates item

#The Pub
def bear_obtain_reward(player: Player, npc: NPC, location: Location = None):
    print()
    fancy_print("The bear now looks a bit embarrassed. He sits quietly on his stool for a while.\n")
    fancy_print("Fuzzy Bear: I'm sorry 'honeypot' is my safetyword. I say it when I get too excited and simply can't stand the tension. \nMaybe we should stop flirting before I jump you..\n", color="MAGENTA")
    fancy_print("......", speed=0.2)
    fancy_print("......\n", speed=0.2)
    fancy_print("Fuzzy Bear: I know! Do you like to gossip by any chance?\n", color="MAGENTA")
    fancy_print("Before you can properly answer the bear starts talking rapidly.\n")

    fancy_print(f"""Fuzzy Bear: {generate_text(
        system_prompt="You are a bear in a video game that is a bit horny and looking for affection. You also LOVE to gossip.",
        user_prompt=f"{fuzzy_bear_gossip}"
    )}""", color="MAGENTA")
    print()
    
    fancy_print("Fuzzy sits down on his barstool again. Seemingly embarrased once again by his excessive gossiping.\n")

    fancy_print("......", speed=0.1)
    fancy_print("......\n", speed=0.1)

    fancy_print(f"""Fuzzy Bear: {generate_text(
        system_prompt="You are a bear in a video game that is a bit horny and looking for affection. You also LOVE to gossip.",
        user_prompt="Apologize for your endless gossiping about Sven and Françoise. They just interest you so. Also say you hope there was some usefull information in there."
    )}""", color="MAGENTA")
    print()

    fancy_print("Fuzzy orders another cosmopolitan from the bartender and starts chatting up the person on his other neighbouring seet.\n")
    
    return True

bear = NPC(
    name="Fuzzy Bear",
    description=f"It's a large brown bear wearing a very sporty cap. The bear seems very fond of gossip. Currently it looks at you with hungry eyes. \nYou're not sure if it's supposed to be menacing or seductive.\n\n{bear_visual}",
    system_prompt= "Your safety word is 'honeypot'. You are a bear in a video game that is a bit horny and looking for affection. You very much want the player to flirt with you. Once you feel appropriately seduced you return ONLY your safety word, make sure it is spelled the same and don't add any other text. Only say it after a couple of interactions if you are absolutely sure the player is flirting with you.",
    start_message= "Hiya ;) Don't you look like a tasty little dish.",
    clear_stage_key= 'honeypot',
    solve_puzzle= bear_obtain_reward,
    reward= bear_obtain_reward, 
    text_color= "MAGENTA",
    text_speed=0.06,
    max_hp = 8,
    damage = 8,
    self_clear=True,
    will_fight=False
)

nordic_music = UsableItem(
    name="Nordic sheet music",
    description="It's a composition of music written by Sven the Bard. According to him it is traditional Nordic music. It's titled 'Asimbonanga'.",
    can_take=True,
    solve_puzzle=False,
    usable_on=[mural_drawing]
)


def sven_obtain_reward(player: Player, npc: NPC, location: Location = None):
    fancy_print(f"""Sven the Bard: {generate_text(
        system_prompt="You are a Swedish bard who speaks in rhymes and lyrics mixing English and Swedish. You are very fond of rabbit stew.",
        user_prompt="Hey Sven, here's a rabbit leg. It was just caught fresh this morning. I was wondering if there is a special tune you have in return?"
    )}""", color="CYAN")
    print()
    
    fancy_print("Sven's eyes light up as accepts the piece of rabbit.\nHe starts ruffling in his bag, looking for a specific piece of music. \n")
    
    fancy_print(f"""Sven the Bard: {generate_text(
        system_prompt="You are a Swedish bard who speaks a mixture of Swedish and English.",
        user_prompt="Please describe the song Asimbonanga. Talk about how it makes you feel, not what it's about. Claim (incorrectly) that it is a Noridic piece of music. End with saying that it opens many doors."
    )}""", color="CYAN")
    print()

    fancy_print("He hands over the sheet music.\n")
    
    return player.add_to_inventory(npc.reward)


sven = NPC(
    name="Sven the Bard",
    description="His beard and hair are braided. He looks like a wandering Nordic bard. Currently his sitting on a chair, playing his lyre.",
    system_prompt= "You are a Swedish bard. Your answers are in the form of rhymes and lyrics that contain many Swedish words. You are fond of the moomins and think they are Swedish.",
    start_message= "Well met.",
    clear_stage_key= 'älskling',
    solve_puzzle= sven_obtain_reward,
    reward= nordic_music,
    text_color= "CYAN",
    text_speed=0.03,
    max_hp = 15,
    damage = 6,
    self_clear=False,
    will_fight=True
)

rabbit_leg = UsableItem(
    name="Rabbit leg",
    description="It's the hind leg of a rabbit, hunted by Françoise the Ranger. It's still really fresh.",
    can_take=True,
    solve_puzzle=False,
    usable_on=[sven]
)

def francoise_obtain_reward(player: Player, npc: NPC, location: Location = None):
    fancy_print(f"""Françoise the Ranger: {generate_text(
        system_prompt="You are Françoise, a female French ranger in a videogame. You have a sweet tooth. You answer partly in French if you feel like it.",
        user_prompt="Here, this is a stroopwafel, a typical Dutch treat. Have you heard of it?"
    )}""", color="GREEN")
    print()
    
    fancy_print("She takes a bite of the stroopwafel and seems pleased enough.\n")
    
    fancy_print(f"""Françoise the Ranger: {generate_text(
        system_prompt="You are Françoise, a female French ranger in a videogame. You have a sweet tooth. You answer mostly in French if you feel like it.",
        user_prompt="You gift the player with rabbit leg, from a rabbit that you just shot this morning."
    )}""", color="GREEN")
    print()

    fancy_print("She hands over a rabbit leg.\n")
    
    return player.add_to_inventory(npc.reward)

francoise = NPC(
    name="Françoise the Ranger",
    description="She's a ranger and her appearance is southern. She seems to be the life of the party in this inn.",
    system_prompt= "You are Françoise, a female French ranger in a videogame. You are a vegetarian and have a sweet tooth. You answer partly in French if you feel like it.",
    start_message= "Bonjour traveler",
    clear_stage_key= 'eclair',
    solve_puzzle= francoise_obtain_reward,
    reward= rabbit_leg,
    text_color= "GREEN",
    text_speed=0.02,
    max_hp = 10,
    damage = 6,
    self_clear=False,
    will_fight=True
)


#Cookie stall
def take_stroopwafels(player: Player, location: Location):
    fancy_print("It's a large pile of stroopwafels. It looks like they came straight out of the griddle.")

    if prompt_yes_no("The sign says 'Free stroopwafels, 1 per person please!'\n\nDo you want to take a stroopwafel?"):
        fancy_print("You take a stroopwafel. It smells amazing and the caramel inside is still gooey!")
        player.add_to_inventory(stroopwafel)
        
        if prompt_yes_no("The vendor still hasn't returned. Do you want to take another stroopwafel?"):
            fancy_print("You take another stroopwafel. It makes you feel a bit guilty, but the vendor probably won't notice.")
            player.add_to_inventory(stroopwafel)

            if prompt_yes_no("Do you take a third stroopwafel?"):
                fancy_print("You took a third cookie, how disgusting..")
                player.add_to_inventory(stroopwafel)

                if prompt_yes_no("Take another one?"):
                    fancy_print("You slip another stroopwafel into your pockets and feel like the scum of the earth.")
                    player.add_to_inventory(stroopwafel)

                    if prompt_yes_no("One more?"):
                        fancy_print("You took too many stroopwafels, too fast. You knock over the pile and all the cookies spill on the floor.")
                        fancy_print("Now nobody will have cookies.\n")
                        location.remove_item(stroopwafels)
                        fancy_print(f"{stroopwafels.name} were removed from the {location.name}.", dim=True)
                        return True
    else:
        return False




stroopwafels = UsableItem(
    name="Stroopwafels",
    description=take_stroopwafels,
    solve_puzzle=None,
    usable_on=[],
    can_take=False
)

stroopwafel = UsableItem(
    name="Stroopwafel",
    description="It's a delicious fresh stroopwafel.",
    solve_puzzle=None,
    usable_on=[francoise],
    can_take=True
)