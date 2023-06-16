import time
import requests
import colorama
import json
from colorama import Fore, Back, Style
print("Welcome to " + Fore.RED + "Gitfoga" + Fore.RESET + "!")

while True:
    repo = input("Please put your desired repository with its full name e.g. (octocat/Spoon-Knife) >>> ")
    if repo == "": repo = "Special-Rocket-Agents/KawaiiXOR"
    reqout = requests.get("https://api.github.com/repos/" + repo)
    j = json.loads(reqout.text)
    # ----------------------------------------------------------------------
    print(f"Repository Name: {Fore.RED}{j['name']}{Fore.RESET}")
    if j["description"] != None: print(Fore.LIGHTYELLOW_EX + j["description"] + Fore.RESET)
    if j["archived"] == True: print(f"{Back.YELLOW}ARCHIVED!{Back.RESET}")
    if j["owner"]["type"] == "User": print(f"By a {Fore.LIGHTMAGENTA_EX}user{Fore.RESET}: " + Fore.LIGHTGREEN_EX + j["owner"]["login"] + Fore.RESET)
    else: print(f"By an {Fore.LIGHTRED_EX}organization{Fore.RESET} named " + Fore.GREEN + j["owner"]["login"] + Fore.RESET)
    print("Visit on Github: " + Fore.LIGHTBLUE_EX + j["html_url"] + Fore.RESET)
    if j["license"] != None: print("License: " + Fore.CYAN + j["license"]["spdx_id"] + Fore.RESET)
    if j["allow_forking"] == True: print(f"Has been forked {Fore.GREEN}{j['forks_count']}{Fore.RESET} times.")
    print(Fore.LIGHTGREEN_EX + str(j["watchers"]) + Fore.RESET + " people have been watching this repository")
    if j["has_issues"] == True: print(Fore.RED + str(j["open_issues"]) + Fore.RESET + " issues are open")
    print("Created at: " + Fore.MAGENTA + str(j["created_at"]) + Fore.RESET)