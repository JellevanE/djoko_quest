# **🧚🏻‍♀️ djoko_quest v0.1.1**
Welcome to djoko_quest. This repository was made as a birthday present for the real life djoko, Josephine. 
Djoko_quest is a text based adventure game that makes use of LLM's. Currently it's setup for OpenAI models, but these can be swapped out with other API's or even local models withe relatively low effort.

**Note for the real Djoko:**
You can install and play this game to earn the rest of your presents. Congratulations and good luck!

# Quickstart

1. clone the repository
2. Create a `.env` file and add your OpenAI API key: `OPENAI_API_KEY = "<ADD YOUR KEY HERE>"`
3. Create a virtual environment
4. Install the required packages: `pip install -r requirements.txt`
5. To play the game, run: `python main.py`

# How to play

## General setup
1. Open up a terminal (any terminal)
2. Navigate to the directory you want to clone djoko_quest to
3. Run the following command:
```
git clone https://github.com/JellevanE/djoko_quest.git
```
4. To access the directory run: `cd djoko_quest` or `dir djoko_quest`
5. Create a file named `.env`
6. Place your OpenAI key in this file: `OPENAI_API_KEY = "<ADD YOUR KEY HERE>"`
7. From this point the commands will differ for MacOS / Windows / Linux

## Windows

1. Check your python version (Python 3.10 or newer is preffered): `python --version`
2. Create a virtual environment (steps here use .venv but feel free to use conda or somehting else)
3. If venv is not yet installed run:
```
    pip install virtualenv
```
4. Create your virtual environment:
```
    virtualenv --python C:\Path\To\Python\python.exe venv
``` 
5. Activate your virtual environment, 
- for Command Prompt:
```
.\venv\Scripts\activate
```
If this doesn't work correctly run `.venv\Scripts\activate`
- for Powershell:
```
.venv/Scripts/activate.ps1
```
If this doesn't work correctly, first run `Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force`and then repeat the first command

6. Install the required packages to your virtual environment
```
pip install -r requirements.txt
```
7. Congratulations, you can now start the game. To play, run:
```
python main.py
```

## MacOS (speciaal voor djoko)
1. Navigate to the correct directory (like a dev)

- Open your terminal
- For the true experience: right click on the terminal icon and change the profile by going to 'New window with profile' and select Homebrew or Pro.
- To read your current directory, type: `ls` and hit enter
- Navigate through your directories, type: `cd Documents/` hit enter and then type `cd LIFE/` hit enter again and then type `cd bday 2024`
- You are now in the correct folder

2. Download the game: clone the correct repository from github using the following command:
```
    git clone https://github.com/JellevanE/djoko_quest.git
```
Now enter the correct folder by running: `cd djoko_quest`

3. Use the correct Python version
```
export PATH="$(brew --prefix)/opt/python@3/libexec/bin:$PATH"
```
4. Create a virtual environment (MAC OS)
```
python3 -m venv path/to/venv
```
5. Activate your virtual environment
```
source path/to/venv/bin/activate
```
6. Install the required packages
```
pip install -r requirements.txt
```
7. Congratulations, you can now start the game. To play, run:
```
python main.py
```
