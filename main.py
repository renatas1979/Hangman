import os
import random
from typing import List
import time
import pygame

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")
clear_screen()

def draw_hanger(failed_attempts: int) -> str:
    hanger_parts = [
        [
            "   ____________",
            "  |           |",
            "  |",
            "  |",
            "  |",
            "  |",
            "  |",
            "----",
        ],
        [
            "   ____________",
            "  |           |",
            "  |           O",
            "  |",
            "  |",
            "  |",
            "  |",
            "----",
        ],
        [
            "   ____________",
            "  |           |",
            "  |           O",
            "  |           |",
            "  |",
            "  |",
            "  |",
            "----",
        ],
        [
            "   ____________",
            "  |           |",
            "  |           O",
            "  |          /|",
            "  |",
            "  |",
            "  |",
            "----",
        ],
        [
            "   ____________",
            "  |           |",
            "  |           O",
            "  |          /|\\",
            "  |",
            "  |",
            "  |",
            "----",
        ],
        [
            "   ____________",
            "  |           |",
            "  |           O",
            "  |          /|\\",
            "  |          /",
            "  |",
            "  |",
            "----",
        ],
        [
            "   ____________",
            "  |           |",
            "  |           O",
            "  |          /|\\",
            "  |          / \\",
            "  |",
            "  |",
            "----",
        ],
    ]
    if failed_attempts < len(hanger_parts):  
        time.sleep(1)
        clear_screen()
        return "\n".join(hanger_parts[failed_attempts])
    else:
        return "Game over"

def choose_word(language: str) -> str:
    folder_path = 'words_lists'
    file_name = 'lt_words.txt' if language.lower() == 'lt' else 'en_words.txt'
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.readlines()
    words = [word.strip() for word in words]
    return random.choice(words)

def print_word(word: str, guessed_letters: List[str]) -> str:
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def print_guessed_letters(guessed_letters: List[str]) -> str:
    return "Guessed letters: " + ", ".join(guessed_letters)

def game_logic() -> None:
    print("Welcome to a Hangman game !")
    max_wrong_guesses: int = 6
    max_guesses: int = 10

    while True:
        language = input("Choose a language (lt for Lithuanian, en for English): ")
        if language.lower() not in ['lt', 'en']:
            print("Invalid choice. Please enter 'lt' for Lithuanian or 'en' for English.")
            continue

        word: str = choose_word(language)
        correct_guesses: List[str] = []
        wrong_guesses: List[str] = []
        guesses_left: int = max_guesses

        while len(wrong_guesses) < max_wrong_guesses and guesses_left > 0:
            print(draw_hanger(len(wrong_guesses)))  
            print(print_guessed_letters(correct_guesses + wrong_guesses))
            print("Word:", print_word(word, correct_guesses))
            print(f"You have {guesses_left} guesses left.")
            guess: str = input("Guess a letter or the whole word: ").lower()

            if guess == word:
                print("Congrats! You guessed the word correctly", word)
                pygame.mixer.init()
                pygame.mixer.music.load("sound_effects/win.mp3")  
                pygame.mixer.music.play()
                break
            
           
            elif len(guess) == 1 and guess.isalpha():
                if guess in correct_guesses + wrong_guesses:
                    print("You've already guessed that letter.")
                elif guess in word:
                    print("Correct guess!")
                    guesses_left -= 1
                    correct_guesses.append(guess)
                    if set(word) == set(correct_guesses):
                        break
                else:
                    print("Incorrect guess.")
                    wrong_guesses.append(guess)
                    guesses_left -= 1
            elif len(guess) == len(word) and guess.isalpha():
            
    
                if guess == word:
                    pygame.mixer.init()
                    pygame.mixer.music.load("sound_effects/win.mp3")  
                    pygame.mixer.music.play()
                    
                    print("Congrats! You guessed the word correctly !", word)
                    
                    break
                elif all(letter in word for letter in guess):
                    print("Correct guess!")
                    correct_guesses.extend(guess)
                    if set(word) == set(correct_guesses):
                       

                        print("Congrats! You guessed the word correctly !", word)
                        pygame.mixer.init()
                        pygame.mixer.music.load("sound_effects/win.mp3")  
                        pygame.mixer.music.play()
                        break
                else:
                    print("Incorrect guess. The whole word is not correct.")
                    wrong_guesses.append(guess)
                    guesses_left -= 1
            else:
                print("Invalid input. Please enter a single letter or the whole word.")

        if guess != word and set(word) == set(correct_guesses):    
            print("Congrats! You guessed the word correctly !", word)
            pygame.mixer.init()
            pygame.mixer.music.load("sound_effects/win.mp3")  
            pygame.mixer.music.play()

        elif guess == word:
            pass
        else:
            print(draw_hanger(len(wrong_guesses)))
            pygame.mixer.init()
            pygame.mixer.music.load("sound_effects/lose.mp3")  
            pygame.mixer.music.play()  
            print("Ooops, you didn't guess the word. The word was:", word)

       

        play_again: str = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

        clear_screen()

game_logic()
