import discord
from discord.ext import commands, tasks
import requests

TOKEN = 'YOUR_TOKEN'


intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True

user_on = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    check_minecraft_status.start()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="gearheartstudios.com"))

@tasks.loop(seconds=5)  # Check every 5 seconds
async def check_minecraft_status():
    global user_on
    target_user_name = "Example Name"
    target_game_name = "Example Game"
    
    print("Checking for user")
    
    for guild in bot.guilds:
        # Check if the user is in the guild
        user_found = False
        for member in guild.members:
            print(member.name)
            if member.name == target_user_name:
                user_found = True
                for activity in member.activities:
                    if isinstance(activity, discord.Activity) and activity.name == target_game_name:
                        if not user_on:
                            print(user_on)
                            channel = discord.utils.get(guild.text_channels, name="general")  # Replace "general" with the desired channel name
                            if channel and user_on == False:
                                await channel.send(f"@everyone Example Name is playing Example Game.")
                                user_on = True
                        break  # Exit the loop as soon as we find a matching activity
                else:
                    # This part will execute if no matching activity is found for the user
                    user_on = False
        
        # If the user is not found in the guild, reset user_on
        if not user_found:
            user_on = False

@bot.command()
async def mcstatus(ctx):
    url = "https://api.mcstatus.io/v2/status/java/YOUR_SERVER_IP" #Add your server IP here
    
    try:
        response = requests.get(url)    
        response.raise_for_status()  # Raise an exception if the request was unsuccessful (e.g., 404 or 500)

        data = response.json()  # Parse the JSON response

        await ctx.send(f"Attempting to ping")

        

        # Check if 'players' and 'online' keys exist in the response
        if 'players' in data and 'online' in data['players']:
            online_players = data['players']['online']
            response_message = f"Number of online players: {online_players}"
        else:
            response_message = "Online player count not found in the response."

        await ctx.send(response_message)

    except requests.exceptions.RequestException as e:
        await ctx.send(f"An error occurred: {e}")
    except ValueError as ve:
        await ctx.send(f"Error parsing JSON response: {ve}")

bot.run(TOKEN)
