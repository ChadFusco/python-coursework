"""
Author: Chad Fusco
Description: A program that defines and demonstrates a class of Book objects having at least three
functions useful for handling the text content of books.
Tested with /users/abrick/resources/urantia.txt
Date: 2022-05-05
Version: 1.0
"""

import sys, re, random

# ----CREATE A CLASS CALLED TEXT---
# There are many possible subclasses of texts - i.e. books, poems, emails.
# This class serves to take the filepath and open and read the file as a string.
class text():
    def __init__(self, filepath):
        # Lines below open text file and catch exceptions in this process.
        try:
            self.file = open(filepath)
        except FileNotFoundError:
            print('File not found.')
            exit()
        except PermissionError:
            print('File not readable (permissions error)')
            exit()
        try:
            self.filetext = self.file.read()
        except UnicodeDecodeError:
            print ('File is not in UTF-8.')
            exit()
        self.file.close()

# ----CREATE A SUBCLASS OF TEXT CALLED BOOK----
class book(text):

    def __init__(self, filename):
        super().__init__(filename)
        # Number of characters in book object
        self.chars = len(self.filetext)

    # Method to print the number of characters in the book
    def charsNum(self):
        print(f"\nThe number of characters in the book is: {book1.chars:,}")

    # Method to split the book into words
    def words(self):
        words = list()
        rawWords = re.split('[^a-zA-Z]',self.filetext.lower())
        for i in range(len(rawWords)):
            # Convert possessive nouns ending in "'s" to non-possessive form,
            # convert to lowercase, and add to list.
            # Effect is that later on, string pairs such as "he's" and "he" will be counted once.
            if len(rawWords[i]) > 2 and rawWords[i][-2:] == "'s": words.append(rawWords[i][:-2].lower())
            # Remove words containing digits, convert to lowercase, and add to list.
            elif not any(map(str.isdigit,rawWords[i])): words.append(rawWords[i].lower())
        return words

    # Method to count the number of words in the book.
    def wordNum(self):
        wordsCount = len(self.words())
        print(f"\nThe number of words in the book is: {wordsCount:,}")

    # Method to create a set of unique words in the book.
    def uniqWords(self):
        return set(self.words())

    # Method to count the number of unique words in the book.
    def uniqWordNum(self):
        uniqWordCount = len(self.uniqWords())
        print(f"\nThe number of unique words in the book is: {uniqWordCount:,}")

    # Method to print specified number of distinct random words
    # all over specified number of characters long
    def uniqWordsSamp(self, minChars=10, uniqWordNum=10):
        try:
            longWords = [word for word in self.uniqWords() if len(word) >= minChars]
            uniqWordsSample = random.sample(longWords,uniqWordNum)
            print(f'\n{uniqWordNum} distinct words sampled from book with length > {minChars-1} characters:')
            print('   ',*uniqWordsSample)
        except ValueError:
            print(f'\nThere are fewer than ten district words with length greater than {minChars-1} characters')
            print('Please enter a smaller minimum word length as the 2nd command line argument.')

    # Method to print the greatest integer in the book 
    def greatestInt(self):
        # Subpattern to signal the end of the full expression. To capture integers in decimal form,
        # it consists of zero or one period, followed by zero or more 0s, followed by one character
        # that is not 1-9 or period.
        endPat = r'\.?0*[^1-9.]'
        # PATTERN TO CAPTURE INTEGERS THAT HAVE COMMAS AS THOUSAND SEPARATORS.
        # Pattern below is zero or one dash (for negative numbers), followed by 1-3 digits,
        # followed by one more subpatterns of a comma followed by 3 digits.
        comPat = r'(-?[0-9]{1,3}(?:,[0-9]{3})+)' + endPat
        # PATTERN TO CAPTURE INTEGERS THAT DO NOT HAVE COMMAS AS THOUSAND SEPARATORS.
        # Pattern below is zero or one dash (for negative numbers), followed by one or more digits.
        # Pattern starts with a negative lookbehind assertion to ensure digits are not extracted
        # from floating point numbers
        noComPat = r'(?<!\.)(-?[0-9]+)' + endPat
        # Search the whole text string using the "comma" expression, and then replace all commas
        # with an empty string.
        comIntList = [int(s.replace(',','')) for s in re.findall(comPat,self.filetext)]
        # Search the whole text string using the "no comma" expression
        noComIntList = [int(s) for s in re.findall(noComPat,self.filetext)]
        # Combining the two lists
        intList = comIntList + noComIntList

        print(f'\nThe single greatest integer in the book is {max(intList):,}')

# ----CREATE BOOK OBJECT FROM COMMAND LINE ARGUMENTS----
try:
    book1 = book(sys.argv[1])
except IndexError:
    print('No filename passed. Please enter a filename as the command argument.\
        \nSuggestion: /users/abrick/resources/urantia.txt')
    exit()

# ----OUTPUT----
print("\nThe provided filepath is:", sys.argv[1])
# Print number of characters
book1.charsNum()
# Print number of words
book1.wordNum()
# Print number of unique words
book1.uniqWordNum()
# Print sample of "uniqWordNum" of unique words all at least "userMinChars" long
book1.uniqWordsSamp(minChars=19,uniqWordNum=6)
# Print the greatest integer in the book
book1.greatestInt()
print("\033[96m {}\033[00m".format("\n    It's been a pleasure \
being in this class with you! Thanks"))
