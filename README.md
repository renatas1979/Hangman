# Game Title: Hangman

# Description:

Hangman is a game where players must guess a hidden word by suggesting letters. 
The game begins with a hidden word represented by dashes, each dash symbolizing a letter in the word. 
Each time a player guesses a letter, if it's in the word, the corresponding dashes are replaced with the guessed letter. 
If the guessed letter is not in the word, the player receives a strike. 
The player is allowed a certain number of strikes before their body is drawn on the gallows. 
The game continues until the player guesses the entire word or makes enough mistakes to have their figure completely drawn.

Objective of the Game:
The objective of the game is to guess the hidden word correctly before accumulating too many strikes.


# How to Play

1. **Starting the Game:**
   - Run the Python script to start the game.
   - You will be prompted to choose a language (currently supported: Lithuanian and English).

2. **Game Rules:**
   - You have to guess the word by suggesting letters or by guessing the entire word.
   - You have a limited number of attempts. For each incorrect guess, a part of the hangman is drawn.
   - If you guess the word correctly before the hangman is fully drawn, you win!
   - Be careful! If the hangman is fully drawn before you guess the word, you lose the game.

3. **Game Controls:**
   - Enter a single letter to guess a letter.
   - Enter the entire word to guess the entire word.

4. **Feedback:**
   - Correct guesses will be shown in the word display.
   - Incorrect guesses will decrease your remaining attempts and draw the hangman.

5. **Winning and Losing:**
   - If you guess the word correctly, you win the game!
   - If the hangman is fully drawn before you guess the word, you lose the game.

6. **Playing Again:**
   - After each game, you have the option to play again.

# Requirements

- Python 3.x
- Pygame library (for sound effects)

# How to Run the Game

1. Clone the repository to your local machine.
2. Navigate to the project directory in the terminal.
4. Install requirements.txt (pip install requirements.txt)
3. Run the Python script using the command `python hangman.py`or `python3 hangman.py` depending on your system.

Enjoy the game and have fun!



# Idea: Mindaugas & Vytautas CodeAcademy LT. 
# Code: Renatas, Google, ChatGPT, Gemini, Copilot and others
© Renatas, Utena, LT, 2024. 


## P.S. There are some intentionally hidden mistakes in this code to add more fun for players and developers :) ##
