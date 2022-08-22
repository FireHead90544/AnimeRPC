from api.api import GogoAnimeClient
from pypresence import Presence
from InquirerPy.base.control import Choice
from InquirerPy import prompt
from colorama import Fore, init
import time
import os

init(autoreset=True)

CLIENT_ID = "1011298188591894618" # Only change if you know what you're doing.
presence = Presence(CLIENT_ID)
client = GogoAnimeClient()

presence.connect()
presence.update(state="Selecting Anime", large_image="logo", large_text="Anime RPC", start=time.time())

stylesheet = {"questionmark": "#16C60C bold", "answermark": "#e0af68", "answer": "#E5E512", "input": "#98c379", "question": "#E74856 bold", "answered_question": "", "instruction": "#a9b1d6", "long_instruction": "#a9b1d6", "pointer": "#3A96DD", "checkbox": "#9ece6a", "separator": "", "skipped": "#48444c", "validator": "", "marker": "#9ece6a", "fuzzy_prompt": "#bb9af7", "fuzzy_info": "#a9b1d6", "fuzzy_border": "#343740", "fuzzy_match": "#bb9af7", "spinner_pattern": "#9ece6a", "spinner_text": ""}

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
def header() -> None:
    """The secant-c header of the application."""
    clear()
    print(f"""
    {Fore.RED}░█████╗░███╗░░██╗██╗███╗░░░███╗███████╗░░░░{Fore.BLUE}██████╗░██████╗░░█████╗░
    {Fore.RED}██╔══██╗████╗░██║██║████╗░████║██╔════╝░░░░{Fore.BLUE}██╔══██╗██╔══██╗██╔══██╗
    {Fore.WHITE}███████║██╔██╗██║██║██╔████╔██║█████╗░░░░░░{Fore.YELLOW}██████╔╝██████╔╝██║░░╚═╝
    {Fore.WHITE}██╔══██║██║╚████║██║██║╚██╔╝██║██╔══╝░░░░░░{Fore.YELLOW}██╔══██╗██╔═══╝░██║░░██╗
    {Fore.GREEN}██║░░██║██║░╚███║██║██║░╚═╝░██║███████╗░░░░{Fore.BLUE}██║░░██║██║░░░░░╚█████╔╝
    {Fore.GREEN}╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░░░░╚═╝╚══════╝░░░░{Fore.BLUE}╚═╝░░╚═╝╚═╝░░░░░░╚════╝░
    
          {Fore.WHITE}A Discord Rich Presence Client for Showing Anime Info
    """)

def get_presence_data() -> list:
    """Ask our not-so-pathetic user to select the anime to update rpc of."""
    questions = [
        {
            "type": "input",
            "message": "Enter the name of Anime to search for:",
            "name": "anime_name",
            "validate": lambda result: len(result) > 0,
            "invalid_message": "Input cannot be empty."
        }
    ]
    result = prompt(questions=questions, style=stylesheet)
    results = client.search(result['anime_name'])
    header()

    if len(results) == 0:
        print(f"\n>>> {Fore.RED}No results found. {Fore.WHITE}Please try again with another query.")
        time.sleep(3)
        get_presence_data()
    else:
        questions = [
            {
                "type": "list",
                "name": "anime_index",
                "message": "Select the anime:",
                "choices": [Choice(indx, name=f"{r['title']} [Released: {r['released']}]") for indx, r in enumerate(results)]
            }
        ]
        result = prompt(questions=questions, style=stylesheet)

        return results[result['anime_index']]

def update_presence() -> None:
    """Update the presence using the data our not-so-pathetic user selected."""
    presence_data = get_presence_data()
    presence.update(
        state=presence_data['title'],
        details=f"Watching Anime | Released {presence_data['released']}",
        large_image=presence_data['image_url'],
        large_text=presence_data['title'],
        start=time.time(),
        buttons=[{"label": "Watch Anime", "url": presence_data['url']}, {"label": "Anime RPC", "url": "https://github.com/FireHead90544/AnimeRPC"}]
    )
    print(f"{Fore.GREEN} >>> Updated Rich Presence | Leave This Window Open in Background :)")

header()
while True:
    print("\n")
    data = prompt({"type": "list", "name": "dat", "message": "What do you want to do?", "choices": ["Update RPC", "Stop & Close"]}, style=stylesheet)
    if data['dat'] == "Update RPC":
        update_presence()
    else:
        try:
            presence.close()
        except Exception:
            pass
        print(f"{Fore.GREEN} >>> Closed Rich Presence :)")
        time.sleep(1)
        break
exit()