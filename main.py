import requests
import dotenv
import os
import discord
from discord.ext import commands

dotenv.load_dotenv("api.env")
dotenv.load_dotenv("token.env")
token = str(os.getenv("TOKEN"))
api_key = str(os.getenv("api_key"))

weatherbot = discord.Bot()

@weatherbot.event

async def on_ready():
    print(f"{weatherbot.user} Está ligado!")

@weatherbot.slash_command(name = "tempo", description="Veja a temperatura e o clima de uma cidade.")
async def tempo(ctx, arg):
    embedClouds = discord.Embed(title="Clima BOT")
    embedClouds.set_image(url="https://cdn.discordapp.com/attachments/1150272954005979156/1150525357624135850/clouds.png")

    embedRain = discord.Embed(title="Clima BOT")
    embedRain.set_image(url="https://cdn.discordapp.com/attachments/1150272954005979156/1150525357947109588/rain.png")

    embedClear = discord.Embed(title="Clima BOT")
    embedClear.set_image(url="https://cdn.discordapp.com/attachments/1150272954005979156/1150525357301178368/clear.png")

    embedSnow = discord.Embed(title="Clima BOT")
    embedSnow.set_image(url="https://cdn.discordapp.com/attachments/1150272954005979156/1150531121696735342/snow.png")

    embedFog = discord.Embed(title="Clima BOT")
    embedFog.set_image(url="https://cdn.discordapp.com/attachments/1150272954005979156/1150556790543622144/fog.png")

    embedTornado = discord.Embed(title="Clima BOT")
    embedTornado.set_image(url="https://cdn.discordapp.com/attachments/1150272954005979156/1150551811741188186/tornado.png")

    dicionario = {
        "Clear": "Limpo",
        "Rain": "Chuvoso",
        "Clouds": "Nuvens",
        "Snow" : "Neve",
        "Drizzle" : "Garoando",
        "Thunderstorm" : "Tempestade",
        "Mist" : "Névoa",
        "Smoke" : "Nevoeiro",
        "Haze"  : "Névoa",
        "Dust" : "Poeira",
        "Sand" : "Poeira",
        "Ash" : "Queimadas",
        "Squall" : "Pequena Tempestade",
        "Tornado" : "Tornado"
    }

    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={arg}&units=imperial&APPID={api_key}&lang=pt_br")

    if weather_data.json()['cod'] == '404': 
        await ctx.respond(f"Nenhuma cidade com esse nome encontrada. Tente novamente com outro nome")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        celsius = ((temp - 32) / 1.8)
    
    if weather == "Clouds":
        await ctx.respond(f"O clima em **{arg}** é: **{dicionario[weather]}** \nA temperatura em **{arg}** é de: **{round(celsius, 1)}°C**", embed = embedClouds)
    elif weather == "Clear":
        await ctx.respond(f"O clima em **{arg}** é: **{dicionario[weather]}** \nA temperatura em **{arg}** é de: **{round(celsius, 1)}°C**", embed = embedClear)
    elif weather == "Rain" or weather == "Drizzle" or weather == "Thunderstorm" or weather == "Squall":
        await ctx.respond(f"O clima em **{arg}** é: **{dicionario[weather]}** \nA temperatura em **{arg}** é de: **{round(celsius, 1)}°C**", embed = embedRain)
    elif weather == "Snow":
        await ctx.respond(f"O clima em **{arg}** é: **{dicionario[weather]}** \nA temperatura em **{arg}** é de: **{round(celsius, 1)}°C**", embed = embedSnow)
    elif weather == "Tornado":
        await ctx.respond(f"O clima em **{arg}** é: **{dicionario[weather]}** \nA temperatura em **{arg}** é de: **{round(celsius, 1)}°C**", embed = embedTornado)
    else:
        await ctx.respond(f"O clima em **{arg}** é: **{dicionario[weather]}** \nA temperatura em **{arg}** é de: **{round(celsius, 1)}°C**", embed = embedFog)

weatherbot.run(token)