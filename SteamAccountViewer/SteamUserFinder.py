from steam.webapi import WebAPI
from PIL import Image
import requests
import io
from tkinter import *

api = WebAPI(key="F3CDC4179CA1D2ECC6BE296BE4B53038")


steam_id = input('Enter a steam id: ')
while True:
    try:
        player_summary = (api.call('ISteamUser.GetPlayerSummaries', steamids=steam_id))
        break
    except:
        steam_id = input("Enter a valid steam id: ")


persona_name = player_summary["response"]["players"][0]["personaname"]
profile_picture_url = player_summary["response"]["players"][0]["avatarfull"]


response = requests.get(profile_picture_url)
img = io.BytesIO(response.content)
im = Image.open(img)
