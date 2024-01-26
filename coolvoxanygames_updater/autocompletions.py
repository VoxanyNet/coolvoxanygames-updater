import discord

async def owned_games(ctx: discord.AutocompleteContext):
    owned_games: dict = ctx.bot.owned_games

    user_owned_games: list = owned_games[
        str(ctx.interaction.user.id)
    ]

    if user_owned_games == []:
        return ["No owned games"]

    return user_owned_games

