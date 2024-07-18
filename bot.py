import discord
import requests
from bs4 import BeautifulSoup
import asyncio
import datetime

TOKEN = ''
CHANNEL_ID = ''
ANIMEPAHE_URL = 'https://animepahe.ru'

intents = discord.Intents.default()
intents.messages = True  # Enable the message intent
intents.typing = False   # You can adjust these intents as needed

client = discord.Client(intents=intents)

async def check_new_uploads():
    await client.wait_until_ready()
    channel = client.get_channel(int(CHANNEL_ID))
    last_link = ""
    refresh_interval = 3600  # Interval in seconds (1 hour)
    
    countdown_message = None
    
    while not client.is_closed():
        try:
            response = requests.get(ANIMEPAHE_URL)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # CSS Selector for the latest upload element
            latest_upload = soup.select_one('.latest-release .episode-list-row .episode-wrap')
            
            if latest_upload:
                latest_title_element = latest_upload.select_one('.episode-title a')
                latest_title = latest_title_element.get_text()
                latest_link = latest_title_element['href']
                latest_episode = latest_upload.select_one('.episode-number-wrap').get_text()

                if latest_link != last_link:
                    await channel.send(f"New upload: {latest_title} - Episode {latest_episode}\nLink: {ANIMEPAHE_URL}{latest_link}")
                    last_link = latest_link
            else:
                # No latest episode found
                await channel.send("No latest episode found.")
            
            # Calculate countdown timer until next refresh
            countdown = refresh_interval
            while countdown > 0:
                minutes, seconds = divmod(countdown, 60)
                if countdown % 60 == 0 or countdown == refresh_interval:
                    if countdown_message:
                        await countdown_message.edit(content=f"Next refresh in {minutes} minutes and {seconds} seconds.")
                    else:
                        countdown_message = await channel.send(f"Next refresh in {minutes} minutes and {seconds} seconds.")
                await asyncio.sleep(1)  # Sleep for 1 second
                countdown -= 1

        except Exception as e:
            print(f"Error: {e}")

        await asyncio.sleep(refresh_interval)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    client.loop.create_task(check_new_uploads())

if __name__ == '__main__':
    asyncio.run(client.start(TOKEN))
