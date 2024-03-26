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