import time
import sys
import colorama
from colorama import init, Fore, Back, Style

colorama.init(autoreset=True)


def fancy_print(text, speed=0.002, color="WHITE", bright=False, dim=False):
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

    # Style selection
    style = ""
    if bright:
        style = Style.BRIGHT
    elif dim:
        style = Style.DIM


    selected_color = color_map.get(color.upper(), Fore.WHITE)
    
    # Print each character with the specified delay
    for char in text:
        print(style + selected_color + char, end='', flush=True)
        time.sleep(speed)
    
    print()  # Ensure there's a newline at the end


#print(Style.BRIGHT + "this is bright")
#print(Style.DIM + "this is DIM")

def get_valid_input(prompt: str, max_option: int) -> int:
    """
    Prompts the user for input and validates it as an integer within the allowed range.
    
    Args:
    prompt (str): The prompt message to display to the user.
    max_option (int): The maximum valid option number.
    
    Returns:
    int: The validated input from the user as an integer.
    """
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            user_input = int(user_input)
            if 1 <= user_input <= max_option:
                return user_input
            else:
                fancy_print(f"Please enter a number between 1 and {max_option}.")
        else:
            fancy_print("Invalid input. Please enter a number.")