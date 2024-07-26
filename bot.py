import discord
from discord.ext import tasks, commands
import feedparser
from datetime import datetime, timezone, timedelta
import pytz
import time

LOCAL_TIMEZONE = pytz.timezone('Asia/Colombo')  # Replace with your local timezone

intents = discord.Intents.default()
client = discord.Client(intents=intents)

channel_id = "Channel ID of Your Choice"  # Replace with your channel ID
feed_url = "http://www.livechart.me/feeds/episodes"
posted_entries = set()  # To keep track of posted entries

def fetch_releases():
    feed = feedparser.parse(feed_url)
    entries = []
    for entry in feed.entries:
        if entry.id not in posted_entries:
            iso_format = time.strftime("%Y-%m-%dT%H:%M:%SZ", entry.published_parsed)
            published = datetime.fromisoformat(iso_format)
            entries.append({
                "title": entry.title,
                "link": entry.link,
                "published": published,
                "description": entry.get("description", "No description available."),
            })
            posted_entries.add(entry.id)
    return entries

@tasks.loop(minutes=1)
async def check_releases():
    releases = fetch_releases()
    for release in releases:
        embed = discord.Embed(title=release["title"], url=release["link"], description=release["description"], timestamp=release["published"])
        embed.set_footer(text="Anime Release Feed")
        channel = client.get_channel(channel_id)
        await channel.send(embed=embed)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    check_releases.start()

client.run("Your Bot Token")
