from loguru import logger
from services.telegram_handler import TelegramHandler

def configure_logging():
    logger.add(
        "logs/dino.log",
        rotation="1 MB",
        retention="7 days",
        level="INFO",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
    )
    
if __name__ == "__main__":
    configure_logging()
    bot = TelegramHandler()
    bot.run()