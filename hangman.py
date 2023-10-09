import random
from words import words

def get_valid_word(words):
  word = random.choice(words)
  print("word", word.upper())
  return word.upper()

get_valid_word(words)