#Import discord permissions
import discord
from discord.ext import commands

#Import .env information
import os
from dotenv import load_dotenv

load_dotenv()

#Load Bot token
TOKEN = os.getenv("DISCORD_TOKEN")

#Load Bot APP ID
BOT_APP_ID = int(os.getenv("BOT_APP_ID"))

#Load user IDs
Zane_id = int(os.getenv("USER_ID_ZANE"))
Nostramo_id = int(os.getenv("USER_ID_NOSTRAMO"))

#Set up bot intents
intents = discord.Intents.default()
intents.message_content = True

#Initialise bot
zbot = commands.Bot(command_prefix='!', intents=intents)

@zbot.event
async def on_ready():
	await zbot.tree.sync()
	print(f'logged in as {zbot.user} (ID: {zbot.user.id}, App ID: {BOT_APP_ID})')

#Slash command: /smite
@zbot.tree.command(name="smite", description="Smite Zane with a gif")
async def smite(interaction: discord.Interaction):
	# Step 1: Fetch User by ID
	user = await zbot.fetch_user(Zane_id)
	
	# Step 2: Creates embed mentioning user
	embed = discord.Embed(description=f"{user.mention} gets smited!")
	
	# Step 3: Set embed image to chosen GIF URL
	gif_url = "https://media.tenor.com/_FtFfrSaJcwAAAAC/shut-up.gif"
	embed.set_image(url=gif_url)
	
	# Step 4: Respond to interaction with embed
	await interaction.response.send_message(embed=embed)

zbot.run(TOKEN)
