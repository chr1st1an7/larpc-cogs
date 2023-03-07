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


class Partnerships(commands.Cog):
    client = commands
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Partnerships Cog is online.')

    
    @commands.slash_command()
    @commands.has_role("Partnership Management")
    async def ppending(self, inter):
        await inter.send("Your partnership request is currently <:larpcpending:1010554561435533383> **Under Review.**\n\n<:larpcinfo:1010554603609264169> **What does this mean?**\nThis means that one of our Partnership Management Team members will inspect your server to see if it matches our partnership requirements.\nPlease note that this process may take several days.")
        await inter.delete()

    @commands.slash_command()
    @commands.has_role("Partnership Management")
    async def paccepted(self, inter):
        await inter.send("Your partnership request has been reviewed and is **<:approved1:1010611038103814284> Approved**\n\n<:larpcinfo:1010554603609264169> **What does this mean?**\nYour partnership request has been reviewed and it seems like your server meets our partnership requirements.\nBefore we go to the final step, please agree to our Partnership Guidelines:\n```- You agree to keep this partnership as sign of collaboration, not just to gain members to your server without any other reason.\n\n- You agree in case you're to terminate our partnership for any reason, that you're required to contact us before doing so.\n\n- You understand that we (larpc) can terminate your partnership for any reason at any time without contacting you.```")
        await inter.message.delete()

    @commands.slash_command()
    @commands.has_role("Partnership Management")
    async def pdenied(self, inter):
        await inter.send("Your partnership request has been reviewed and is <:failed1:1010610950354784366> **Denied**\n\n<:larpcinfo:1010554603609264169> **What does this mean?**\nOur Partnership Management Team has decided to deny your partnership due to it not following our Partnership Requirements. This may be but is not limited to: your server not meeting our minimal members requirement, your server is not active, your server has bad reputation or we simply do not see that partnering with your server will benefit us.")
        await inter.message.delete()


    @commands.slash_command(description="Ping Perms role required. Pings a Partnership role in partnership channel.")
    @commands.has_role("Partnership Management")
    @commands.has_role("Ping Perms")
    async def partnerping(self, message):
            await message.channel.send(f"Hey <@&928584599800520744>! Make sure to check this server out!")
    

def setup(client):
    client.add_cog(Partnerships(client))