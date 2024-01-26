import os
import json

from coolvoxanygames_updater import bot

DISCORD_TOKEN = os.environ["COOLVOXANYGAMES_UPDATER_BOT_DISCORD_TOKEN"]
GAMES_PATH = os.environ["COOLVOXANYGAMES_UPDATER_GAMES_FOLDER"]
CONFIG_DIRECTORY = os.environ["COOLVOXANYGAMES_UPDATER_CONFIG_DIRECTORY"]

with open(f"{CONFIG_DIRECTORY}/owned_games.json", "w") as file:
    owned_games = json.load(file)

bot = bot.CoolVoxanyGamesUpdater(games_folder=GAMES_PATH, owned_games=owned_games)

bot.run(DISCORD_TOKEN)