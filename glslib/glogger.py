import sys

class GLogger:
    INFO = 1
    DEBUG = 2
    WARN = 4
    ERROR = 8

    def __init__(self, module_name, debug_level: int = 0):
        self.module_name = module_name
        self.debug_level = debug_level
        import sys

    def info(self, message, *argv):
        if self.debug_level & self.INFO:
            print(f"INFO: [{self.module_name}] {message}", *argv, file=sys.stderr)

    def debug(self, message, *argv):
        if self.debug_level & self.DEBUG:
            print(f"DEBUG: [{self.module_name}] {message}", *argv, file=sys.stderr)

    def warn(self, message, *argv):
        if self.debug_level & self.WARN:
            print(f"WARN: [{self.module_name}] {message}", *argv)

    def print(self, message, *argv):
        print(f"{message}", *argv)

    def error(self, message, *argv):
        if self.debug_level & self.ERROR:
            print(f"ERROR: [{self.module_name}] {message}", *argv, file=sys.stderr)

    def critical(self, message, *argv):
        print(f"CRITICAL: [{self.module_name}] {message}", *argv, file=sys.stderr)

    def die(self, message, *argv):
        self.critical(message, *argv)
        sys.exit(1)
