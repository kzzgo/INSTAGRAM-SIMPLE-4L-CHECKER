import requests, random, time
from colorama import Fore

while True:
    user = ""

    for character in random.choices("abcdefghijklmnopqrstuvwxyz1234567890", k=4):
        user = user + character

    response = requests.get("https://instagram.com/{user}/")

    if (response.status_code == 200):
        print(Fore.RED + f"not found: {user}" + Fore.RESET)
    elif (response.status_code == 404):
        print(Fore.LIGHTGREEN_EX + f"FOUND: {user}" + Fore.RESET)
    else:
        print("BANNED")
        time.sleep(100)
