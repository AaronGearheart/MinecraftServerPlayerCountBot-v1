# MinecraftServerPlayerCountBot-v1
A simple discord bot and independent client script to ping any Java Minecraft Server and return player count.
**For the bot:**
***I won't go over how to set up a discord bot because I assume you know how if you are coming to his page.***
1. Set up a Discord bot through the Discord Developer Portal.
2. Install the following packages through pip install: Discord, Requests
3. Get your bot token and paste it into the TOKEN variable in the CheckServerDiscordBot-v1.py file
4. Change the URL variable (ln 57) to https://api.mcstatus.io/v2/status/java/YOUR_SERVER_IP replacing YOUR_SERVER_IP with your server IP
5. Change rich presence (ln 21) to whatever you want
6. Run the bot and add it to your server again through the Developer Portal
7. Type !mcstatus into your server and enjoy
**For the client side script**
1. Install the following packages through pip install: Discord, Requests
2. Run the script and enjoy
