import discord  # connects to discord server
import requests
import os


class MyClient(discord.Client):  # creates a MyClient class
    async def on_ready(
            self
    ):  # runs when bot connects to discord, says that it is logged in
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):  # sees the message in the chat
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:  # checks if the message is from itself
            return

        if message.content.lower() == 'j!comic':  # creates the command
            data = requests.get(
                'https://c.xkcd.com/random/comic/')  # fetches random comic
            data = requests.get(
                'https://xkcd.com/' + data.url[17:-1] +
                '/info.0.json').json()  # fetches the json data + the number
            await message.channel.send(data["img"])  # sends the actual image

        if message.content.lower() == 'j!yesno':  # creates the command
            data = requests.get(
                'https://yesno.wtf/api')  # fetches the yes/no json data
            await message.channel.send(data.json()["image"])  # sends the image

        if message.content.lower() == 'j!ree':
            await message.channel.send("ree")

        if message.content.lower() == 'j!anime':  # creates the command
            response = requests.get('https://kitsu.io/api/edge/anime'
                                    )  # fetches the yes/no json data
            data = response.json()['data']
            anime = random.choice(data)
            await message.channel.send(data.json()["image"])  # sends the image

        if message.content.lower() == 'j!hatelaptops':
            await message.channel.send(
                "Today when I walked into my economics class I saw    something I dread every time I close my eyes. Someone had brought their new gaming laptop to class. The Forklift he used to bring it was still running idle at the back. I started sweating as I sat down and gazed over at the 700lb beast that was his laptop. He had already reinforced his desk with steel support beams and was in the process of finding an outlet for a power cable thicker than Amy Schumer's thigh. I start shaking. I keep telling myself I'm going to be alright and that there's nothing to worry about. He somehow finds a fucking outlet. Tears are running down my cheeks as I send my last texts to my family saying I love them. The teacher starts the lecture, and the student turns his laptop on. The colored lights on his RGB Backlit keyboard flare to life like a nuclear flash, and a deep humming fills my ears and shakes my very soul. The entire city power grid goes dark. The classroom begins to shake as the massive fans begin to spin. In mere seconds my world has gone from vibrant life, to a dark, earth shattering void where my body is getting torn apart by the 150mph gale force winds and the 500 decibel groan of the cooling fans. As my body finally surrenders, I weep, as my school and my city go under. I fucking hate gaming laptops."
            )
        if message.content.startswith('j!add '):
            #await message.channel.send('Die!')
            #print("hi")
            data = message.content[6:]  # gets the content from the message
            try:
                ans = int(data.split(" ")[0]) + int(data.split(" ")[1])
                await message.channel.send(ans)
            except:
                await message.channel.send("Please enter an integer")
                # await means that it waits for the async command to stop, allows multiple users to use the bot at once
                # if the bot is waiting for a response from the HTTP website, then async (a.k.a a coroutine) allows it to submit a request, like a request to the website, and then do other work in the queue, like reading the chat, while waiting for the HTTP website to respond
                # await tells the code that it is waiting for it to be run, which is useful in async - https://docs.python.org/3/library/asyncio-task.html, https://stackabuse.com/python-async-await-tutorial/
                # the main idea is if statement for commands in the chat, then fetch the data from the source, then send it to the chat


client = MyClient()  # creates an obj
client.run(os.environ['DISCORD_TOKEN'])  # token for the bot
