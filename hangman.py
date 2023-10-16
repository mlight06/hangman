import random
from words import words
import string

def get_valid_word(words):
  word = random.choice(words)
  print("word", word.upper())
  return word.upper()

def hangman():
  word = get_valid_word(words)
  word_letters = set(word) #creates a set of letters from the chosen word
  alphabet = set(string.ascii_uppercase) #creates a set of letters from the alphabet
  used_letters = set() #empty set to track used letters
  print(word_letters, "word letter")
  # print(alphabet, "alphabet")
  while len(word_letters) > 0:
    print('You have already used: ', ' '.join(used_letters))

    word_list = [letter if letter in used_letters else '-' for letter in word]

    print('Current word:', ' '.join(word_list))
    user_letter = input("Guess a letter:").upper()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
    elif user_letter in used_letters:
      print("You've already used this letter. Please make another guess")
    else:
      print("Invalid character")
  print("Congratulations, you've guessed the word!")

hangman()