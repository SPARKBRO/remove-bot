# remove-bot



Telegram Bot for Removing Users with Russian Alphabet in their Names



This is a Telegram bot that automatically removes users with Russian alphabet in their names from a Telegram channel. The bot is built using Python and the python-telegram-bot library.

Getting Started
Prerequisites

To run the bot, you will need:

🔰Python 3.6 or later
🔰A MongoDB instance for storing data
🔰Telegram API credentials (API ID and API hash) for your bot


Installing

To install the required Python packages, run:

pip install -r requirements.txt

Configuration

The bot is configured using environment variables. You can set the following variables:

🔰BOT_TOKEN: The Telegram bot token.
🔰API_ID: The API ID for your bot.
🔰API_HASH: The API hash for your bot.
🔰DATABASE_URL: The MongoDB database URL.

You can set these variables in a .env file in the root directory of the project. Alternatively, you can set them as environment variables in your operating system.

Usage

To start the bot, run:

python main.py


Deployment
This bot is designed to be deployed on a cloud platform such as Heroku. The Procfile and runtime.txt files are provided for deploying on Heroku.

Built With

python-telegram-bot -
🔰Python library for the
Telegram Bot API
🔰MongoDB - NoSQL database


License

This project is licensed under the MIT License - see the LICENSE.md file for details.

#Deploy
<details><summary>Deploy To Heroku</summary>
<p>
<br>
<a href="https://heroku.com/deploy?template=https://github.com/SPARKBRO/romove-bot">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy To Heroku">
</a>
</p>
</details>

