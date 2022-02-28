# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "KerolosInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time

def linearSearch(anArray, item):
    item.lower()
    for i in range(len(anArray) - 1):
        if item == anArray[i]:
            return i
    return -1

def binarySearch(anArray, item):
    item.lower()
    low = 0
    high = len(anArray) - 1
    while low <= high:
        mid = (high + low) // 2
        if anArray[mid] < item:
            low = mid + 1
        elif anArray[mid] > item:
            high = mid - 1
        else:
            return mid
    return -1

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    kerolosWords = loadWordsFromFile("data-files/KerolosInWonderLand.txt")

    while True:
        print("""
        Main Menu
        1: Spell Check a Word (Linear Search)
        2: Spell Check a Word (Binary Search)
        3: Spell Check Alice In Wonderland (Linear Search)
        4: Spell Check Alice In Wonderland (Binary Search)
        5: Exit
        """)
        input_num = int(input('Enter menu selection (1-5): '))
        if input_num == 1:
            word = input('Please enter a word: ')
            word.lower()
            print('Linear Search starting...')
            start = time.time()
            answer = linearSearch(dictionary, word)
            if answer == -1:
                end = time.time()
                print(f'{word} is not in the dictionary')
                print(f'Time taken: {end-start} seconds')
            else:
                end = time.time()
                print(f'{word} is In the dictionary at position {answer}')
                print(f'Time taken: {end-start} seconds')
        if input_num == 2:
            word = input('Please enter a word: ')
            word.lower()
            print('Binary Search starting...')
            start = time.time()
            answer = binarySearch(dictionary, word)
            if answer == -1:
                end = time.time()
                print(f'{word} is not in the dictionary')
                print(f'Time taken: {end-start} seconds')
            else:
                end = time.time()
                print(f'{word} is In the dictionary at position {answer}')
                print(f'Time taken: {end-start} seconds')
        if input_num == 3:
            print('Linear Search starting...')
            words = 0
            start = time.time()
            for i in range(len(kerolosWords)):
                if linearSearch(dictionary, kerolosWords[i]) == -1:
                    words += 1
            end = time.time()
            print(f'Number of words not found in dictionary: {words}')
            print(f'Time taken: {end-start} seconds')
        if input_num == 4:
            print('Binary Search starting...')
            words = 0
            start = time.time()
            for i in range(len(kerolosWords)):
                if binarySearch(dictionary, kerolosWords[i]) == -1:
                    words += 1
            end = time.time()
            print(f'Number of words not found in dictionary: {words}')
            print(f'Time taken: {end-start} seconds')
        if input_num == 5:
            exit()

# end main()

def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Call main() to begin program
main()
