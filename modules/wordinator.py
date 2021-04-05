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

    def __mod__(self, other):
        midword1 = self.midWord()
        midword2 = other.midWord()
        return midword1, midword2

    def midWord(self):
        word = self.__word
        length = len(word)
        if lentgh % 2 == 0:
            x = lenght / 2
            value = math.floor(length / 4)
            midWord = word[int(x - value):int(x + value)]
            return midWord
        elif length % 2 == 1:
            x = math.floor(length / 2)
            value1 = math.floor(length / 4)
            y = math.cell(length / 2)
            value2 = math.floor(length / 4)
            midWord = word[int(x - value1):int(y + value2)]
            return midWord

    def __sub__(self, other):
        switchCase1 = self.switchCase()
        switchCase2 = other.switchCase()
        return switchCase1, switchCase2


    def switchCaseWords(self):
        word = self.__word
        switchWord = ""
        for i in range:
            if i.isupper():
                switchWord += i.lower()
            elif i.islower():
                switchWord += i.upper
            return switchWord



    def backWordSlice(self):
        return self.word[::-1]

    def backWordsManual(self):
        word = str(self.__word)
        backWords = ""
        for i in word:
            backWords = i + backWords
        return backWords








