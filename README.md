# Discord Anime Release Feed Bot

This bot fetches the latest anime release information from a feed and posts updates to a Discord channel.

## Features

- Periodically checks an RSS feed for new anime releases.
- Posts updates to a specified Discord channel with details such as title, link, description, and published date.

## Technologies Used

- **Python**: The programming language used to write the bot.
- **discord.py**: A Python wrapper for the Discord API.
- **feedparser**: A library for parsing RSS feeds.
- **pytz**: A library for accurate and cross-platform timezone calculations.

## Prerequisites

Before running the bot, ensure you have Python installed and the necessary libraries. You can install the required libraries using the following command:

    pip install discord.py feedparser pytz

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/DinilHansana/Anime-Release-Feed
    cd Anime-Release-Feed
    ```

2. **Update configuration:**

    - Replace `"Channel ID of Your Choice"` with your Discord channel ID. (line 12)
    - Replace `"Your Bot Token"` with your Discord bot token. (line 46)
    - If necessary, replace `Asia/Colombo` with your local timezone. (line 7)

3. **Run the bot:**

    ```sh
    python bot.py
    ```

## Usage

The bot will log in to your Discord server and start checking for new anime releases every 1 minutes. If a new release is found, it will post an update to the specified Discord channel.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- [discord.py](https://github.com/Rapptz/discord.py) for providing an excellent wrapper for the Discord API.
- [feedparser](https://github.com/kurtmckee/feedparser) for making it easy to parse RSS feeds.

