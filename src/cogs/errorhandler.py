from disnake.ext.commands import Cog, Bot,CommandError
from disnake import CmdInter
from disnake.errors import HTTPException

class ErrorHandler(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_slash_command_error(self, inter: CmdInter, error: CommandError):
        try:
            await inter.send(error.__cause__, ephemeral=True)
        except HTTPException: pass

def setup(bot: Bot): pass
