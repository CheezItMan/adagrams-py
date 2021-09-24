from adagrams.hand import Hand

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
play = True

my_hand = Hand(LETTER_POOL)

# print(my_hand.letters)

print("Welcome to Adagrams!")
print("Lets draw some letters")

while play:
    print(f"Letters = {my_hand.letters}")
    word = input("Give me a word => ")

    if my_hand.uses_available_letters(word):
        print(f"Nice {word} works!")
    else:
        print(f"Sorry {word} does not work")

    cont = input("Do you want to continue Y/N ==> ")
    if cont == "Y":
        play = True
    else:
        play = False