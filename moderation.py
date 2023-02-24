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

class Moderation(commands.Cog):
    client = commands
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Moderation Cog is online.')

    # ------------------------ Commands
    def has_owner():
        def predicate(ctx):
            ids = [role.id for role in ctx.author.roles]
            return bool([rid for rid in [789978655044272148, 1007687842526412810] if rid in ids])
        return commands.check(predicate)

    @commands.command()
    @has_owner()
    async def gkick(self, ctx: Context, user: User, *, reason: str = None) -> None:
        await user.send(embed=disnake.Embed(
            color=disnake.Color.blue(),
            title="**Notification**",
            description=(
            "You have been **NETWORK KICKED** from all servers related" +
            f" to **``{ctx.guild.name}``** (ID: {ctx.guild.id}). You have been been network kicked for ``{reason}``."
            )
        ))

        count = 0
        for guild in ctx.bot.guilds:
            count += 1
            try:
                await guild.kick(user, reason=reason)
            except (NotFound, Forbidden, HTTPException):
                count -= 1

        await ctx.send(f"Kicked `{user}` from {count}/{len(ctx.bot.guilds)} guilds.")

        embed1 = disnake.Embed(
            color=disnake.Color.green(), title="",
            description=f"<:success:993221530936950874> ***{user} (ID: {user.id}) was network kicked*** | {reason}")
        embed1.set_footer(text=disnake.utils.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
        embed2 = disnake.Embed(
            color=disnake.Color.red(), title=f"Network Kicked | {user}",
            description=f"***{user} (ID: {user.id}) was network kicked*** by {ctx.author} | {reason}")
        embed2.set_footer(text=disnake.utils.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

        await ctx.send(embed=embed1)
        logs = disnake.utils.get(ctx.guild.channels, name="punishment-logs")
        await logs.send(embed=embed2)

    @commands.command()
    @has_owner()
    async def gban(self, ctx: Context, user: User, *, reason: str = None) -> None:
        await user.send(embed=disnake.Embed(
            color=disnake.Color.blue(),
            title="**Notification**",
            description=(
            "You have been **NETWORK BANNED** from all servers related" +
            f" to **``{ctx.guild.name}``** (ID: {ctx.guild.id}). You have been been network banned for ``{reason}``."
            f"You may be able to appeal this punishment at our [Ban Appeals Server](https://discord.gg/DH9Pc8rGEC)."

            )
        ))

        count = 0
        for guild in ctx.bot.guilds:
            count += 1
            try:
                await guild.ban(user, reason=reason)
            except (NotFound, Forbidden, HTTPException):
                count -= 1

        await ctx.send(f"Banned `{user}` from {count}/{len(ctx.bot.guilds)} guilds.")

        embed1 = disnake.Embed(
            color=disnake.Color.green(), title="",
            description=f"<:success:993221530936950874> ***{user} (ID: {user.id}) was network banned*** | {reason}")
        embed1.set_footer(text=disnake.utils.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
        embed2 = disnake.Embed(
            color=disnake.Color.red(), title=f"Network Banned | {user}",
            description=f"***{user} (ID: {user.id}) was network banned*** by {ctx.author} | {reason}")
        embed2.set_footer(text=disnake.utils.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

        await ctx.send(embed=embed1)
        logs = disnake.utils.get(ctx.guild.channels, name="punishment-logs")
        await logs.send(embed=embed2)

    @commands.command()
    @has_owner()
    async def gunban(self, ctx: Context, user: User, *, reason: str = None) -> None:
        await user.send(embed=disnake.Embed(
            color=disnake.Color.blue(),
            title="**Notification**",
            description=(
                    "You have been **NETWORK UNBANNED** from all servers related" +
                    f" to **``{ctx.guild.name}``** (ID: {ctx.guild.id})."

            )
        ))

        count = 0
        for guild in ctx.bot.guilds:
            count += 1
            try:
                await guild.unban(user, reason=reason)
            except (NotFound, Forbidden, HTTPException):
                count -= 1

        await ctx.send(f"Unbanned `{user}` from {count}/{len(ctx.bot.guilds)} guilds.")

        embed1 = disnake.Embed(
            color=disnake.Color.green(), title="",
            description=f"<:success:993221530936950874> ***{user} (ID: {user.id}) was network unbanned*** | {reason}")
        embed1.set_footer(text=disnake.utils.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
        embed2 = disnake.Embed(
            color=disnake.Color.green(), title=f"Network Unbanned | {user}",
            description=f"***{user} (ID: {user.id}) was network unbanned*** by {ctx.author} | {reason}")
        embed2.set_footer(text=disnake.utils.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

        await ctx.send(embed=embed1)
        logs = disnake.utils.get(ctx.guild.channels, name="punishment-logs")
        await logs.send(embed=embed2)

    @commands.command(description="Admin permissions required. Mutes a member.")
    @commands.has_role("All mod perms")
    async def mute(self, ctx, member: disnake.Member, *, reason =None):
        client = commands
        guildId = ctx.message.guild.id
        guild = client.get_guild(guildId)
        embed = disnake.Embed(
            color=disnake.Color.blue(), title="**Notification**",
            description=f"You have been **muted** in **``{guild.name}``** (ID: {guildId}) for {reason}")
        embed.timestamp = datetime.datetime.utcnow()
        embed1 = disnake.Embed(
            color=disnake.Color.green(), title="",
            description=f"<:success:993221530936950874> ***{member} (ID: {member.id}) was muted*** | {reason}")
        embed.timestamp = datetime.datetime.utcnow()
        embed2 = disnake.Embed(
            color=disnake.Color.red(), title=f"Muted | {member}",
            description=f"***{member} (ID: {member.id}) was muted*** by {ctx.author} | {reason}")
        embed.timestamp = datetime.datetime.utcnow()

        muted_role = disnake.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(muted_role)

        await ctx.send(embed=embed1)
        logs = disnake.utils.get(ctx.guild.channels, name="punishment-logs")
        await logs.send(embed=embed2)
        await member.send(embed=embed)

    @commands.command(description="Admin permissions required. Unmutes a muted member.")
    @commands.has_role("All mod perms")
    async def unmute(self, ctx, member: disnake.Member):
        client = commands
        guildId = ctx.message.guild.id
        guild = client.get_guild(guildId)
        embed = disnake.Embed(
            color=disnake.Color.blue(), title="**Notification**",
            description=f"You have been **unmuted** in **``{guild.name}``** (ID: {guildId})")
        embed.timestamp = datetime.datetime.utcnow()
        embed1 = disnake.Embed(
            color=disnake.Color.green(), title="",
            description=f"<:success:993221530936950874> ***{member} (ID: {member.id}) was unmuted***")
        embed.timestamp = datetime.datetime.utcnow()
        embed2 = disnake.Embed(
            color=disnake.Color.green(), title=f"Unmuted | {member}",
            description=f"***{member} (ID: {member.id}) was unmuted*** by {ctx.author}")
        embed.timestamp = datetime.datetime.utcnow()

        muted_role = disnake.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(muted_role)

        await ctx.send(embed=embed1)
        logs = disnake.utils.get(ctx.guild.channels, name="punishment-logs")
        await logs.send(embed=embed2)
        await member.send(embed=embed)


    @commands.command(description="Kicks a member")
    @commands.has_role("All mod perms")
    async def kick(self, ctx: commands.Context, member: disnake.Member = None, *, reason=None):
        guildId = ctx.message.guild.id
        guild = commands.get_guild(guildId)
        embed = disnake.Embed(
            color=disnake.Color.blue(), title="**Notification**",
            description=f"You have been **kicked** from **``{guild.name}``** (ID: {guildId}) for {reason}")
        embed.timestamp = datetime.datetime.utcnow()
        embed1 = disnake.Embed(
            color=disnake.Color.green(), title="",
            description=f"<:success:993221530936950874> ***{member} (ID: {member.id}) was kicked*** | {reason}")
        embed.timestamp = datetime.datetime.utcnow()
        embed2 = disnake.Embed(
            color=disnake.Color.red(), title=f"Kick | {member}",
            description=f"***{member} (ID: {member.id}) was kicked*** by {ctx.author} | {reason}")
        embed.timestamp = datetime.datetime.utcnow()

        if member == None:
            await ctx.send("You have to specify an user!")
            print('no user')
            return
        if member == ctx.message.author or member == None:
            await ctx.send("You cannot kick yourself!")
            print('yourself')
            return
        if reason == None:
            await ctx.send("You have to specify a reason!")
            print('No reason specified')
            return

        await ctx.send(embed=embed1)
        logs = disnake.utils.get(ctx.guild.channels, name="punishment-logs")
        await logs.send(embed=embed2)
        await member.send(embed=embed)
        await ctx.guild.kick(member, reason=reason)


    @client.command(description="Bans a member")
    @commands.has_role("All mod perms")
    async def ban (self, ctx, member:disnake.User=None, *, reason =None):
        guildId = ctx.message.guild.id
        guild = commands.get_guild(guildId)
        embed = disnake.Embed(
            color=disnake.Color.blue(), title="**Notification**",
            description=f"You have been **banned** from **``{guild.name}``** (ID: {guildId}) for {reason}. You may be able to appeal here: https://discord.gg/DH9Pc8rGEC.")
        embed.timestamp = datetime.datetime.utcnow()
        embed1 = disnake.Embed(
            color=disnake.Color.green(), title="",
            description=f"<:success:993221530936950874> ***{member} (ID: {member.id}) was banned*** | {reason}")
        embed.timestamp = datetime.datetime.utcnow()
        embed2 = disnake.Embed(
            color=disnake.Color.red(), title=f"Ban | {member}",
            description=f"***{member} (ID: {member.id}) was banned*** by {ctx.author} | {reason}")
        embed.timestamp = datetime.datetime.utcnow()

        if member == None:
            await ctx.send("You have to specify an user!")
            print('no user')
            return
        if member == ctx.message.author or member == None:
            await ctx.send("You cannot ban yourself!")
            print('yourself')
            return
        if reason == None:
            await ctx.send("You have to specify a reason!")
            print('No reason specified')
            return

        await ctx.send(embed=embed1)
        logs = disnake.utils.get(ctx.guild.channels, name="punishment-logs")
        await logs.send(embed=embed2)
        await member.send(embed=embed)
        await ctx.guild.ban(member, reason=reason)


    @commands.command(description="Admin permissions required. Unbans a banned member.") #ban
    @commands.has_role("All mod perms")
    async def unban (self, ctx, user:disnake.User=None, *, reason =None):
        guildId = ctx.message.guild.id
        guild = commands.get_guild(guildId)
        embed1 = disnake.Embed(
            color=disnake.Color.green(), title="",
            description=f"<:success:993221530936950874> ***{user} (ID: {user.id}) was unbanned*** | {reason}")
        embed2 = disnake.Embed(
            color=disnake.Color.green(), title=f"Unban | {user}",
            description=f"***{user} (ID: {user.id}) was unbanned*** by {ctx.author} | {reason}")

        await ctx.guild.unban(user, reason=reason)
        print(user)
        print(reason)

        await ctx.send(embed=embed1)
        logs = disnake.utils.get(ctx.guild.channels, name="punishment-logs")
        await logs.send(embed=embed2)
        
    
    @commands.command(description="Admin permissions required. Purges a specified amount of messages.")
    @commands.has_role("All mod perms")
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)



    
def setup(client):
    client.add_cog(Moderation(client))