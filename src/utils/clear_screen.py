import os
# from sys import platform

def clear_screen():
    """Clears console screen for every platform"""
    os.system('cls' if os.name=='nt' else 'clear')


    # #check operating system
    # if platform == "darwin":
    #     # OS X
    #     os.system('clear')
    # if platform == "win32":
    #     # Windows...
    #     os.system('cls')