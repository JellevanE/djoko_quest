# djoko_quest


# windows

1. Open up a terminal
2. Navigate to the correct directory (\djoko_quest)
3. Create a virtual environment (.venv)
    For Command Prompt (windows)
    3a. pip install virtualenv (if venv not installed)
    3b. virtualenv --python C:\Path\To\Python\python.exe venv
    3c. .\venv\Scripts\activate
    
    For Powershell activation (windows)
    3a. Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
    3b. .venv/Scripts/activate.ps1
4. Install requirements to virtual environment
    4a. pip install -r requirements.txt
5. Run the game
    5a. python main.py