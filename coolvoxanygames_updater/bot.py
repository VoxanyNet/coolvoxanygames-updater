from typing import Dict, Type
import uuid

import discord

from coolvoxanygames_updater import commands

class CoolVoxanyGamesUpdater(discord.Bot):
    def __init__(self, games_folder: str, owned_games, description=None, *args, **options):

        intents = discord.Intents.default()

        super().__init__(description, intents=intents, *args, **options)
        
        self.games_folder = games_folder
        self.owned_games = owned_games
    
        self.add_application_command(commands.update)

        

