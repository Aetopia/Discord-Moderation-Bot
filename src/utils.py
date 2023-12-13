from disnake import Member, CmdInter


class GuildMember():
    def __init__(self, inter: CmdInter, member: Member) -> None:
        self.inter = inter
        self.member = member

    @property
    def owner(self) -> bool:
        return self.member == self.inter.guild.owner
