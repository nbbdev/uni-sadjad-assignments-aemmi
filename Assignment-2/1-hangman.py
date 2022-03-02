# -*- coding: utf-8 -*-
import random
import human


class Game:
    START = "💡 enter first the character\n"
    CORRECT = "✅ You guessed one of the characters correctly\n"
    IN_CORRECT = "❌ You made a mistake, your blood decreased\n"
    WIN = "✅ YOU WIN ✅\n"
    LOSE = "‼️ YOU LOSE ‼️\n"

    def __init__(self):
        self.words = ["one", "two", "three", "four",
                      "five", "six", "seven", "eight", "nine", "ten"]
        self.goalWord = 0
        self.wrongCounter = 0
        self.guess = ''

    def start(self):
        self.goalWord = self.words[random.randrange(0, len(self.words))]
        self.wrongCounter = len(human.steps) - 1
        self.guess = ''.ljust(len(self.goalWord), '-')
        self.__gameStatus()
        print(self.START)

        self.__tryForWin()

    def __tryForWin(self):
        while(self.wrongCounter > 0):
            singleInput = raw_input("Your character: ").lower()
            charIndexFound = self.goalWord.find(singleInput)

            if(charIndexFound != -1):
                self.guess = self.guess[:charIndexFound] + \
                    singleInput + self.guess[charIndexFound+1:]
                self.goalWord = self.goalWord[:charIndexFound] + \
                    '-' + self.goalWord[charIndexFound+1:]
            else:
                self.wrongCounter -= 1
            self.__gameStatus()

            if(self.guess.find('-') == -1):
                print(self.WIN)
                break
        if(self.guess.find('-') == 1):
            print(self.LOSE)

    def __gameStatus(self):
        print("\n{wrongCounter}❤️ - Completed words: '{guess}'"
              .format(wrongCounter=self.wrongCounter, guess=self.guess))
        print(human.steps[len(human.steps) - (self.wrongCounter + 1)])


game = Game()

while(1):
    game.start()
    inp = raw_input("You play again? [y]yes [n]no: ").lower()
    if(inp == 'n'):
        print("good luck")
        break
