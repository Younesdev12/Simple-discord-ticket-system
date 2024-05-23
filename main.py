import discord
import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="*", intents=intents)

@client.event
async def on_ready():
    print("Bot Running!")
    await client.tree.sync()
    print("Tree commands synced!") 
@client.tree.command(name="ticket", description="Create a ticket")
async def ticket(ctx):
    create = discord.ui.Button(style=discord.ButtonStyle.green, label="Create Ticket 📩")
    close = discord.ui.Button(style=discord.ButtonStyle.danger, label="Close ticket 🔒")

    #functions
    async def create_ticket(ctx):
        guild = ctx.guild
        perms = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            ctx.user: discord.PermissionOverwrite(view_channel=True)
            }
        channel = await guild.create_text_channel(f"{ctx.user}'s ticket", overwrites=perms)
        await ctx.response.send_message(f"Ticket created! <#{channel.id}>", ephemeral=True)
        await channel.send(f"{ctx.user.mention}", embed=embed2, view=view2)
    async def close_ticket(ctx):
        await ctx.channel.delete()

    #embeds
    embed = discord.Embed(
        title="Create Ticket",
        description="Click on the button bellow to create a ticket",
        color=discord.Color.from_rgb(255,255,255)
    )
    embed.set_footer(text="Ticket System By Younesdev0")
    embed2 = discord.Embed(
        title="An admin will be with you shortly!",
        description="If you wish to close the ticket click on the button bellow",
        color=discord.Color.from_rgb(255,255,255)
    )
    embed2.set_footer(text="Ticket System By Younesdev0")

    #buttons    
    close.callback = close_ticket    
    create.callback = create_ticket    
    view = discord.ui.View()
    view.add_item(create)
    view2 = discord.ui.View()
    view2.add_item(close)
   
    await ctx.channel.send(embed=embed, view=view)
client.run("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")