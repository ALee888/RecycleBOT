# RecycleBot

RecycleBot is a lightweight Discord bot designed to track and manage in-game recycling totals for my sister's GTA RP group. The bot allows users to manually input recycling numbers, which are then stored and can be backed up using Python's shelve library for persistent data storage.
## Features
- Manual Input Tracking: Users can input recycling numbers directly via Discord commands.
- Data Backup: Utilizes the shelve library to store and back up recycling totals.
- Lightweight: Designed to be simple and efficient, making it easy to run on various hosting platforms.

## Installation and Usage
### Prerequisites
- Python 3.x
- discord.py library
- shelve library (included in Python's standard library)

### Running the Bot
1. Clone the repository or download the source code.
2. Install the required dependencies:
```bash
pip install discord.py
```
3. Run the bot:
```bash
python bot.py
```

### Hosting
The bot is currently hosted on a server hosting site. A setup script is included to simplify deployment on the hosting platform.

## Technologies Used
- **Language**: Python
- **Data Storage**: shelve
