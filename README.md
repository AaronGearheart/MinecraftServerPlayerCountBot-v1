# MinecraftServerPlayerCountBot-v1
A simple discord bot and independent client script to ping any Java Minecraft Server and return player count.
<br>
**For the bot:**
<br>
***I won't go over how to set up a discord bot because I assume you know how if you are coming to his page.***
<br>
Set up a Discord bot through the Discord Developer Portal.
<br>
Install the following packages through pip install: Discord, Requests
<br>
Get your bot token and paste it into the TOKEN variable in the CheckServerDiscordBot-v1.py file
<br>
Change the URL variable (ln 57) to https://api.mcstatus.io/v2/status/java/YOUR_SERVER_IP replacing YOUR_SERVER_IP with your server IP
<br>
Change rich presence (ln 21) to whatever you want
<br>
Run the bot and add it to your server again through the Developer Portal
<br>
Type !mcstatus into your server and enjoy
<br>
**For the client side script**
<br>
Install the following packages through pip install: Discord, Requests
<br>
Run the script and enjoy
