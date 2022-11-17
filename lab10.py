from datetime import datetime

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

#Python3
class Logger(metaclass=Singleton):
    DEBUG = False
    PADDING = 9
    
    def __init__(self, filename = None):
        if filename is None:
            today = datetime.now().today()
            self.filename = f"log{today.day}-{today.month}-{today.year}.log"
        
    def log(self, msg, level = "INFO"):
        """Log at level"""
        with open(self.filename, "a") as file:
            type = level.ljust(self.PADDING)
            currentTime = datetime.now()
            file.write(f"|{type}|{currentTime.hour}:{currentTime.minute}:{currentTime.second}| {msg}\n")
            
    def debug(self, msg):
        """Only logs if the static variable {DEBUG} is set to True."""
        if not self.DEBUG:
            return
        self.log(msg, "DEBUG")
            
    def info(self, msg):
        """Log info"""
        self.log(msg, "INFO")

    def warning(self, msg):
        """Log warning"""
        self.log(msg, "WARNING")
        
    def error(self, msg):
        """Log error"""
        self.log(msg, "ERROR")
    
    def critical(self, msg):
        """Log critical"""
        self.log(msg, "CRITICAL")
        
    def clear(self):
        """Clears the log file"""
        with open(self.filename, "r+") as file:
            file.truncate(0)

if __name__ == "__main__":
    logger = Logger()
    logger.debug("A DEBUG Message")
    logger.info("An INFO")
    logger.warning("A WARNING")
    logger.error("An ERROR")
    logger.critical("A message of CRITICAL severity")
    
    logger2 = Logger()
    logger2.clear()
    logger2.DEBUG = True
    logger2.debug("A DEBUG Message")
    logger2.info("An INFO")
    logger2.warning("A WARNING")
    logger2.error("An ERROR")
    logger2.critical("A message of CRITICAL severity")