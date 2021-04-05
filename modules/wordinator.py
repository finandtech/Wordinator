import math

class Wordinator:

    def __init__(self, word):
        self.word = word

    def __lt__(self, other):
        if self.word < other.word:
            return True
        else:
            return False

    def __add__(self, other):
        return (self.word + other.word).title()

    def __str__(self):
        return self.word


    def __mul__(self, factor):
        return (self.word * factor).upper()



    def __len__(self):
        return len(self.word)

    def __truediv__(self, otherWord):
        lenA = len(self.word)
        lenB = len(otherWord.word)

        longWord = ""
        shortWord = ""
        longWordLen = 0
        totalString = ""

        if lenA >= lenB:
            longWordLen = lenA
            longWord = self.word
            shortWord = otherWord.word
        elif lenA <= lenB:
            longWordLen = lenB
            longWord = otherWord.word
            shortWord = self.word

        for i in range(longWordLen):
            if i < len(shortWord):
                totalString += shortWord[i]
            totalString += longWord[i]
        return totalString.title()


    def __divmod__(self, other):






    def switchCaseWords(self):
        switch = ""
        for i in self.word1:
            if i.isupper():
                switch += i.lower()
            else:
                switch += i.upper()
            switch += "\n"
        for i in self.word2:
            if i.isupper():
                switch += i.lower()
            else:
                switch += i.upper()
        return switch




    def backWordSlice(self):
        return self.word[::-1]


    def backWordsManual(self):
        switch = ""
        lenght1 = len(self.word1)
        lenght2 = len(self.word2)
        word = self.word1 + self.word2
        for i in range(len(word) - 1, -1, -1):
            if i == lenght1 - 1:
                switch += "\n"
                switch += self.word1[i]
            elif lenght1 <= i <= lenght1 + lenght2:
                switch += self.word2[i - lenght1]
            else:
                switch += self.word1[i]
        return switch


