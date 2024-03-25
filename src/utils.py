import time
import colorama
from colorama import init, Fore, Back, Style
colorama.init(autoreset=True)


def fancy_print(text, speed=0.1, color="WHITE"):
    """
    Print text with a specific speed and color.

    :param text: The text to be printed.
    :param speed: The delay between each character (in seconds).
    :param color: The color of the text. Supports "BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE".
    """
    # Color mapping based on colorama Fore attributes
    color_map = {
        "BLACK": Fore.BLACK,
        "RED": Fore.RED,
        "GREEN": Fore.GREEN,
        "YELLOW": Fore.YELLOW,
        "BLUE": Fore.BLUE,
        "MAGENTA": Fore.MAGENTA,
        "CYAN": Fore.CYAN,
        "WHITE": Fore.WHITE,
    }

    selected_color = color_map.get(color.upper(), Fore.WHITE)
    
    # Print each character with the specified delay
    for char in text:
        print(selected_color + char, end='', flush=True)
        time.sleep(speed)
    
    print()  # Ensure there's a newline at the end


#print(Style.BRIGHT + "this is bright")
#print(Style.DIM + "this is DIM")