from inspect import Traceback
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
    open("accounts.txt", "w").close()
    with open("accounts.txt", "w") as f:
        for i in range(len(data)):
            f.write(data[i] + "\n")


async def getAuthUserData():
    with open("user_id.txt") as f:
        data = f.readlines()
        f.close()
    size = len(data)
    for i in range(size):
        data[i] = data[i].strip('\n')
    return data


async def writeAuthUserData(data):
    open("user_id.txt", "w").close()
    with open("user_id.txt", "w") as f:
        for i in range(len(data)):
            f.write(data[i]+"\n")


async def getRankList(rank):
    data = await getData()
    counter = 0
    result = ""
    for i in range(len(data)):
        details = data[i].split(':')
        if rank in details[2]:
            counter = counter + 1
            result = result + "IGN      : " + details[0]+"#"+details[1] + "\nRANK  : " + details[2] + \
                "\nID         : " + \
                details[3]+"\nPASS   : " + details[4] + \
                "\n------------------------------------\n"
    return counter, result


def isItDev(ctx):
    if ctx.author.id == 360081149407526912 or ctx.author.id == 203699964000337921:
        return True
    else:
        return False


async def isItAuthUser(ctx):
    data = await getAuthUserData()
    isAuth = False
    for i in range(len(data)):
        userID = data[i].split(":")
        if str(ctx.author.id) == userID[0]:
            isAuth = True
            break
    return isAuth


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@bot.command(name='gold')
@commands.check(isItAuthUser)
async def gold_acc(ctx):
    counter, result = await getRankList("Gold")
    if counter == 0:
        await ctx.author.send("No accounts found at Gold")
    else:
        await ctx.author.send(result)


@bot.command(name='bronze', brief="1 game behind the most recent match")
@commands.check(isItAuthUser)
async def bronze_acc(ctx):
    counter, result = await getRankList("Bronze")
    if counter == 0:
        await ctx.author.send("No accounts found at Bronze")
    else:
        await ctx.author.send(result)


@bot.command(name='iron')
@commands.check(isItAuthUser)
async def iron_acc(ctx):
    counter, result = await getRankList("Iron")
    if counter == 0:
        await ctx.author.send("No accounts found at Iron")
    else:
        await ctx.author.send(result)


@bot.command(name='all', brief="This bot will update the ranks every 6hrs. Ranks shown are")
@commands.check(isItAuthUser)
async def all_acc(ctx):
    data = await getData()
    result = ""
    counter = 0
    for i in range(len(data)):
        counter = counter + 1
        details = data[i].split(':')
        result = result + "IGN      : " + details[0]+"#"+details[1] + "\nRANK  : " + details[2] + \
            "\nID         : " + details[3]+"\nPASS   : " + \
            details[4] + "\n------------------------------------\n"
        if counter == 10:
            await ctx.author.send(result)
            result = ""
    await ctx.author.send(result)


@bot.command(name='silver')
@commands.check(isItAuthUser)
async def silver_acc(ctx):
    counter, result = await getRankList("Silver")
    if counter == 0:
        await ctx.author.send("No accounts found at Silver")
    else:
        await ctx.author.send(result)


@bot.command(name='plat')
@commands.check(isItAuthUser)
async def plat_acc(ctx):
    counter, result = await getRankList("Platinum")
    if counter == 0:
        await ctx.author.send("No accounts found at Platinum")
    else:
        await ctx.author.send(result)


@bot.command(name='diamond')
@commands.check(isItAuthUser)
async def dia_acc(ctx):
    counter, result = await getRankList("Diamond")
    if counter == 0:
        await ctx.author.send("No accounts found at Diamond")
    else:
        await ctx.author.send(result)


@bot.command(name="ign", brief="<command> <old_name#tag> <new_name#tag>")
@commands.check(isItAuthUser)
async def upd_ign(ctx, arg1, arg2):
    data = await getData()
    for i in range(len(data)):
        details = data[i].split(":")
        ign = details[0] + "#" + details[1]
        if str(arg1) == ign:
            new_ign = arg2.split("#")
            details[0] = new_ign[0]
            details[1] = new_ign[1]
            data[i] = details[0] + ":" + details[1] + ":" + \
                details[2] + ":" + details[3] + ":" + details[4]
            await writeData(data)
            await ctx.author.send("IGN updated")
            return
    await ctx.author.send("IGN not found")


@bot.command(name="id", brief="<command> <old_id> <new_id>")
@commands.check(isItAuthUser)
async def upd_id(ctx, arg1, arg2):
    data = await getData()
    for i in range(len(data)):
        details = data[i].split(":")
        id = details[3]
        if str(arg1) == id:
            new_id = str(arg2)
            details[3] = new_id
            data[i] = details[0] + ":" + details[1] + ":" + \
                details[2] + ":" + details[3] + ":" + details[4]
            await writeData(data)
            await ctx.author.send("ID updated")
            return
    await ctx.author.send("ID not found")


@bot.command(name="pass", brief="<command> <old_pass> <new_pass>")
@commands.check(isItAuthUser)
async def upd_pw(ctx, arg1, arg2):
    data = await getData()
    for i in range(len(data)):
        details = data[i].split(":")
        pw = details[4]
        if str(arg1) == pw:
            new_pass = str(arg2)
            details[4] = new_pass
            data[i] = details[0] + ":" + details[1] + ":" + \
                details[2] + ":" + details[3] + ":" + details[4]
            await writeData(data)
            await ctx.author.send("Password updated")
            return
    await ctx.author.send("Password not found")


@bot.command(name="add", brief="<command> <name#tag> <id> <pw>")
@commands.check(isItAuthUser)
async def add_acc(ctx, arg1, arg2, arg3):
    data = await getData()
    name = str(arg1).split("#")
    data.append(name[0] + ":" + name[1] + ":Unrated:" +
                str(arg2) + ":" + str(arg3))
    await writeData(data)
    await ctx.author.send("Account added")


@bot.command(name="del", brief="<command> <name#tag>")
@commands.check(isItAuthUser)
async def del_acc(ctx, arg1):
    data = await getData()
    new_data = []
    for i in range(len(data)):
        details = data[i].split(":")
        if str(arg1) not in (details[0] + "#" + details[1]):
            new_data.append(data[i])
    await writeData(new_data)
    await ctx.author.send("Account list updated")


@bot.command(name="adduser", brief="<command> <username>")
@commands.check(isItDev)
async def add_auth_user(ctx, member: discord.Member):
    data = await getAuthUserData()
    new_data = []
    exsits = False
    for i in range(len(data)):
        details = data[i].split(":")
        if str(member.id) not in (details[0]):
            new_data.append(data[i])
        else:
            exsits = True
            break
    if exsits:
        await ctx.author.send("{} already exsits".format(member))
    else:
        new_data.append("{}:{}".format(member.id, member.name))
        await writeAuthUserData(new_data)
        await ctx.author.send("{} added successfully".format(member))


@bot.command(name="deluser", brief="<command> <username>")
@commands.check(isItDev)
async def del_auth_user(ctx, member: discord.Member):
    data = await getAuthUserData()
    new_data = []
    exsits = False
    for i in range(len(data)):
        details = data[i].split(":")
        if str(member.id) not in (details[0]):
            new_data.append(data[i])
        else:
            exsits = True
            break
    if(exsits):
        await writeAuthUserData(new_data)
        await ctx.author.send("{} deleted successfully".format(member))
    else:
        await ctx.author.send("{} doesn't exsits".format(member))


@bot.command(name="alluser", brief="<command> <username>")
@commands.check(isItDev)
async def del_auth_user(ctx):
    data = await getAuthUserData()
    result = ""
    for i in range(len(data)):
        details = data[i].split(":")
        result = result + str(details[1]) + \
            "\n------------------------------------\n"
    await ctx.author.send(result)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.author.send("Sorry you don't have the required permissions!\nPlease contact the developers")
    else:
        print('Ignoring exception in command {}:'.format(
            ctx.command), file=os.system.stderr())
        Traceback.print_exception(
            type(error), error, error.__traceback__, file=os.system.stderr())


bot.run("")
