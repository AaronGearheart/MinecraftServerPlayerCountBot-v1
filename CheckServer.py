import requests
import time

url_Selected = False
debug = False
motd = False

while url_Selected == False:
    print("Quick Options:")
    if debug == True:
        print("1: Example 1")
    else:
        print("1: Example 1 0: Debug Mode -: Show MOTD")
    print("Please enter URL or select quick options.")
    url = input()
    if url == "":
        print("Invalid input. Please select an option or enter a URL.")
    elif url == "1":
        url = 0
        url = "https://api.mcstatus.io/v2/status/java/quick_url_1" #Add your quick URL here as you please
        url_Selected = True
    elif url == "0" and debug == False:
        debug = True
        print("Debug mode enabled")
        pass
    elif url == "-":
        motd = True
        print("Showing MOTD")
    else:
        url = "https://api.mcstatus.io/v2/status/java/" + url
        url_Selected = True

print("Please enter time before pings in seconds. Default 5 seconds")
wait_input = input()
if wait_input.strip() == "":
    wait = 5
else:
    try:
        wait = int(wait_input)
    except ValueError:
        print("Invalid input. Using default value of 5.")
        wait = 5
print(f"Time before pings is {wait} seconds")

def check_Players(url):
    try:
        global motd

        response = requests.get(url)    
        response.raise_for_status()  # Raise an exception if the request was unsuccessful (e.g., 404 or 500)
        data = response.json()  # Parse the JSON response
        # Check if 'players' and 'online' keys exist in the response\
        if debug == True:
            print(data)
        if 'players' in data and 'online' in data['players']:
            online_players = data['players']['online']
            response_message = f"Number of online players: {online_players}"
        if 'motd' in data and 'clean' in data['motd']:
            clean_motd = data['motd']['clean']
            print("Clean MOTD:", clean_motd)
        else:
            response_message = "Online player count not found in the response."
        return response_message
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except ValueError as ve:
        print(f"Error parsing JSON response: {ve}")

def main(url):
    start_time = time.time() * 1000
    response_message = check_Players(url)
    end_time = time.time() * 1000
    execution_time = end_time - start_time
    return execution_time, response_message

try:
    while True:
        print(f"Attempting to ping server")
        time_to_complete, response_message = main(url)
        if response_message is not None:
            print(f"Took {time_to_complete:.2f}ms to ping server")
            print(response_message)
        time.sleep(wait)
except KeyboardInterrupt:
    print("Stopped by user")