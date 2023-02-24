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


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Events Cog is online.')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.name == 'Los Angeles Roleplay Community':
            channel = commands.get_channel(925700658257084456)
            await channel.send(f'{member.mention} just joined **{member.guild.name}**! They are our ``{member.guild.member_count}th`` member, please give them a warm welcome! 😄')
            role = disnake.utils.get(member.guild.roles, name="Member")
            await member.add_roles(role)
            embed = disnake.Embed(title=f'Welcome to Los Angeles Roleplay Community! :smile:',
                                description=f'Welcome to **Los Angeles Roleplay Community**, the largest Los Angeles roleplay-based community on the ERLC, Roblox.')
            embed.add_field(name="ㅤ",
                            value="Here are some important links you may find useful;\nㅤ\n** Our Official Roblox Group** *(Use ``/getroles`` to claim awesome perks after joining!)*\nhttps://www.roblox.com/groups/9247039/\n**Discord Vanity Invite** *(Share this server with your friends, by using our vanity link!)*\nhttps://discord.gg/larpc\n**Ban Appeals Server** *(In case you ever get banned, you may be able to appeal!)*\nhttps://discord.gg/DH9Pc8rGEC\nㅤ\n📖 Make sure to read our <#926816507630084137> and <#926816531789279232>!\n:blue_book: To apply for Staff Team, check <#926817251280191569>!\nㅤ\n:police_officer_tone5: **Do you want to apply for a special department/job?**\nYou can apply by checking out our <#876785568510541845> and <#958007897084801094> channels!\nㅤ\n**We hope you enjoy your stay at our Community!**\nIf you have any questions, feel free to ask one of our Staff Members, and they will be more than happy to answer you as soon as possible!\nㅤ\nSigned,\n**Los Angeles Roleplay Community**,\nManagement Team.",
                            inline=False)
            embed.set_footer(text="Thank you for choosing Los Angeles Roleplay Community!", icon_url="https://media.discordapp.net/attachments/880519966070276156/1003737327832678541/larpclogowatermarked.png")
            await member.send(embed=embed)
            
    
    

    

    # @commands.Cog.listener()
    # async def on_message(self, message: Message) -> None:
    #     from disnake.ext.commands import CooldownMapping, BucketType
    #     from disnake import Message
    #     message_cooldown = CooldownMapping.from_cooldown(10.0, 600.0, BucketType.user)
    #     if message.author.bot:
    #         return

    #     if any([message.content.startswith(check) for check in ["!ban", "!mute", "!kick", "!softban", ".gban", ".gkick"]]) and message.mentions:
    #         bucket = message_cooldown.get_bucket(message)
    #         retry_after = bucket.update_rate_limit()

    #         if retry_after:
    #             if message.author.top_role.position < message.guild.self_role.position:
    #                 dt = datetime.datetime.now().astimezone() + datetime.timedelta(days=1)
    #                 await message.author.timeout(duration=datetime.timedelta(minutes=15),
    #                                             reason="Spamming moderation commands.")
    #                 await message.channel.send(
    #                     f"<:redwarn:972186324020908112> Muted {message.author.mention} for `spamming moderation commands`" +
    #                     f" until <t:{int(dt.timestamp())}:F> (<@&956999230730412115>)"
    #                 )
    #             else:
    #                 print(
    #                     f"<:redwarn:972186324020908112> {message.author}, is moderation commands but",
    #                     "cannot be muted since the user either has a higher or equal role to me. (<@&956999230730412115>)"
    #                 )

    #     await commands.process_commands(message)
        



def setup(client):
    client.add_cog(Events(client))