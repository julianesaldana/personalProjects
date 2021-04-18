from generators.generating_words import *

from generators.generating_sentences import *


class EasyEnemy:
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.time = 10
        self.damage = 10
        self.word = One()

    def gainHP(self, amount):
        self.hp += amount

    def hitFor(self, damage):
        self.hp -= damage

    def generateNewWord(self):
        self.word = One()


class MediumEnemy:
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.time = 10
        self.damage = 10
        self.word = Two()

    def gainHP(self, amount):
        self.hp += amount

    def hitFor(self, damage):
        self.hp -= damage

    def generateNewWord(self):
        self.word = Two()


class HardEnemy:
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.time = 10
        self.damage = 10
        self.word = Three()

    def gainHP(self, amount):
        self.hp += amount

    def hitFor(self, damage):
        self.hp -= damage

    def generateNewWord(self):
        self.word = Three()


class SuperHardEnemy:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.time = 15
        self.damage = 10
        self.word = Four()

    def gainHP(self, amount):
        self.hp += amount

    def hitFor(self, damage):
        self.hp -= damage

    def generateNewWord(self):
        self.word = Four()


class BossEnemy:
    def __init__(self, name):
        self.name = name
        self.hp = 200
        self.time = 20
        self.damage = 10
        self.word = sentence_generator()

    def gainHP(self, amount):
        self.hp += amount

    def hitFor(self, damage):
        self.hp -= damage

    def generateNewWord(self):
        self.word = sentence_generator()