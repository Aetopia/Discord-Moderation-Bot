from disnake.ext.commands import Bot, slash_command, option_enum, CommandError
from disnake import CmdInter, Member
from datetime import timedelta
from cogs.errorhandler import ErrorHandler
from utils import *

class Timeout(ErrorHandler):
    def __init__(self, bot: Bot):
        self.bot = bot

    @slash_command()
    async def timeout(self, inter: CmdInter):
        """Timeout a member."""
        pass

    @timeout.sub_command()
    async def add(inter: CmdInter, *, member: Member, reason: str, duration:  option_enum({"1 Day": 1, "7 Days": 7, "28 Days": 28})):
        """Timeout a member with a reason and a certain duration."""
        guildmember = GuildMember(inter, member).owner
        await member.timeout(duration=timedelta(days=duration), reason=reason)
        await inter.send(f"Timed out {member.mention} for {duration} day{"s" if duration > 1 else ""}.")

    @timeout.sub_command()
    async def remove(inter: CmdInter, *, member: Member, reason: str):
        """Remove a timeout from a member."""
        await member.timeout(duration=None, reason=reason)
        await inter.send(f"Removed timeout for {member.mention}.")


def setup(bot: Bot):
    print("Loaded Timeout Cog")
    bot.add_cog(Timeout(bot))
