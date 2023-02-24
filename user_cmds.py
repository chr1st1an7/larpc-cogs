import disnake
from disnake import message
from disnake.ext import commands
from disnake.ext.commands import command, has_permissions, bot_has_permissions
from disnake.ui import View, Button, button
from disnake import ButtonStyle, Interaction

class UserCmds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'UserCmds Cog is online.')

    
    # ------------------------ Commands

    @commands.command()
    async def ping(self, ctx):
        latency = round(self.client.latency * 1000)

        await ctx.send(f'Pong! Latency: {latency}ms')

    
def setup(client):
    client.add_cog(UserCmds(client))