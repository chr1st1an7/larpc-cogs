import disnake
from disnake import message
from disnake.ext import commands
from disnake.ext.commands import command, has_permissions, bot_has_permissions
from disnake.ui import View, Button, button
from disnake import ButtonStyle, Interaction
from disnake.ext import tasks
import random

class UserCmds(commands.Cog):
    client = commands
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'UserCmds Cog is online.')

    
    # ------------------------ Commands

    @commands.slash_command()
    async def ping(self, inter):
        latency = round(self.client.latency * 1000)

        await inter.response.send_message(f'Pong! Latency: {latency}ms')

    
    @commands.slash_command(description="No permissions needed.")
    async def ad(self, inter):
        embed = disnake.Embed(title="Our Server Advertisement", description="```**:palm_tree: Los Angeles Roleplay Community**\nWelcome to Los Angeles Roleplay Community, the largest Los Angeles roleplay-based community on the ERLC, Roblox.\n\n**:police_officer_tone5: We offer probably one of the best roleplay experiences!**\nWe own every perk, professionally organized Discord server, and loads of Departments & Jobs you can work as!\n\n**Join us Today!**\nhttps://discord.gg/larpc\n\nand guess what.. we've kept your family hostage.. and if you don't join.. you know what we will do :smirk:\nhttps://youtu.be/jCI84XmCUK8```\nYou can use our server advertisement for partnerhip purposes, or to help us advertise and grow our server (<#608799037872930837>)!")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/880519966070276156/1003737327832678541/larpclogowatermarked.png")
        await inter.response.send_message(embed=embed)

    
    @commands.slash_command(description="No permissions needed.")
    async def community(self, inter):
        embed = disnake.Embed(title="How do I become a Community Member?", description="Join the [Roblox Group](https://www.roblox.com/groups/9247039/LARPC-Los-Angeles-Roleplay-Community#!/about). Once you have joined the group, type ``/getroles`` in <#925703188814901268>.")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/880519966070276156/1003737327832678541/larpclogowatermarked.png")
        await inter.response.send_message(embed=embed)


    @commands.slash_command(description="No permissions needed.")
    async def donate(self, inter):
        embed = disnake.Embed(title="How do I become a Donator?", description="Join the [Donation Hub](https://www.roblox.com/games/8739676569/LARPC-Donation-Hub). Once you have donated, your donation will appear in <#806944639734120498>. After that, open community support ticket in <#816765532295397376> to claim your role.")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/880519966070276156/1003737327832678541/larpclogowatermarked.png")
        await inter.response.send_message(embed=embed)


    @commands.slash_command(description="No permissions needed.")
    async def serverlink(self, inter):
        embed = disnake.Embed(title="How do I join a Game Server?", description="You can join our Game Server by using the link below.\nhttps://policeroleplay.community/join/larpc ")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/880519966070276156/1003737327832678541/larpclogowatermarked.png")
        await inter.response.send_message(embed=embed)


    @commands.slash_command(description="No permissions needed.")
    async def appeal(self, inter):
        embed = disnake.Embed(title="How do I appeal a ban?", description="You can appeal your punishment at our [Ban Appeals Server](https://discord.gg/DH9Pc8rGEC). However, some bans may not be appealable!")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/880519966070276156/1003737327832678541/larpclogowatermarked.png")
        await inter.response.send_message(embed=embed)


    @commands.slash_command(description="No permissions needed.")
    async def staffapp(self, inter):
        embed = disnake.Embed(title="How do I become a Staff Member?", description="You can apply to become a part of our Staff Team by filling out a form attached in <#926817251280191569>.")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/880519966070276156/1003737327832678541/larpclogowatermarked.png")
        await inter.response.send_message(embed=embed)


    @commands.slash_command(description="No permissions needed.")
    async def jurisdiction(self, inter):
        embed = disnake.Embed(title="LARPC Jurisdiction Map", description="You are to follow this Jurisdiction Map at all times while patrolling on your Department!")
        embed.set_image(url="https://media.discordapp.net/attachments/1045410156525129828/1110888395271569488/IMG_4770.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1045410156525129828/1109843966997831680/jd.png")
        await inter.response.send_message(embed=embed)


    @commands.slash_command(description="No permissions needed. Shows the server's membercount.")
    async def membercount(self, inter):
        embed = disnake.Embed(title="")
        embed = disnake.Embed(color=000000, timestamp=inter.message.created_at)
        embed.add_field(name="👥 Member Count",
                            value=f"There are currently ``{inter.guild.member_count}`` Members in this server!",
                            inline=False)
        await inter.response.send_message(embed=embed)


    @commands.slash_command(aliases=["whois"], description="No permissions needed. Shows an user info.")
    async def userinfo(self, inter, member: disnake.Member = None):
        if not member:  # if member is no mentioned
            member = inter.message.author  # set member as the author
        roles = [role for role in member.roles]
        embed = disnake.Embed(timestamp=inter.message.created_at,
                            title=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text=f"Requested by {inter.author}")

        embed.add_field(name="Display Name:", value=member.display_name, inline=False)
        embed.add_field(name="ID:", value=member.id, inline=False)

        embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        await inter.response.send_message(embed=embed)

    @commands.slash_command()
    async def test(self, inter):
        await inter.response.send_message("Just a test command! :D")

    @commands.slash_command()
    async def vote(self, inter):
        embed = disnake.Embed(title="Support our server by voting!",
                              description="Make sure to leave a review and vote for our server on Melonly.\n https://servers.melonly.xyz/los-angeles-roleplay-community")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/880519966070276156/1003737327832678541/larpclogowatermarked.png")
        await inter.response.send_message(embed=embed)

    

    @tasks.loop(seconds=20)
    async def send_message():
        staff_embed = disnake.Embed(title="We are hiring Staff Team members!", description="You can apply for our Staff Team by visiting our <#926817251280191569>.")

        embeds = [staff_embed]
        channel_id = 925700658257084456
        channel = commands.get_channel(channel_id)
        
        await channel.send(random.choice(embeds))
    
def setup(client):
    client.add_cog(UserCmds(client))

    
