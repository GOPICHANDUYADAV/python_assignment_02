#logger with singleton pattern
from datetime import datetime

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {message}"
        self.logs.append(entry)
        print(entry)

    def get_log(self):
        return self.logs


# Test
logger1 = Logger()
logger2 = Logger()

print("Same instance:", logger1 is logger2)

logger1.log("Application started")
logger2.log("User logged in")

print(logger1.get_log())