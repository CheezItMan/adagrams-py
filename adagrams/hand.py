import random
import copy
#  Build a Hand class

# A Hand will keep track of it's letters
# A hand will be able to:
#   * Draw letters from the letter pool
#   * Be able to tell you if a word uses the available letters

HAND_SIZE = 10

class Hand:
    """ Class to represent a hand of letters in
        the Adagrams game
    """
    def __init__(self, letter_pool):
        self.letters = self.draw_letters(letter_pool)

    def draw_letters(self, letter_pool):
        letter_bank = []
        letters = []
        # Making a list of all the letters in letter_pool
        for letter, count in letter_pool.items():
            for i in range(count):
                letter_bank.append(letter)
                    #  ['A', 'A', 'A'... 'B', B']

        # Plucking out HAND_SIZE letters from the pool
        letters = random.sample( letter_bank, HAND_SIZE  )

        return letters

    def uses_available_letters(self, word):
        letters_copy = self.letters[:]

        for letter in word:
            letter = letter.upper()
            if letter in letters_copy:
                letters_copy.remove(letter)
            else:
                return False
        return True



