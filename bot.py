import random
from decouple import config
import nextcord
import json
from nextcord.ext import commands
CLIENTTOKEN = config('CLIENTTOKEN')
client = commands.Bot(command_prefix=">")
client.remove_command('help')
#
@client.event
async def on_ready():
    print(f'Bot is ready. Logged in as {client.user}(ID: {client.user.id}) ')
    await client.change_presence(activity = nextcord.Activity(type = nextcord.ActivityType.watching, name = ">help"))
#
@client.command()
async def eggotyou(ctx):
    await ctx.send('Fine. You got me... screenshot this and send it to me on my discord to have your name put in the source code!', delete_after=5)
@client.command()
async def project(ctx):
    await ctx.send('```https://github.com/Wamy-Dev/Enantion```')
@client.command()
async def donate(ctx):
    await ctx.send('```https://homeonacloud.com/pages/donate.html```')
@client.command()
async def ping(ctx):
    await ctx.send(f'```I`m not too slow... right? {round(client.latency * 1000)}ms```')
@client.command()
async def leaderboard(ctx):
    with open ("./resources/wins.json", "r") as wins:
        windata = json.load(wins)
    try:
        top_users = {k: v for k, v in sorted(windata.items(), key=lambda item: item[1], reverse=True)}
        names = ""
        for position, user in enumerate(top_users):
            if position > 9:
                break
            else:
                names += f'{position+1} - <@!{user}> with {top_users[user]} wins.\n'
        embed = nextcord.Embed(title="Global Leaderboard", color= nextcord.Color.from_rgb(160,131,196))
        embed.add_field(name="Top 10 users by win count:", value=names, inline=False)
        embed.set_footer(text=f'Includes users from other servers.')
        await ctx.send(embed = embed)
    except:
        embed = nextcord.Embed(title="Global Leaderboard", color= nextcord.Color.from_rgb(255,0,0))
        embed.add_field(name="Something went wrong...", value='No data present for leaderboard. Either something is wrong and you should make an issue on github by using >project, or not enough people have won yet; get playing!\n\n\n-With love, <@!219545357388873728>')
        await ctx.send(embed=embed)
    wins.close()
@client.command()
async def counts(ctx):
    with open("./resources/counts.json", "r") as count:
        previouscount = json.load(count)
    rpscount = previouscount["rpscount"]
    coinflipcount = previouscount["coinflipcount"]
    dicecount = previouscount["dicecount"]
    totalcount = int(rpscount) + int(coinflipcount) + int(dicecount)
    embed = nextcord.Embed(title = "Global Counts", color= nextcord.Color.from_rgb(160,131,196))
    embed.add_field(name = 'Rock, Paper, Scissors', value=f'Played {rpscount} times.', inline = False)
    embed.add_field(name = 'Coinflip', value=f'Played {coinflipcount} times.', inline = False)
    embed.add_field(name = 'The Dice Game', value=f'Played {dicecount} times.', inline = False)
    embed.set_footer(text=f'Includes data from other servers. Total: {totalcount}.')
    await ctx.send(embed = embed)
    count.close()
@client.command(pass_context = True, aliases = ['Help', "h"])
async def help(ctx):
    embed = nextcord.Embed(title = "Here is a command list:", color= nextcord.Color.from_rgb(160,131,196))
    embed.set_author(name = ctx.message.author, icon_url = ctx.author.avatar.url)
    embed.add_field(name = '>ping', value='Shows the ping between the bot and the user.', inline = False)
    embed.add_field(name = '>project', value='View the project github.', inline = False)
    embed.add_field(name = '>donate', value='Donate to the project.', inline = False)
    embed.add_field(name = '>counts', value='See how many times all games have been played globally.', inline = False)
    embed.add_field(name = '>leaderboard', value='See the top winners globally.', inline = False)
    await ctx.send(embed = embed)
#

client.run(CLIENTTOKEN)