import discord
from discord.ext import commands
import os

client = discord.Client()
bot = commands.Bot(command_prefix="$")

async def getData():
    with open("accounts.txt") as f:
        data = f.readlines()
        f.close()
    size = len(data) 
    for i in range(size):
        data[i] = data[i].strip('\n')
    return data

async def writeData(data):
    open("accounts.txt","w").close()
    with open("accounts.txt","w") as f:
        for i in range(len(data)):
            f.write(data[i] + "\n")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@bot.command(name='gold')
async def gold_acc(ctx):
    data = await getData()
    counter = 0
    result = ""
    for i in range(len(data)):
        details = data[i].split(':')
        if "Gold" in details[2]:
            counter = counter + 1
            result = result + "IGN      : " + details[0]+"#"+details[1]+ "\nRANK  : " + details[2]+ "\nID         : " + details[3]+"\nPASS   : " + details[4]+ "\n------------------------------------\n"
    if counter == 0:
        await ctx.send("No accounts found at Gold")
    else:
        await ctx.send(result)

@bot.command(name='bronze',brief="1 game behind the most recent match")
async def bronze_acc(ctx):
    data = await getData()
    counter = 0
    result = ""
    for i in range(len(data)):
        details = data[i].split(':')
        if "Bronze" in details[2]:
            counter = counter + 1
            result = result + "IGN      : " + details[0]+"#"+details[1]+ "\nRANK  : " + details[2]+ "\nID         : " + details[3]+"\nPASS   : " + details[4]+ "\n------------------------------------\n"
    if counter == 0:
        await ctx.send("No accounts found at Bronze")
    else:
        await ctx.send(result)

@bot.command(name='iron')
async def iron_acc(ctx):
    data = await getData()
    counter = 0
    result = ""
    for i in range(len(data)):
        details = data[i].split(':')
        if "Iron" in details[2]:
            counter = counter + 1
            result = result + "IGN      : " + details[0]+"#"+details[1]+ "\nRANK  : " + details[2]+ "\nID         : " + details[3]+"\nPASS   : " + details[4]+ "\n------------------------------------\n"
    if counter == 0:
        await ctx.send("No accounts found at Iron")
    else:
        await ctx.send(result)

@bot.command(name='all',brief="This bot will update the ranks every 6hrs. Ranks shown are")
async def all_acc(ctx):
    data = await getData()
    result = ""
    counter = 0
    for i in range(len(data)):
        counter = counter + 1
        details = data[i].split(':')
        result = result + "IGN      : " + details[0]+"#"+details[1]+ "\nRANK  : " + details[2]+ "\nID         : " + details[3]+"\nPASS   : " + details[4]+ "\n------------------------------------\n"
        if counter == 12:
            await ctx.send(result)
            result = ""
    await ctx.send(result)

@bot.command(name='silver')
async def silver_acc(ctx):
    data = await getData()
    counter = 0
    result = ""
    for i in range(len(data)):
        details = data[i].split(':')
        if "Silver" in details[2]:
            counter = counter + 1
            result = result + "IGN      : " + details[0]+"#"+details[1]+ "\nRANK  : " + details[2]+ "\nID         : " + details[3]+"\nPASS   : " + details[4]+ "\n------------------------------------\n"
    if counter == 0:
        await ctx.send("No accounts found at Silver")
    else:
        await ctx.send(result)

@bot.command(name='plat')
async def plat_acc(ctx):
    data = await getData()
    counter = 0
    result = ""
    for i in range(len(data)):
        details = data[i].split(':')
        if "Platinum" in details[2]:
            counter = counter + 1
            result = result + "IGN      : " + details[0]+"#"+details[1]+ "\nRANK  : " + details[2]+ "\nID         : " + details[3]+"\nPASS   : " + details[4]+ "\n------------------------------------\n"
    if counter == 0:
        await ctx.send("No accounts found at Platinum")
    else:
        await ctx.send(result)

@bot.command(name='diamond')
async def dia_acc(ctx):
    data = await getData()
    counter = 0
    result = ""
    for i in range(len(data)):
        details = data[i].split(':')
        if "Diamond" in details[2]:
            counter = counter + 1
            result = result + "IGN      : " + details[0]+"#"+details[1]+ "\nRANK  : " + details[2]+ "\nID         : " + details[3]+"\nPASS   : " + details[4]+ "\n------------------------------------\n"
    if counter == 0:
        await ctx.send("No accounts found at Diamond")
    else:
        await ctx.send(result)

@bot.command(name="ign",brief="<command> <old_name#tag> <new_name#tag>")
async def upd_ign(ctx,arg1,arg2):
    data = await getData()
    for i in range(len(data)):
        details = data[i].split(":")
        ign = details[0] + "#" + details[1]
        if str(arg1) == ign:
            new_ign = arg2.split("#")
            details[0] = new_ign[0]
            details[1] = new_ign[1]
            data[i] = details[0] + ":" + details[1] + ":" + details[2] +  ":" +details[3] +":" + details[4]
            await writeData(data)
            await ctx.send("IGN updated")
            return
    await ctx.send("IGN not found")

@bot.command(name="id",brief="<command> <old_id> <new_id>")
async def upd_id(ctx,arg1,arg2):
    data = await getData()
    for i in range(len(data)):
        details = data[i].split(":")
        id = details[3]
        if str(arg1) == id:
            new_id = str(arg2)
            details[3] = new_id
            data[i] = details[0] + ":" + details[1] + ":" + details[2] +  ":" +details[3] +":" + details[4]
            await writeData(data)
            await ctx.send("ID updated")
            return
    await ctx.send("ID not found")

@bot.command(name="pass",brief="<command> <old_pass> <new_pass>")
async def upd_pw(ctx,arg1,arg2):
    data = await getData()
    for i in range(len(data)):
        details = data[i].split(":")
        pw = details[4]
        if str(arg1) == pw:
            new_pass = str(arg2)
            details[4] = new_pass
            data[i] = details[0] + ":" + details[1] + ":" + details[2] +  ":" +details[3] +":" + details[4]
            await writeData(data)
            await ctx.send("Password updated")
            return
    await ctx.send("Password not found")

@bot.command(name="add",brief="<command> <name#tag> <id> <pw>")
async def add_acc(ctx,arg1,arg2,arg3):
    data = await getData()
    name = str(arg1).split("#")
    data.append(name[0] + ":" + name[1] + ":Unrated:" + str(arg2) +":" + str(arg3))
    await writeData(data)
    await ctx.send("Account added")

@bot.command(name="del",brief="<command> <name#tag>")
async def del_acc(ctx,arg1):
    data = await getData()
    new_data = []
    for i in range(len(data)):
        details = data[i].split(":")
        if str(arg1) not in (details[0] + "#" + details[1]):
            new_data.append(data[i])
    await writeData(new_data)
    await ctx.send("Account list updated")

bot.run("ODc2MDkxNDE0OTQ0MDM0ODU2.YRfBtg.JhBfvUmlcrYelWhsf7YrBYpmNCA")
