import shutil

import discord

from coolvoxanygames_updater import autocompletions

@discord.commands.application_command(description="Upload an update")
async def update(
        ctx: discord.ApplicationContext, 
        file: discord.Option(discord.SlashCommandOptionType.attachment, description="Game zip file"),
        game: discord.Option(str, autocomplete=autocompletions.owned_games)
    ):

    if game not in ctx.bot.owned_games[str(ctx.interaction.user.id)]:
        await ctx.respond(f"You do not own {game}", ephemeral=True)
        return
    
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
    
    game_link = f"https://games.voxany.net/games/{game}/index.html)".replace(" ", "%20")

    await ctx.respond(f"**Update complete!** ✅ \n\n[Play it!]({game_link})", ephemeral=True)