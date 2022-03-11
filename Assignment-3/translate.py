
from __future__ import print_function
from os.path import exists


class Translate:
    dic = {}

    def __init__(self):
        if(exists('db.txt') == False):
            raise Exception("Sorry, database not found")
        dicFile = open("db.txt", "r")
        for line in dicFile.readlines():
            lineSplit = line.split("=")
            if len(lineSplit) > 1:
                self.dic[lineSplit[0]] = lineSplit[1].strip('\n')

    def Start(self):
        while(1):
            self.__setTarget()
            if self.target == "1":
                self.__infinitAdd()
            elif self.target == "2":
                self.__e2p()
            elif self.target == "3":
                self.__p2e()
            elif self.target == "4":
                break

    def __setTarget(self):
        self.target = input(
            '1 - add new word\n2 - translation english2persian\n3 - translation persian2english\n4 - exit\nenter your target: ')

    def __infinitAdd(self):
        with open('db.txt', "a") as fileHandle:
            while(1):
                newWords = raw_input(
                    "sample ENGLISH=PERSIAN\nAlso use comma to add new word\nuse[!q] to return: ").split(",")
                if(newWords[0] == "!q"):
                    break
                for word in newWords:
                    wordSplit = word.split('=')
                    if len(wordSplit > 2):
                        self.dic[wordSplit[0]] = wordSplit[1]
                        fileHandle.write(word)

    def __e2p(self):
        while(1):
            inpSplitByDot = input(
                '[!q] for return\nenter paragraph fro translate to persian: ').split('.')
            if(inpSplitByDot[0] == "!q"):
                break
            for wordByDot in inpSplitByDot:
                wordBySpace = wordByDot.split(' ')
                for word in wordBySpace:
                    end = ' '
                    if wordBySpace[-1] == word:
                        end = ''

                    if word in self.dic:
                        print(self.dic[word], end=end)
                    else:
                        print(word, end=end)
                if (len(inpSplitByDot) > 1) & (inpSplitByDot[-1] != wordByDot):
                    print('.', end='')
            print()

    def __p2e(self):
        while(1):
            inpSplitByDot = input(
                '[!q] for return\nenter paragraph fro translate to english: ').split('.')
            if(inpSplitByDot[0] == "!q"):
                break
            for wordByDot in inpSplitByDot:
                wordBySpace = wordByDot.split(' ')
                for word in wordBySpace:
                    end = ' '
                    if wordBySpace[-1] == word:
                        end = ''

                    if word in self.dic.values():
                        print(list(self.dic.keys())[
                              list(self.dic.values()).index(word)], end=end)
                    else:
                        print(word, end=end)
                if (len(inpSplitByDot) > 1) & (inpSplitByDot[-1] != wordByDot):
                    print('.', end='')
            print()


translate = Translate()
translate.Start()
