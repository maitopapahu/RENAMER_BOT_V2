from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "7529913637:AAFr-E6m5HRQLwhCRGUZBhT9pUfzcwRnG4Q")

API_ID = int(os.environ.get("API_ID", "29696002"))

API_HASH = os.environ.get("API_HASH", "b0402db44bb51470d0c50d3be950781b")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
