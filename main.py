import discord
import requests
from discord.ext import commands
import json
import config

token = config.token
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
client = discord.Client(intents=intents)

class MyView(discord.ui.View):
    @discord.ui.select(
        placeholder = "Are you bored?\nChoose the type of activity!", 
        min_values = 1, 
        max_values = 1, 
        options = [ 
            discord.SelectOption(
                label="education"
            ),
            discord.SelectOption(
                label="recreational"
            ),
            discord.SelectOption(
                label="social"
            ),
            discord.SelectOption(
                label="diy"
            ),
            discord.SelectOption(
                label="charity"
            ),
            discord.SelectOption(
                label="cooking"
            ),
            discord.SelectOption(
                label="relaxation"
            ),
            discord.SelectOption(
                label="music"
            ),
            discord.SelectOption(
                label="busywork"
            )

        ]
    )
    async def select_callback(self, select, interaction):
        txt = requests.get(f'http://www.boredapi.com/api/activity?type={select.values[0]}').text
        res = json.loads(txt)['activity']
        await interaction.response.send_message(res)

@bot.command()
async def bored(ctx):
    await ctx.send("Are you bored?🥱\nChoose the type of activity!", view=MyView())


bot.run(token)
