import random
from words import words
import string

def get_valid_word(words):
  word = random.choice(words)
  print("word", word.upper())
  return word.upper()

def hangman():
  word = get_valid_word(words)
  word_letter = set(word) #creates a set of letters from the chosen word
  alphabet = set(string.ascii_uppercase) #creates a set of letters from the alphabet
  used_letters = set() #empty set to track used letters
  print(word_letter, "word letter")
  print(alphabet, "alphabet")

get_valid_word(words)
hangman()