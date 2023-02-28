import logging
import telegram
from telegram.ext import Updater, MessageHandler, Filters
from bot import remove_russian_names
from database import Database
from config import Config

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(name)

def main():
    """Start the Telegram bot."""
    # Load configuration from Config class
    config = Config()

    # Connect to the database
    db = Database(config.DATABASE_URL)

    # Create the Telegram bot
    updater = Updater(config.BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add message handler to remove users with Russian alphabet in their names
    dp.add_handler(MessageHandler(Filters.text, remove_russian_names, db))

    # Start the bot
    logger.info("Starting bot...")
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
