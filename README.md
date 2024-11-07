# The Hangman Game (Python X MySQL)

## Description
The Hangman Game is a Python-based application that allows players to create a personal account or play as a guest, bringing the classic word-guessing game to a digital platform. Once logged in, the computer selects a random word from a `words.txt` file. The player must guess letters to reveal the hidden word, with each incorrect guess adding a part to the hangman figure. The game concludes if the player successfully guesses the word within five incorrect guesses or loses after the sixth incorrect guess. The leaderboard displays the top 22 scores, and all player data is stored in a MySQL database for seamless management.

## Features
- **Account Creation and Login**: Players can create accounts to track progress and scores or play as guests.
- **Random Word Selection**: Each game uses a randomly selected word from `words.txt`.
- **Game Mechanics**: Players must guess letters to reveal the hidden word. Six incorrect guesses result in game over.
- **Leaderboard**: Shows the top 22 scores of all players.
- **Automated Record Management**: Player credentials and scores are securely stored and managed using MySQL.

## Motivation
This digital Hangman game eliminates the need for manual, pen-and-paper setups, reducing the potential for human error. It is time-efficient, allows organized data storage, and offers easy access to player information through MySQL, making it a comprehensive digital solution for managing and playing the classic game.

## Technologies Used
- **Languages**: Python, MySQL
- **Libraries**:
  - `mysql.connector`: For connecting and interacting with MySQL database
  - `tkinter`: For graphical user interface
  - `os` and `random`: For file operations and random word selection
  - `hangman.py` (user-defined module)

## Installation
1. Ensure Python IDLE and MySQL are installed on your system.
2. Download or clone the project files to your local machine.
3. Open `hangman_menu.py` in Python IDLE.
4. On line 6 of `hangman_menu.py`, enter your MySQL password for the variable `SQLpassword` to enable database connectivity.

## Usage
- **Running the Game**: Open and run `hangman_menu.py` in Python IDLE to start the game.
- **Login or Guest Access**: Players can log in to a personal account or play as a guest.
- **Gameplay**: Follow the on-screen prompts to guess letters and complete the hidden word.
- **Leaderboard**: View the top scores after each session.
