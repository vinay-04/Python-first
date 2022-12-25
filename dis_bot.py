import discord

client = discord.Client()
@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("?"):
        await message.channel.send("hello_op "+ str(message.author))


client.run('ODA1Nzk3Nzc5NDk3OTQzMDcx.YBgHqQ.Yz4nJQR6ilzJYqrI_Wchek_VSxY')