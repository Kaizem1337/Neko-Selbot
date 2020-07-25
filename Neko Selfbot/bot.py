
import discord, random, datetime, io, json, logging, requests, re, time, os ,ctypes, sys
import subprocess, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string
import webbrowser, aiohttp, asyncio, functools, logging
from colorama import init, Fore
from discord.ext import commands
import COVID19Py
import time
import random
import subprocess
import pymongo
from pymongo import MongoClient
import asyncio
import uuid
init(convert=True)

def CheckUUID():
    conn = MongoClient("mongodb+srv://ilikechildporn:pleasesenpai@cluster0-adkcw.mongodb.net/test?retryWrites=true&w=majority")
    database = conn["Neko"]
    collection = database["HWID LIST"]
    
    results = collection.find({"HWID":subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()})
    resultList = []

    for result in results:
        resultList.append(result)

    if len(resultList) != 0:
        print("HWID Found, Thanks For Choosing Neko")
        time.sleep(3)
        clear()
        print("Authenticating.")
        time.sleep(1)
        clear()
        print("Authenticating..")
        time.sleep(1)
        clear()
        print("Authenticating...")
        clear()
        return
    else:
        print("HWID Not Found. HWID: {}".format(subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()))
        inp = input("")
        exit()

start_time = datetime.datetime.utcnow()


def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'


def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))



covid19 = COVID19Py.COVID19()

ctypes.windll.kernel32.SetConsoleTitleW("Neko Selfbot | https://discord.gg/4bb2jAB")



clear =  lambda : os.system("cls")

CheckUUID()

print(f"[{Fore.RED}Import Discord Token{Fore.RESET}]")
token = input(" > ")

print(f"[{Fore.RED}Preferred Prefix{Fore.RESET}]")
prefix = input(" > ")
clear()

client = discord.Client()
client = commands.Bot(command_prefix=prefix, self_bot=True,
                      fetch_offline_members=False)

client.remove_command('help')


print(f'''{Fore.RESET}
                     
                                {Fore.GREEN} ██╗  ██╗██╗████████╗███████╗██╗   ██╗███╗   ██╗███████╗
                                {Fore.RED} ██║ ██╔╝██║╚══██╔══╝██╔════╝██║   ██║████╗  ██║██╔════╝
                                {Fore.GREEN} █████╔╝ ██║   ██║   ███████╗██║   ██║██╔██╗ ██║█████╗  
                                {Fore.RED} ██╔═██╗ ██║   ██║   ╚════██║██║   ██║██║╚██╗██║██╔══╝  
                                {Fore.GREEN} ██║  ██╗██║   ██║   ███████║╚██████╔╝██║ ╚████║███████╗
                                {Fore.RED} ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                       
                        
                                            {Fore.CYAN}Neko 1.0v | {Fore.GREEN}Logged In Successfully {Fore.GREEN}  
                                            {Fore.CYAN}Nitro Sniper | {Fore.GREEN}Active {Fore.GREEN}
                                            {Fore.CYAN}Prefix: {Fore.GREEN}{prefix}
                                            {Fore.CYAN}{prefix}help  |  Lists Commands {Fore.GREEN}
    '''+Fore.RESET)



data = {"channel_id": None, "payment_source_id": None}
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36", 'Authorization': token}

def getShibe(amount:int):

    shibes = requests.get(f"http://shibe.online/api/shibes?count={amount}&urls=true&htetpsUrls=true").text

    return shibes

@client.event
async def on_connect():
    ctypes.windll.kernel32.SetConsoleTitleW(f"Neko Selfbot | https://discord.gg/4bb2jAB | Logged in as {str(client.user)}")


@client.event
async def on_message(ctx: commands.Context):
    gift = re.search("discord.gift\/[a-zA-Z0-9]+|discordapp.com\/gifts\/[a-zA-Z0-9]+", ctx.content)

    if gift:

        start_time = datetime.datetime.now()

        code = gift.group().split("/")[1]

        _data = requests.post('https://discordapp.com/api/v6/entitlements/gift-codes/' + code + '/redeem', json=data, headers= headers).json()

        print(f'''
{Fore.CYAN} [Gift Redeemer]
    {Fore.MAGENTA}MESSAGE:  {Fore.LIGHTRED_EX}{_data['message']}
    {Fore.MAGENTA}CHANNEL:  {Fore.LIGHTBLACK_EX}[{ctx.channel}]
    {Fore.MAGENTA}ELAPSED:  {Fore.RESET}[ .{(datetime.datetime.now() - start_time)} ms]''') 


    await client.process_commands(ctx)

@client.command()
async def help(ctx):
    await ctx.message.delete()
    print(f'''
{Fore.BLUE}shrug {Fore.LIGHTBLACK_EX}- Express yourself!     
{Fore.BLUE}owo {Fore.LIGHTBLACK_EX}- 0w0  
{Fore.BLUE}embed {Fore.LIGHTBLACK_EX}- Sends the message you put in an embed
{Fore.BLUE}game {Fore.LIGHTBLACK_EX}- Sets your status to either streaming or normal
{Fore.BLUE}tableflip {Fore.LIGHTBLACK_EX}- Flips Table
{Fore.BLUE}unflip {Fore.LIGHTBLACK_EX}- Unflips table
{Fore.BLUE}massspoiler {Fore.LIGHTBLACK_EX}- Sends a huge spoiler
{Fore.BLUE}suggestion {Fore.LIGHTBLACK_EX}- Leave a suggestion for the selfbot
{Fore.BLUE}pfp {Fore.LIGHTBLACK_EX}- Responds with the profile picture of a user
{Fore.BLUE}guildicon {Fore.LIGHTBLACK_EX}- Responds with the server icon
{Fore.BLUE}destory {Fore.LIGHTBLACK_EX}- Self desctructs the selfbot.
{Fore.BLUE}purgeall {Fore.LIGHTBLACK_EX}- Purges all your messages
{Fore.BLUE}purge {Fore.LIGHTBLACK_EX}- Purges your an amount of your messages
{Fore.BLUE}shibe {Fore.LIGHTBLACK_EX}- Returns a shibe (example: !shibe 1 (prints 1 shibe))
{Fore.BLUE}corona {Fore.LIGHTBLACK_EX}- Corona Virus Statistics
{Fore.BLUE}ping {Fore.LIGHTBLACK_EX}- displays your ping
{Fore.BLUE}chatwipe {Fore.LIGHTBLACK_EX}- nukes the chat
{Fore.BLUE}geoip {Fore.LIGHTBLACK_EX}- displays information on a given ip
{Fore.BLUE}roleinfo {Fore.LIGHTBLACK_EX}- displays information on a role
{Fore.BLUE}whois {Fore.LIGHTBLACK_EX}- displays information on a mentioned user(only for servers)
{Fore.BLUE}pingwebsite {Fore.LIGHTBLACK_EX}- tells you if a website is online or not
{Fore.BLUE}dick {Fore.LIGHTBLACK_EX}- shows you how big someones dick is
{Fore.BLUE}_1337_speak {Fore.LIGHTBLACK_EX}- puts your text in 1337 talk!
{Fore.BLUE}servercopy {Fore.LIGHTBLACK_EX}- copies an entire server! (very fast)
{Fore.BLUE}serverdestroy {Fore.LIGHTBLACK_EX}- destroys an entire server and makes 250 channels
{Fore.BLUE}massban {Fore.LIGHTBLACK_EX}- bans everyone!
{Fore.BLUE}massunban {Fore.LIGHTBLACK_EX}- unbans everyone!
{Fore.BLUE}masschannel {Fore.LIGHTBLACK_EX}- makes loads of channels!
{Fore.BLUE}delchannels {Fore.LIGHTBLACK_EX}- deletes loads of channels!
{Fore.BLUE}spam {Fore.LIGHTBLACK_EX}- spams loads of a given message.
{Fore.BLUE}friendbackup {Fore.LIGHTBLACK_EX}- Saves all your friends!
{Fore.BLUE}abc {Fore.LIGHTBLACK_EX}- sends the alphabet!
{Fore.BLUE}btc {Fore.LIGHTBLACK_EX}- displays the current bitcoin price
{Fore.BLUE}anal {Fore.LIGHTBLACK_EX}- NSFW
{Fore.BLUE}hentai {Fore.LIGHTBLACK_EX}- NSFW
{Fore.BLUE}uptime {Fore.LIGHTBLACK_EX}- shows the uptime of the bot
{Fore.BLUE}group-leaver {Fore.LIGHTBLACK_EX}- leaves all groups
{Fore.BLUE}read {Fore.LIGHTBLACK_EX}- reads all your server(very satisfying)
{Fore.BLUE}lenny {Fore.LIGHTBLACK_EX}- emote!
{Fore.BLUE}bold {Fore.LIGHTBLACK_EX}- sends your message in bold
{Fore.BLUE}secret {Fore.LIGHTBLACK_EX}- sends your message as a spoiler
{Fore.BLUE}nitro {Fore.LIGHTBLACK_EX}- generates random nitro
''')



@client.command()
async def shrug(ctx):
    await ctx.message.delete()
    await ctx.send("¯\_(ツ)_/¯")


@client.command()
async def owo(ctx):
    await ctx.message.delete()
    await ctx.send("0w0")


@client.command()
async def embed(ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(color=0xFF1700, description=f">>> **{str(message)}**")
    await ctx.send(embed=embed)

@client.command()
async def pfp(ctx, *, member: discord.Member = None):

    member = member or ctx.author
    embed = discord.Embed()
    embed.set_image(url=member.avatar_url)

    await ctx.send(embed=embed)


@client.command()
async def game(ctx, *, message):

    status = message.split(" ")[0]

    if status == "streaming":
        await client.change_presence(activity=discord.Streaming(name=message[10:len(message)], url="https://twitch.tv/twitch"))
    elif status == "normal":
        await client.change_presence(activity=discord.Game(name=message[7:len(message)]))


@client.command()
async def tableflip(ctx):
    await ctx.message.delete()
    await ctx.send("(╯°□°）╯︵ ┻━┻")


@client.command()
async def unflip(ctx):
    await ctx.message.delete()
    await ctx.send("┬─┬ ノ( ゜-゜ノ)")


@client.command()
async def massspoiler(ctx):
    await ctx.message.delete()
    await ctx.send('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
''')
    await ctx.send('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    ''')
    await ctx.send('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    ''')

@client.command()
async def suggestion(ctx):
    await ctx.message.delete()
    print(f"[{Fore.GREEN}+{Fore.RESET}] Suggestion Recorded!")

@client.command()
async def destruct(ctx):
    await ctx.message.delete()
    print(f"[{Fore.GREEN}+{Fore.RESET}] Destroying selfbot.....")
    for num in [3,2,1]:
        if num == 3:
            time.sleep(1)
            print(f"{Fore.LIGHTGREEN_EX}3")
        if num == 2:
            time.sleep(1)
            print(f"{Fore.LIGHTYELLOW_EX}2")
        if num == 1:
            time.sleep(1)
            print(f"{Fore.LIGHTRED_EX}1")
    time.sleep(1)
    client.logout()
    clear()
    exit()

@client.command()
async def purgeall(ctx):
    await ctx.message.delete()
    print(f"[{Fore.CYAN}>{Fore.RESET}] Purging your own messages...")
    print(f"[{Fore.CYAN}>{Fore.RESET}] Input a delay: {Fore.RED}(no delay makes hella requests){Fore.RESET}")
    delay = input(" > ")
    message_count = 0
    async for message in ctx.channel.history(limit=None):
            if message.author.id == client.user.id:
                time.sleep(int(delay))
                message_count+=1
                await message.delete()
    mess = await ctx.send(f"Deleted {message_count} messages in the channel.....")
    time.sleep(2)
    await mess.delete()

@client.command()
async def shibe(ctx, *, message):

    if not message:

        shibes = json.loads(getShibe(1))

        for shibe in shibes:
            
            embed = discord.Embed()

            embed.set_image(url=shibe)

            time.sleep(3)

            await ctx.send(embed=embed)

    elif message.isdigit():

        shibes = json.loads(getShibe(message))

        for shibe in shibes:

            embed = discord.Embed()

            embed.set_image(url=shibe)

            time.sleep(3)

            await ctx.send(embed=embed)



@client.command(aliases=['Corona', 'covid19', 'coronastats'])
async def corona(ctx):
    await ctx.message.delete()
    data = covid19.getLatest()
    em = discord.Embed(color=0x4e03fc, title="Neko Corona Virus Stats")
    em.set_thumbnail(url='https://i.imgur.com/8MD9c4H.png')
    fields = [
        {'name': 'Confirmed', 'value': data['confirmed']},
        {'name': 'Deaths', 'value': data['deaths']},
        {'name': 'Recovered', 'value': data['recovered']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
    return await ctx.send(embed=em)


@client.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f"Pong! `{round(client.latency * 1000)}ms!`")

@client.command()
async def chatwipe(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')


@client.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'ipType', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'IPName', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)

@client.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#000000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xFFFFFF))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
    f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)


@client.command()
async def whois(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    em = discord.Embed(description=user.mention)
    em.set_author(name=str(user), icon_url=user.avatar_url)
    em.set_thumbnail(url=user.avatar_url)
    em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    em.add_field(name="Join position", value=str(members.index(user)+1))
    em.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        em.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    em.add_field(name="Guild permissions", value=perm_string, inline=False)
    em.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=em)


@client.command()
async def pingwebsite(ctx, website = None): # b'\xfc'
    await ctx.message.delete()
    if website is None: 
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        if r == 404:
            await ctx.send(f'Site is down, responded with a status code of {r}', delete_after=3)
        else:
            await ctx.send(f'Site is up, responded with a status code of {r}', delete_after=3)      


@client.command(name='1337-speak', aliases=['1337speak'])
async def _1337_speak(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3')\
            .replace('E', '3').replace('i', '!').replace('I', '!')\
            .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'`{text}`')


@client.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0xFF1700)
    await ctx.send(embed=em)


@client.command()
async def servercopy(ctx): # b'\xfc'
    await ctx.message.delete()
    await client.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in client.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:                
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass


@client.command()
async def serverdestroy(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="https://hentaihaven.xxx",
            reason="I Love Hentai!",
            icon=None,
            banner=None
        )  
    except:
        pass        
    for _i in range(250):
        await ctx.guild.create_text_channel(name=RandString())
    for _i in range(250):
        await ctx.guild.create_role(name=RandString(), color=RandomColor())


@client.command()
async def massban(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    

@client.command()
async def masskick(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass 

@client.command()
async def masschannel(ctx): # b'\xfc'
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name=RandString())
        except:
            return

@client.command()
async def delchannels(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@client.command()
async def spam(ctx, amount: int, *, message): # b'\xfc'
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)


@client.command(aliases=['guildpfp'])
async def guildicon(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)

@client.command(name='backup-f', aliases=['friendbackup', 'friend-backup', 'backup-friends', 'backupf']) # FIX LATER WITH FWEAK OR SOMETHING 
async def _backup_f(ctx): # b'\xfc'
    await ctx.message.delete()
    for friend in client.user.friends:
       friendlist = (friend.name)+'#'+(friend.discriminator)   
       with open('Backup/Friends.txt', 'a+') as f:
           f.write(friendlist+"\n" )
    for block in client.user.blocked:
        blocklist = (block.name)+'#'+(block.discriminator)
        with open('Backup/Blocked.txt', 'a+') as f: 
            f.write(blocklist+"\n" )

@client.command()
async def abc(ctx): # b'\xfc'
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)

@client.command(aliases=['bitcoin'])
async def btc(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)


@client.command()
async def anal(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed()   
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@client.command()
async def hentai(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@client.command()
async def uptime(ctx): # b'\xfc'
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f'`'+uptime+'`')

@client.command()
async def purge(ctx, amount: int): # b'\xfc'
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@client.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def _group_leaver(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in client.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()


@client.command(aliases=['markasread', 'ack'])
async def read(ctx): # b'\xfc'
    await ctx.message.delete()
    for guild in client.guilds:
        await guild.ack()


@client.command()
async def lenny(ctx): # b'\xfc'
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)

@client.command()
async def bold(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('**'+message+'**')


@client.command()
async def secret(ctx, *, message): # b'\xfc'
	await ctx.message.delete()
	await ctx.send('||'+message+'||')


@client.command()
async def nitro(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(Nitro())


if __name__ == "__main__":
    client.run(token, bot=False)
