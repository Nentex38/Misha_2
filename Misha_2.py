import discord
from discord.ext import commands

class Misha(commands.Bot):
    def __init__(self, !):
        super().__init__(!)
        self.user_data = {}

    async def on_ready(self):
        print(f"{self.user} is ready to go!")

    async def on_message(self, message):
        # Ignore messages from the bot itself
        if message.author == self.user:
            return

        # Check if user data exists, create a new dict if not
        user_id = str(message.author.id)
        if user_id not in self.user_data:
            self.user_data[user_id] = {}

        # Generate an OpenAI prompt based on user message and their data
        prompt = f"User: {message.content}\nMisha:"
        for key, value in self.user_data[user_id].items():
            prompt += f" {key}={value}"

        # Use OpenAI API to generate a response
        # You'll need to set up your own OpenAI API key
        # See https://beta.openai.com/docs/quickstart for instructions
        # on how to get an API key and install the OpenAI Python package
        import openai
        openai.api_key = "YOUR_API_KEY"
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            temperature=0.5,
            max_tokens=128,
            n=1,
            stop=None,
            timeout=10,
        )

        # Extract response from OpenAI output and send it to the user
        response_text = response.choices[0].text.strip()
        self.user_data[user_id] = self.extract_user_data(response_text)
        await message.channel.send(response_text)

    def extract_user_data(self, response_text):
        # Extract data from OpenAI response and store it in a dictionary
        user_data = {}
        for line in response_text.split("\n"):
            line = line.strip()
            if line.startswith("Misha:"):
                data = line.split(":")[1].strip()
                key, value = data.split("=")
                user_data[key] = value
        return user_data

bot = Misha(!="!")
bot.run("MTA0ODgzMzIwNzU1MTkzMDQxOA.GItLqG.BIDNiQZ7Wob9Dg8QCOGFrBXkjpDhjwvw1abrXc")
    
