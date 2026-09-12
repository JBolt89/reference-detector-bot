# Nullscape Reference Detector
This is the original project I created reference detector bot for.

All the references to the Roblox game Nullscape are already in the project, all you need to do is set it up!

# Setup Instructions
All the setup instructions to getting the bot running locally.
This guide will assume that you are somewhat new to using a terminal.
## Linux
1. Make sure Python is installed.
   Most distributions of Linux come with Python preinstalled, but in case it isn't, install it using your package manager.

   Debian based (Includes Ubuntu):
   ```
   sudo apt-get install python3 python3-dev
   ```
   Fedora, CentOS or Red Hat:
   ```
   sudo dnf install python3 python3-devel
   ```
   Arch Linux:
   ```
   sudo pacman -S python3
   ```
   Gentoo:
   ```
   sudo emerge dev-lang/python
   ```

2. Clone the repository.
   Open your terminal and navigate to the directory you want to clone the repository into.

   Then run the following command to clone the repository:
   ```
   git clone -b nullscape-reference-detector https://github.com/JBolt89/reference-detector-bot.git
   ```
   Navigate into the directory it was cloned into.
   ```
   cd reference-detector-bot
   ```

3. Create the venv (Virtual Environment)
   Run this command in the directory you just navigated into:
   ```
   python3 -m venv .venv
   ```
   The next command is different depending on what terminal you are using

   If using bash terminal:
   ```
   source .venv/bin/activate
   ```
   If using fish terminal:
   ```
   source .venv/bin/activate.fish
   ```

4. Install dependencies
   Run the following command. Note that you should only do this after activating the venv:
   ```
   pip install -r requirements.txt
   ```

5. Modify main.py and bot setup on Discord
   Open main.py in the text editor of your choice.

   Modify the line near the bottom of your code that says `bot.run("YOUR_TOKEN_HERE")`
   and replace `YOUR_TOKEN_HERE` with a bot token from the Discord developer portal.
   Make sure that the application you have on the developer portal has the Message Content intent.

   Go to the Installation tab in the application you are using for the bot and untick User Install under Installation Contexts.

   In the installation tab, scroll down to Default Install Settings and go to Guild Install. Click on the dropdown menu for scopes and click bot. Now go to the permissions tab. If you are unsure how to set up permissions, just tick Administrator.

6. Run the bot
   Run the following command to start the bot. Note that closing the terminal window will cause the bot to **go offline**:
   ```
   python main.py
   ```
   Congratulations! You have now set up Nullscape Reference Detector! Inviting the bot to your server is up to you.

# Windows
Coming soon when I have the time to write it.
