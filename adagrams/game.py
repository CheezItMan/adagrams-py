import random

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    available_letters = []
    for letter, count in LETTER_POOL.items():
        for i in range(count):
            available_letters.append(letter)

    hand = []
    for i in range(10):
        index = random.randint(0, len(available_letters) -1)
        hand.append(available_letters.pop(index))

    return hand


def uses_available_letters(word, letter_bank):
    frequency_count = {}
    for letter in letter_bank:
        if frequency_count.get(letter):
            frequency_count[letter] += 1
        else: 
            frequency_count[letter] = 1
    
    for letter in word:
        if frequency_count.get(letter) == 0 \
             or frequency_count.get(letter) == None:
            return False
        else:
            frequency_count[letter] -= 1

    return True

def score_word(word):
    LETTER_SCORES = {
        'A': 1,
        'E': 1,
        'I': 1,
        'O': 1,
        'U': 1,
        'L': 1,
        'N': 1,
        'R': 1,
        'S': 1,
        'T': 1,
        'D': 2,
        'G': 2,
        'B': 3,
        'C': 3,
        'M': 3,
        'P': 3,
        'F': 4,
        'H': 4,
        'V': 4,
        'W': 4,
        'Y': 4,
        'K': 5,
        'J': 8,
        'X': 8,
        'Q': 10,
        'Z': 10,
    }

    total_score = 0
    for letter in word:
        if LETTER_SCORES.get(letter.upper()):
            total_score += LETTER_SCORES[letter.upper()]
        else:
            raise ValueError(f'invalid letter {letter} in {word}')
    
    if len(word) >= 7 and len(word) <= 10:
        total_score += 8
    return total_score
        

def get_highest_word_score(word_list):
    pass