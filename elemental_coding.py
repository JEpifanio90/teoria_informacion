#!/usr/bin/python
# -*- coding: latin-1 -*-
__author__ = 'José Epifanio'
from operator import itemgetter


class ElementalCoding:
    def __init__(self):
        self.compression_ratio = 0

    def processFile(self, text):
        self.chain = ""
        with open(text) as source_file:
            for line in source_file:
                for character in line.lower():
                    self.chain += character
        self.chain = self.chain
        self.originalChainSize = len(self.chain)
        self.codeElemental(self.chain)
        self.compression_ratio = ''

    def codeElemental(self, chain):
        self.chain = chain
        self.originalChainSize = len(self.chain)
        self.dictionary = {}
        self.listOrder = []
        self.listEncoded = []
        self.uncodedList = []
        for element in chain.split():
            self.dictionary[element] = self.dictionary.get(element, 0) + 1
            self.listOrder.append(element)
        for element in self.listOrder:
            # print "Element: ", element, " value: ", dictionary[element]
            self.uncodedList.append(((len(element), self.dictionary[element]), element))
        self.compression_ratio = self.originalChainSize / len(chain)

    def encodeText(self):
        chain = ''
        flag = False
        self.codedList = []
        i = 0
        x = 13
        miniChain = ''
        for key, value in self.uncodedList:
            if i >= 118:
                flag = True
                i = 0
                x += 1
            if flag:
                a = self.listElements[i].upper()
                b = self.listElements[x]
                chain = a + b
            else:
                if len(self.listElements[i]) > 1:
                    Aflag = True
                    for character in self.listElements[i]:
                        if Aflag:
                            miniChain = character.upper()
                            Aflag = False
                        else:
                            miniChain = miniChain + character
                    chain = miniChain
                else:
                    chain = self.listElements[i]
            self.codedList.append((key, chain))
            i += 1

    def printCodedText(self):
        chain = ''
        output = ''
        for key, value in self.codedList:
            # Sprint "Key: ",key," Value: ",value
            chain = chain + value
        output += "\nTexto Codificado: " + chain
        self.compression_ratio = len(chain) / float(self.originalChainSize)
        return output

    def getElementList(self):
        self.listElements = []
        try:
            fp = open("ListOfElements.txt")
        except:
            print "Moviste el .txt de los elementos. Gracias, ahora ya no funciono."
        for line in fp:
            line = line.lower().rstrip()
            self.listElements.append(line)


    def checkCodedText(self):
        dictionary = {}
        for key, value in self.codedList:
            dictionary[value] = dictionary.get(value, 0) + 1
        for key, value in dictionary.items():
            # print "key: ",key,"  value: ",value
            if value != 1:
                print 'Se produjo un error a la hora de la codificación. El valor de ', key, " se repitió ", value, "veces."

    def lookForString(self, word):
        word = word.lower()
        characters = []
        word = word.lstrip().rstrip()
        for character in word:
            characters.append(character)
        self.valuesAndKeySorted = []
        temp = ""
        self.uncodedList = sorted(self.uncodedList, key=itemgetter(1))
        self.uncodedList.reverse()
        output = ''
        listaO = list()
        flag = False
        for key, value in self.uncodedList:
            if key[0] == len(word):
                x = 0
                i = 0
                for character in value:
                    if character == characters[i]:
                        x += 1
                    i += 1
                if value == word:
                    output += "\n->>>" + value
                    listaO.append(output)
                    break
                elif temp != value:
                    print value
                    if len(word) < 2:
                        if x == (len(word) - 1):
                            output += "\n->>" + value
                            listaO.append(output)
                        else:
                            output += "\n->" + value
                            listaO.append(output)
                    else:
                        if x == (len(word) - 1):
                            output += "\n->>" + value
                            listaO.append(output)
                        elif x == (len(word) - 2):
                            output += "\n-> " + value
                            listaO.append(output)
                        elif x == (len(word) - 3):
                            output += "\n-> " + value
                            listaO.append(output)
                        else:
                            '''Códifica'''
                            output += "\n-> " + value
                            listaO.append(output)
                            self.dictionary[word] = self.dictionary.get(word, 0) + 1
                temp = value
            else:
                j = 0
                aciertos = 0
                if len(value) >= len(characters):
                    if temp != value:
                        for char in characters:
                            if char == value[j]:
                                aciertos += 1
                            j += 1
                        print aciertos
                        if aciertos == (len(characters) - 1):
                            output += "\n->>" + value
                            listaO.append(output)
                        elif aciertos == (len(characters) - 2):
                            output += "\n-> " + value
                            listaO.append(output)
                        elif aciertos == (len(characters) - 3):
                            output += "\n-> " + value
                            listaO.append(output)
                        else:
                            if value.startswith(str(word)):
                                output += "\n-> " + value
                                listaO.append(output)
                            elif value.endswith(str(word)):
                                output += "\n-> " + value
                                listaO.append(output)
                            else:
                                output += "\n->0"
                                listaO.append(output)
                        temp = value
            return listaO

    def getCharacterF(self):
        dictionary = {}
        self.characterF = []
        for character in self.chain:
            dictionary[character] = dictionary.get(character, 0) + 1
        for key, value in dictionary.items():
            self.characterF.append((key, value))
        self.characterF = sorted(self.characterF, key=itemgetter(1))

    def get_compression_ratio(self):
        return self.compression_ratio


def main():
    teo = ElementalCoding()
    teo.getElementList()
    # teo.processFile('pagina.txt')
    teo.codeElemental('HOLAAAA')
    teo.encodeText()
    print teo.printCodedText()
    print teo.chain
    teo.checkCodedText()
    #teo.lookForString(raw_input("Give me a word to look: "))
    #teo.getCharacterF()


if __name__ == "__main__":
    main()
