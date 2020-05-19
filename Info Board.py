import discord
import json
from discord.ext import commands
with open('config.json') as f:
    config = json.load(f)

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print('Logged in as {}'.format(bot.user.name))
    print('------')

#introduction
#----------------------------------------------------------------
@bot.command(name = 'greetings')
async def intro(ctx):
    await ctx.channel.send("Welcome traveler to Pamphlet, Im Odette. \nHere to learn something new? or to exchange information? \nEither way if you have any question just call for !help")

@bot.remove_command("help")
@bot.command(name = 'help', pass_context=True)
async def help(ctx):
    await ctx.channel.send("Pamphlet is a phrontistery, an establishment of knowledge if you will. \nWould you like to !learn ?")

@bot.command(name = 'learn')
async def learn(ctx):
    await ctx.channel.send("At the moment I'm short on information but can supply you more knowledge of the people around Acacia. \nJust say their !name")
#----------------------------------------------------------------




# Guild Members
#----------------------------------------------------------------
@bot.command(aliases =['caserin', 'babyboy', 'whatishentai'])
async def Caserin (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Caserin.png'))
    await ctx.channel.send("Oh? Weird of you to ask about him, everyone know who Caserin Ottom is.")
    await ctx.channel.send("""
**Caserin S. Ottom**
Wood elf Paladin level 20
Strength: +2
Dexterity: 0
Constitution: +2
Intelligence: 0
Wisdom: +2
Charisma: +3
Skills: Athletics, Insight, Perception, Survival
Weapons: 2 Short swords, Javelins
    """)

@bot.command(aliases =['kigana', 'kiki', 'bazinga', 'scaly'])
async def Kigana (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Kigana.png'))
    await ctx.channel.send("Ahh so many tales of the white dragon! \nShe's the tough left hand of mr Ottom himself!")
    await ctx.channel.send("""
**Kigana Aorogo**
Dragonborn Fighter level 14
Strength: +4
Dexterity: +3
Constitution: +3
Intelligence: +1
Wisdom: +1
Charisma: +3
Skills: Athletics, Insight, Survival
Weapons: 2 Hand axes, War axe
    """)

@bot.command(aliases = ['zoel', 'tired', 'dealer', 'blind', 'noeyes'])
async def Zoel (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Zoel.png'))
    await ctx.channel.send("A quiet one, I rarely saw him out in town unless he's passing into the forest.")
    await ctx.channel.send("""
**Zoel Oakmor**
Human Ranger level 14
Strength: +2
Dexterity: +2
Constitution: +2
Intelligence: +1
Wisdom: +4
Charisma: +2
Skills: Animal handling, Insight, Perception
Weapons: Short sword, Long bow
    """)

@bot.command(aliases = ['moragel', 'mori', 'robbie', 'robbierotten'])
async def Moragel (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Moragel.png'))
    await ctx.channel.send("He seems to stay to the shadows. I dont know much about him, but i do know he's loyal.")
    await ctx.channel.send("""
**Moragel Blacken**
High elf Rogue level 14
Strength: 0
Dexterity: +5
Constitution: +1
Intelligence: +4
Wisdom: +1
Charisma: 0
Skills: Acrobatics, Insight, Investigation, Perception, Performance, Stealth
Weapons: 2 Knives, Crossbow
    """)

@bot.command(aliases=['alexen', 'ale', 'hubby'])
async def Alexen (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Ale.png'))
    await ctx.channel.send("Ah the local tavern keep!\nSweet man that one, really proving the tiefling tales wrong.")
    await ctx.channel.send("""
**Alexen Aardvark**
Tiefling Bard level 14
Strength: +1
Dexterity: +2
Constitution: +2
Intelligence: 0
Wisdom: +1
Charisma: +2
Skills: Acrobatics, Deception, Insight, Performance, Persuasion 
Weapons: Rapier, Dagger
    """)

@bot.command(aliases = ['gusher', 'twunk', 'bigfoot'])
async def Gusher (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Gusher.png'))
    await ctx.channel.send("At first I thought he was a big mean fella, but he ended up being a gentle giant... sounds familiar")
    await ctx.channel.send("""
**Gusher**
Bugbear Barbarian level 14
Strength: +4
Dexterity: +3
Constitution: +3
Intelligence: 0
Wisdom: +1
Charisma: 0
Skills: Athletics, Intimidation, Stealth, Survival
Weapons: Battle axe
    """)

@bot.command(aliases =['sea', 'furry', ':3'])
async def Sea (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Sea.png'))
    await ctx.channel.send("She likes to call herself the better half, her brother disagrees.")
    await ctx.channel.send("""
**Sea Fog**
Tabaxi Monk level 14
Strength: +2
Dexterity: +4
Constitution: +1
Intelligence: +3
Wisdom: +2
Charisma: +2
Skills: Acrobatics, History, Insight, perception, Stealth
Weapons: Short sword, 2 Sickles
    """)

@bot.command(aliases =['smoke', 'vape', '420', 'naruto'])
async def Smoke (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Smoke.png'))
    await ctx.channel.send("He's a feisty one! arguably the polar opposite of his older sister.")
    await ctx.channel.send("""
**Smoke Water**
Tabaxi Sorcerer level 14
Strength: +1
Dexterity: +4
Constitution: +2
Intelligence: +2
Wisdom: +1
Charisma: +4
Skills: Arcana, Insight, Intimidation, Perception, stealth
Weapons: 2 Daggers, Quarterstaff
    """)

@bot.command(aliases =['gaela', 'boxer'])
async def Gaela (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Gaela.png'))
    await ctx.channel.send("I hear some auful gossip about her... \nI hope its not true.")
    await ctx.channel.send("""
**Gaela**
Half orc Barbarian level 14
Strength: +4
Dexterity: +1
Constitution: +3
Intelligence: +1
Wisdom: +2
Charisma: 0
Skills: Athletics, Intimidation, Survival
Weapons: 2 Hand axe, Great axe
    """)

@bot.command(aliases =['spring', 'summer'])
async def Spring (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Spring.png'))
    await ctx.channel.send("A man of the book, he practices science.. and self love.")
    await ctx.channel.send("""
**Spring Blackbuck**
Hill dwarf Wizard level 14
Strength: +1
Dexterity: 0
Constitution: +2
Intelligence: +2
Wisdom: +3
Charisma: 0
Skills: Arcana, History
Weapons: Quarterstaff, Hand axe
    """)

@bot.command(aliases = ['vix', 'vixera', 'ginger', 'scientology'])
async def Vixera (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Vixera.png'))
    await ctx.channel.send("A very bright woman, with a very short fuse.")
    await ctx.channel.send("""
**Vixera Amali**
Human Cleric level 14
Strength: 0
Dexterity: +2
Constitution: 0
Intelligence: +4
Wisdom: +4
Charisma: 0
Skills: Arcana, Nature, Religion, Sleight of hand
Weapons: Dagger, Quarterstaff
    """)

@bot.command(aliases = ['siverdale', 'snipsnip', 'snippetman', 'tinyman', 'gnotagnelf', 'gnotagnoblin'])
async def Siverdale (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Siverdale.png'))
    await ctx.channel.send("Can't fathom how an innocent young lad found himself in this establishment.")
    await ctx.channel.send("""
**Siverdale Ox**
Gnome Ranger level 14
Strength: 0
Dexterity: +1
Constitution: +2
Intelligence: +1
Wisdom: 0
Charisma: +4
Skills: Animal handling, Nature, Perception
Weapons: Short bow, Mace
    """)

@bot.command(aliases = ['simon', 'semen', 'hentai', 'twink', 'handjob'])
async def Simon (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Simon.png'))
    await ctx.channel.send("I heard stories about his relatives but... these stories don't sound likely.")
    await ctx.channel.send("""
**Simon Reeves**
Half elf Bard level 4
Strength: 0
Dexterity: +2
Constitution: +1
Intelligence: 0
Wisdom: +2
Charisma: +3
Skills: Deception, Insight, Perception, Performance, Persuasion
Weapons: Short bow, Dagger, War hammer, Long bow
    """)

@bot.command(aliases = ['vanelis', 'vanilla', 'onehand', 'virgin', 'cripple', 'handy', 'boomer', 'winemom', 'villagesaver'])
async def Vanelis (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Vanelis.png'))
    await ctx.channel.send("I heard rumors of his past, just make sure you shake the right hand.")
    await ctx.channel.send("""
**Vanelis Udon**
Half elf Warlock level 4
Strength: +3
Dexterity: 0
Constitution: +2
Intelligence: 0
Wisdom: +2
Charisma: +2
Skills: Arcana, Deception, Intimidation, Investigation, Perception
Weapons: 2 Hand axe, 2 Dagger, Staff, Morning star
    """)

@bot.command(aliases = ['naatzi', 'hitler', 'natzi', 'megumin', 'vore', 'phoo', 'nazi', 'lizard'])
async def Naatzi (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Naatzi.png'))
    await ctx.channel.send("Hot temper... hot head... make sure to have a bucket of water near him.")
    await ctx.channel.send("""
**Naatzi**
Dragonborn Sorcerer level 4
Strength: +5
Dexterity: +1
Constitution: 0
Intelligence: +1
Wisdom: 0
Charisma: +1
Skills: Arcana, Athletics, Insight
Weapons: Short sword, Battle axe, Light crossbow, 4 Daggers
    """)

@bot.command(aliases = ['raylend', 'rayman', 'raymond', 'rayboy', 'homeless', 'bum'])
async def Raylend (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Raylend.png'))
    await ctx.channel.send("I dont even know his last name, heard he keeps his past a secret... \nI wonder why.")
    await ctx.channel.send("""
**Raylend** 
Human Ranger level 4
Strength: +1
Dexterity: +4
Constitution: +3
Intelligence: +1
Wisdom: +1
Charisma: -2
Skills: Deception, Insight, Perception, Performance, Persuasion
Weapons: Crossbow, Dagger, Long bow, Longsword
    """)

@bot.command(aliases = ['danarei', 'mercy', 'pacifistroute', 'heroesneverdie', 'loli'])
async def Danarei (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Danarei.png'))
    await ctx.channel.send("I heard some stories of a pacifist in the guild, but I never thought of them to be true.")
    await ctx.channel.send("""
**Danarei Nikos**
Tiefling Cleric level 4
Strength: -1
Dexterity: 0
Constitution: +1
Intelligence: +3
Wisdom: +1
Charisma: +3
Skills: Medicine, Religion
Weapons: The power of love
    """)

@bot.command(aliases = ['thoradin', 'toblerone', 'torbjorn', 'onion'])
async def Thoradin (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Thoradin.png'))
    await ctx.channel.send("Heard of a stubborn cleric with a weird obsession with sparrows, although I didnt see him around lately.")
    await ctx.channel.send("""
**Thoradin**
Hill dwarf Cleric level 3
Strength: +1
Dexterity: +1
Constitution: +3
Intelligence: 0
Wisdom: +3
Charisma: -1
Skills: Religion, Insight, Medicine, Persuasion
Weapons: Warhammer, Hand axe
    """)
#----------------------------------------------------------------




# Acacia residents
#----------------------------------------------------------------
@bot.command(aliases = ['rumia', 'rum', 'rummy', 'wifey', 'boozemom'])
async def Rumia (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Rum.png'))
    await ctx.channel.send("A dear friend! I heard she's the only one who tamed Mr. free bird himself.")
    await ctx.channel.send("""
**Rumia Aardvark**
Human Warlock level 14
Strength: +2
Dexterity: +3
Constitution: +3
Intelligence: 0
Wisdom: +1
Charisma: +3
Skills: Deception, Investigation, Performance, Persuasion
Weapons: Hand axe, Light crossbow
    """)

@bot.command(aliases = ['flutter', 'bird', 'seeds', 'prettybird', 'featherey', 'avian', 'crow'])
async def Flutter (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Flutter.png'))
    await ctx.channel.send("A curious type, never met a kenku that speaks common as well as him.")
    await ctx.channel.send("""
**Flutter**
Kenku Warlock level 12
Strength: +1
Dexterity: +2
Constitution: +1
Intelligence: +2
Wisdom: +1
Charisma: +2
Skills: Deception, History, Persuasion, Stealth
Weapons: Dagger, Sickle
    """)

@bot.command(aliases = ['strong', 'orc', 'pie', 'pieman', 'soft'])
async def Strong (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Strong.png'))
    await ctx.channel.send("Has a frightning demeanor, but he's as sweet as the pies he bakes.")
    await ctx.channel.send("""
**Strong**
Orc Fighter level 14
Strength: +4
Dexterity: +1
Constitution: +4
Intelligence: +1
Wisdom: +1
Charisma: +2
Skills: Insight, Intimidation, Survival
Weapons: 2 Short sword
    """)

@bot.command(aliases = ['odette', 'gardengnome', 'librarian'])
async def Odette (ctx):
    await ctx.channel.send(file=discord.File('Pictures/Odette.png'))
    await ctx.channel.send("Oh thats me the most knowledgeable gnome alive, in thirteen languages!\nDon't mind the embarrassing picture, they wont let me change it")
    await ctx.channel.send("""
**Odette Newton**
Gnome Wizard level 14
Strength: -1
Dexterity: +2
Constitution: 0
Intelligence: +3
Wisdom: +4
Charisma: 0
Skills: Arcana, History, Investigation, Nature
Weapons: Quarterstaff
    """)
#----------------------------------------------------------------




# Unknown deitys
#----------------------------------------------------------------
@bot.command(aliases = ['dm', 'them', 'gm', 'GM', 'god', 'godmode', 'sexy', 'jesus', 'voldemort', 'theunspoken', 'beholder','pussymagnet'])
async def DM(ctx):
    await ctx.channel.send(file=discord.File('Pictures/DM.png'))
    await ctx.channel.send("I... I do not know who you speak of..")
    await ctx.channel.send("""
**DM**
Creator level ????????
Strength: 99999
Dexterity: 99999
Constitution: 99999
Intelligence: 99999
Wisdom: 99999
Charisma: 99999
Skills: Bending the fabric of time
Weapons: ????????
    """)

@bot.command(name = 'gay')
async def gay(ctx):
    await ctx.channel.send("{} your mother is a homosexual".format(ctx.message.author.mention))
#----------------------------------------------------------------

bot.run(config['token'])