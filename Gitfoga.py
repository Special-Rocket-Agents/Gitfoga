import time
import requests
import colorama
import json
import os
from colorama import Fore, Back, Style
IXE = None
repo_name = os.getenv('REPO_NAME')
print("Welcome to " + Fore.RED + "Gitfoga" + Fore.RESET + "!")
print("Proud work of Arezalgamer89")

while True:
    if repo_name == None:
        repo = input("Please put your desired repository with its full name e.g. (octocat/Spoon-Knife) >>> ")
    else:
        repo = "octocat/Spoon-Knife"
    if repo == "": repo = "octocat/Spoon-Knife"
    reqout = requests.get("https://api.github.com/repos/" + repo)
    j = json.loads(reqout.text)
    # ----------------------------------------------------------------------
    print("-----------------------------------------------------------------")
    try:
        print(f"Repository Name: {Fore.RED}{j['name']}{Fore.RESET}")
        if j["description"] != None: print(Fore.LIGHTYELLOW_EX + j["description"] + Fore.RESET)
        if j["archived"] == True: print(f"{Back.YELLOW}ARCHIVED!{Back.RESET}")
        if j["owner"]["type"] == "User": print(f"By a {Fore.LIGHTMAGENTA_EX}user{Fore.RESET}: " + Fore.LIGHTGREEN_EX + j["owner"]["login"] + Fore.RESET)
        else: print(f"By an {Fore.LIGHTRED_EX}organization{Fore.RESET} named " + Fore.GREEN + j["owner"]["login"] + Fore.RESET)
        print("Visit on Github: " + Fore.LIGHTBLUE_EX + j["html_url"] + Fore.RESET)
        if j["license"] != None: print("License: " + Fore.CYAN + j["license"]["spdx_id"] + Fore.RESET)
        if j["forks"] >= 1: print(f"Has been forked {Fore.GREEN}{j['forks_count']}{Fore.RESET} times.")
        if j["watchers"] != 0: print(Fore.LIGHTGREEN_EX + str(j["watchers"]) + Fore.RESET + " people have been watching this repository")
        if j["has_issues"] == True: print(Fore.RED + str(j["open_issues"]) + Fore.RESET + " issues are open")
        print("Created at: " + Fore.MAGENTA + str(j["created_at"]) + Fore.RESET)
        ####### Let user know about the reason 0 forks or 0 Issues do not appear #####################################################
        if j["forks"] == 0 or j["allow_forking"] == False or j["watchers"] == 0 or j["has_issues"] != True or j["license"] == None:
            print(Fore.CYAN + "[Note that some attributes are dynamic and will appear if they are above or equal to 1]" + Fore.RESET)
        ##############################################################################################################################
    except KeyError:
        print(Fore.RED + "Nonexistant Name, GitHub API down or something went wrong!" + Fore.RESET)
    except requests.exceptions.ProxyError:
        print(Fore.RED + "Something is wrong with Internet. Please try again" + Fore.RESET)
    print("-----------------------------------------------------------------")