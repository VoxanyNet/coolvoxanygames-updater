import shutil

import discord

from coolvoxanygames_updater import autocompletions

@discord.commands.application_command(description="Upload an update")
async def update(
        ctx: discord.ApplicationContext, 
        file: discord.Option(discord.SlashCommandOptionType.attachment, description="Game zip file"),
        game: discord.Option(str, autocomplete=autocompletions.owned_games)
    ):
    
    ZIP_SAVE_PATH = f"/tmp/{file.filename}"
    USER_GAME_PATH = f"{ctx.bot.games_folder}/{game}"

    try:
        await file.save(ZIP_SAVE_PATH)
    except:
        await ctx.respond("Failed to download update", ephemeral=True)
        
        return

    try:
        shutil.unpack_archive(ZIP_SAVE_PATH, USER_GAME_PATH)
    except:
        await ctx.respond("Failed to unpack update", ephemeral=True)

        return

    await ctx.respond(f"**Update complete!** ✅ \n\n[Play it!](https://games.voxany.net/games/{game}/index.html)".replace(" ", "%20"), ephemeral=True)