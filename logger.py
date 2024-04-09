import os
from pathlib import Path
import time


class Logger:
# If we add a GUI at some point, this class can be easily
# adapted to send messages to the GUI instead of the console.
    def __init__(self, debug: bool = False, create_log_files: bool = True):
        self.debug = debug
        self.create_log_files = create_log_files
        if self.create_log_files:
            dir_path = os.path.join(os.getcwd(), "save")
            os.makedirs(os.path.join(dir_path, "log"), exist_ok=True)
            os.makedirs(os.path.join(dir_path, "story"), exist_ok=True)
            self.story_file = Path(f"save/story/{time.time()}.txt")
            self.log_file = Path(f"save/log/{time.time()}.txt")

    # Use to print messages we want the player to see
    def log(self, message: str, story: bool = False) -> None:
        if self.create_log_files:
            if story:
                self.save_to_story(message)
            self.save_to_log(message)
        print(message)

    # Use to print messages we want to see, but not the player
    def debug_log(self, message: str) -> None:
        if self.debug:
            print(message)
        if self.create_log_files: 
            self.save_to_log(message)
    
    # Use to get input from the player
    def input(self, message: str) -> str:
        response = input(message)
        self.save_to_log(f"{message} {response}")
        if response == "/help":
            self.log("Commands: ")
            self.log("/exit - Exits the game")
            self.log("/debug - Toggles debug mode")
            self.log("/inventory - Displays your inventory (only available in game)")
            self.log("/save - Saves your game and character (only available in game)")
            self.log("/help - Displays this message")
            response = self.input(message)
        elif response == "/exit":
            exit()
        elif response == "/debug":
            self.debug = not self.debug
            self.log(f"Debug mode set to: {self.debug}")
            response = self.input(message)
        return response
    
    def save_to_log(self, message: str) -> None:
        with open(self.log_file, "a+") as f:
            f.write(message + "\n")

    def save_to_story(self, message: str) -> None:
        with open(self.story_file, "a+") as f:
            f.write(message + "\n")