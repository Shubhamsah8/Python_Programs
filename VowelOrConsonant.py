"""
Method to check the alphabet is vowel or not

Args:
    alphabet (str): Character to check the vowel

Returns:
    return the boolean values
"""


def check_vowel(alphabet):
    vowels = "aeiouAEIOU"

    if alphabet.isalpha() and len(alphabet) == 1:
        if alphabet in vowels:
            return True

    return False


#Taking user input for the alphabet
alphabet = input("Enter the alphabet: ")

if check_vowel(alphabet):
    print("Alphabet is Vowel")
else:
    print("Alphabet is Consonant")
