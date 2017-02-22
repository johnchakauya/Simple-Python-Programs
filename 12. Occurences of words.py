''''
Python program by John Chakauya
This is a Python program to count the occurrences of each word in a given sentence.
'''


def word_count(strng):  # function to count the occurrences of each word in a given sentence
    counts = dict()  # creating a dictionary data structure to store each word and its number of occurrences
    words = strng.split()  # using the split method to return a list of all the words in the string or sentence

    for word in words:
        if word in counts:  # if a word which is already in the dictionary reoccurs then increment its occurrence by 1
            counts[word.strip().lower()] += 1
            # words are placed in lower case to ensure similar characters are read regardless of the initial case
        else:
            counts[word.strip().lower()] = 1  # if a new word appears then set its occurrence to 1

    return counts    # return the dictionary with words and their respective number of occurrences

str = 'the quick brown fox jumps over the lazy dog.'
print("Sample sentence: " + str)
print(word_count(str))

print('\nEnter a blank to exit...\n')  # informing the user to enter a blank to exit the program loop

while str != "":   # while loop to allow the user to enter a sentence multiple times
    str = input('Input a sentence to count the occurrences of each words:\n')
    if str != "":
        print(word_count(str))
