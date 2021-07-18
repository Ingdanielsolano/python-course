import os
import platform
import random
from functools import reduce


def getLineCounter(file):
    lineCounter = 0
    for line in file:
        if line != "\n":
            lineCounter += 1
    return lineCounter


def chooseWord():

    f = open("./data.txt", "r", encoding="utf-8")
    lines = f.readlines()

    randomNumber = random.randint(0, len(lines))
    print(randomNumber)

    return lines[randomNumber]


def run():
    choosenWord = chooseWord()
    choosenWord = list(filter(lambda letter: letter != "\n", choosenWord))
    choosenWordArray = [{"letter": i, "got": False} for i in choosenWord]
    print("System")
    print(os.name)

    def missingLetters(): return list(
        filter(lambda letter: letter["got"], choosenWordArray))

    def isThereMissingLetters(actualArray): return len(
        list(filter(lambda letter: not letter["got"], actualArray))) > 0

    def formatSentence(actualWordArray): return reduce(
        lambda a, b: a+b, [i["letter"] if i["got"] else " _ " for i in actualWordArray])

    print(isThereMissingLetters(choosenWordArray))

    while isThereMissingLetters(choosenWordArray):
        print("Guess the word!")
        formattedSentence = formatSentence(choosenWordArray)
        print(formattedSentence)
        inputWord = input("Input some letter: ")
        choosenWordArray = list(map(lambda word: {
                                "letter": word["letter"], "got": word["got"] or word["letter"] == inputWord}, choosenWordArray))
        print(choosenWordArray)
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
    print(formatSentence(choosenWordArray))


if __name__ == "__main__":
    run()
