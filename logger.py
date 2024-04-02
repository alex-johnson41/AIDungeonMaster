# If we add a GUI at some point, this class can be easily
# adapted to send messages to the GUI instead of the console.
class Logger:
    def __init__(self, debug: bool = False):
        self.debug = debug

    # Use to print messages we want the player to see
    def log(self, message: str) -> None:
        print(message)

    # Use to print messages we want to see, but not the player
    def debug_log(self, message: str) -> None:
        if self.debug:
            print(message)
    
    # Use to get input from the player
    def input(self, message: str) -> str:
        response = input(message)
        if response == "/help":
            self.log("Commands: ")
            self.log("/exit - Exits the game")
            self.log("/debug - Toggles debug mode")
            self.log("/inventory - Displays your inventory (only available in game)")
            self.log("/help - Displays this message")
        elif response == "/exit":
            exit()
        elif response == "/debug":
            self.debug = not self.debug
            self.log(f"Debug mode set to: {self.debug}")
        return response