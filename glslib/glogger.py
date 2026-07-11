class GLogger:
    def __init__(self, debug_level):
        self.debug_level = debug_level

    def log(self, message):
        print(f"[{self.debug_level}] {message}")

    def die(self, message):
        print(f"[{self.debug_level}] {message}")
        exit(1)