import disnake
from disnake import message
from disnake.ext import commands
from disnake.ext.commands import command, has_permissions, bot_has_permissions
from disnake.ui import View, Button, button
from disnake import ButtonStyle, Interaction
from disnake.ui import Select, View
from disnake import User, NotFound, Forbidden, HTTPException
from disnake.ext.commands import Context
import datetime

class Staff(commands.Cog):
    client = commands
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Staff Cog is online.')


    def check_id(inter):
        ids = [649280874550132746]
        role = disnake.utils.get(inter.guild.roles, name="Game Moderation")
        if inter.author.id in ids or role in inter.author.roles:
            return True


    @commands.slash_command(description="Game Moderation role required. Requests assistance in-game (requests more staff members to join).")
    @commands.check(check_id)
    @commands.cooldown(1, 1800, commands.BucketType.default)
    async def assistance(self, inter):
        channel = self.client.get_channel(876781598937346109)
        embed = disnake.Embed(title="Staff requires in-game Assistance!")
        embed = disnake.Embed(timestamp=inter.created_at)
        button = disnake.ui.Button(label="Join Server to Assist", style=disnake.ButtonStyle.green, emoji="📲", url="https://policeroleplay.community/join/larpc")
        embed.add_field(name="Please join up the server and log on-duty!",
                        value="Don't forget to act mature and professional at all time!",
                        inline=False)
        #await channel.send('<@&999955672827432980>', embed=embed, components=[button])
        await channel.send(embed=embed, components=[button])
        await inter.response.send_message(f"Hey, {inter.author.mention}! I successfully requested assistance in <#876781598937346109>!")
        

    @assistance.error
    async def assistance_error(self, message, error):
        if isinstance(error, commands.CommandOnCooldown):
            await message.send(f"The assistance command is on cooldown. Retry in **{int(error.retry_after // 60)} minutes**.")

        elif isinstance(error, commands.CheckFailure):
            await message.send(f"Fuck you! You do not have permission :angry:")
        else:
            raise error
    

    @commands.slash_command(description="Game Moderation role required. Shows all game staff announcements.")
    @commands.check(check_id)
    async def announcements(self, inter):
        embed = disnake.Embed(title="**Game Staff Announcements**")
        embed = disnake.Embed(timestamp=inter.created_at)
        embed.add_field(name="**Discord Announcements**",
                        value="`:m Make sure to join our communications, as it's a MUST! .gg/larpc`\n`:h We’re currently hiring and looking to expand our Game Staff Team! Apply today! .gg/larpc`\n`:h Ever wanted to be a member of a specific Department or Division? Apply today! .gg/larpc`",
                        inline=False)
        embed.add_field(name="**Game Announcements**",
                        value="""
                        `:m Peacetime is now in effect. You can see this by the message at the map! When that message is gone, then peacetime is off! This means, No shooting! Always pull over for cops! No robberies! etc. Breaking peacetime means that you'll be instantly kicked!`\n`:m Peacetime is now over! This means that you can go back to NORMAL roleplay!`\n`:m Hello. Three Guys is Open. Stop by if your feeling hungry.`\n`:m Hello. Three Guys is currently hiring workers at the moment. Contact Owner (name) for more information.`\n
                        """, inline=False)
        embed.add_field(name="Game Announcements 2", value="""
        `:m Hello. The Taxi and Limo company is available for service. Contact them if you need a ride.`\n`:m Hello. The Taxi and Limo Service company is currently hiring workers at the moment. Contact Owner (name) for more information.`\n`:m Hello. The J Store is open. Stop by if your looking for some fancy jewels.`\n`:m Hello. The J Store is currently hiring workers at the moment. Contact Owner (name) for more information.`\n`:m Hello. The LA General Hospital is open. Stop by if your not feeling good and need some medicine`.\n`:m Hello. The LA General Hospital is hiring workers at the moment. Contact (Name) for more information`
        """)
        await inter.response.send_message(embed=embed)

    @commands.slash_command(description="Game Moderation role required. Shows everything needed for an STS.")
    @commands.check(check_id)
    async def stsinfo(self, inter):
        embed = disnake.Embed(title="**STS Information**")
        embed = disnake.Embed(timestamp=inter.message.created_at)
        embed.add_field(name="**STS Handbook**", value="https://docs.google.com/document/d/1Lup_S7350JgXd5adk0QgbfelWO4vVDK10ZIESu_9M2c/edit?usp=sharing", inline=False)
        embed.add_field(name="**STS Script**", value="https://discord.com/channels/789978424646828042/925702293402304532/1029424293945294979")
        await inter.response.send_message(embed=embed)

    @commands.slash_command(description="DMs Member")
    @commands.has_role("Owner")
    async def dm(self, inter, member: disnake.Member = None, *, content=None):
        await member.send(content)
        await inter.response.send_message(f"I successfully sent message with content ``{content}`` to {member} (ID: {member.id})")



def setup(client):
    client.add_cog(Staff(client))