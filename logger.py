# We may want to log the output of the game to a file at some point, 
# so use this class anytime we want to print something, so we can later
# easily change this to write to a file if we want to. 
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