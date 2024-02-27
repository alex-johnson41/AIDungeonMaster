# AIDungeonMaster

## Development Instructions

- Download and install Python 3.10.2 or later 
- Create a virtual environment with the packages in requirements.txt
    - Create the venv:
        - ```python3.10 -m venv .venv ```
    - Activate the venv:
        - Linux/MacOS: ```source .venv/bin/activate```
        - Windows: ```./.venv/Scripts/activate```
    - Install dependencies:
        - ```pip install -r requirements.txt```
- Create a config.py file in the project root directory and add your API key to a variable called ```GEMINI_API_KEY```

- You should now be able to run main.py and interact with the program