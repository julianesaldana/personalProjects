from random_word import RandomWords
import random

r = RandomWords()

# Return a single random word
r.get_random_word()
# Random Number
num = random.randint(5, 15)


# print(num) DIAGNOSTIC FOR NUM

# DIFFICULTY # OF RANDOM WORDS, RANDOM LENGTH
def One():
    # Create Easy Enemy
    enemy_easy = r.get_random_words(minCorpusCount = 10, hasDictionaryDef ="True", minLength=15, maxLength=20, sortBy="alpha", sortOrder="asc", limit=1)

    if enemy_easy is None:
      enemy_easy = r.get_random_words(minCorpusCount = 10, hasDictionaryDef ="True", minLength=15, maxLength=20, sortBy="alpha", sortOrder="asc", limit=2)
    
    # Added random to pick from the list in enemy hard with a min of 0 and max of 3
    # print(enemy_easy)
    enemy_easy_word = enemy_easy[0]
    return enemy_easy_word


def Two():
    # Create Medium Enemy
    enemy_med = r.get_random_words(minCorpusCount = 10, hasDictionaryDef ="True", minLength=7, maxLength=12, sortBy="alpha", sortOrder="asc", limit=2)

    # Check if enemy_med return nothing
    if enemy_med is None:
        enemy_med = r.get_random_words(minCorpusCount = 10, hasDictionaryDef ="True", minLength=7, maxLength=12, sortBy="alpha", sortOrder="asc", limit=2)

    # print(enemy_med)

    # Roll to pick between 0, 5
    med_num_1 = random.randint(0, 2 - 1)
    med_num_2 = random.randint(0, 2 - 1)

    # print(med_num_1)
    # print(med_num_2)

    # Set a loop to check if both words will be the same, if they are the same keep it rolling until they are different
    while True:
        if med_num_1 != med_num_2:
            enemy__med_word = enemy_med[med_num_1] + " " + enemy_med[med_num_2]
            return enemy__med_word

        else:
            med_num_1 = random.randint(0, 2 - 1)
            med_num_2 = random.randint(0, 2 - 1)


def Three():
    # Create Hard Enemy
    enemy_hard = r.get_random_words(minCorpusCount = 10, hasDictionaryDef ="True", minLength=6, maxLength=6, sortBy="alpha", sortOrder="asc", limit=3)

    if enemy_hard is None:
        enemy_hard = r.get_random_words(minCorpusCount = 10, hasDictionaryDef ="True", minLength=6, maxLength=6, sortBy="alpha", sortOrder="asc",limit=3)

    # print(enemy_hard)
    # Added random to pick from the list in enemy hard with a min of 10 and max of 15
    hard_num_1 = random.randint(0, 3 - 1)
    hard_num_2 = random.randint(0, 3 - 1)
    hard_num_3 = random.randint(0, 3 - 1)

    # print(hard_num_1)
    # print(hard_num_2)
    # print(hard_num_3)

    while True:
        if hard_num_1 == hard_num_2:
            hard_num_1 = random.randint(0, 3 - 1)
            hard_num_2 = random.randint(0, 3 - 1)
        elif hard_num_1 == hard_num_3:
            hard_num_1 = random.randint(0, 3 - 1)
            hard_num_3 = random.randint(0, 3 - 1)
        elif hard_num_2 == hard_num_3:
            hard_num_2 = random.randint(0, 3 - 1)
            hard_num_3 = random.randint(0, 3 - 1)

        if hard_num_1 != hard_num_2 and hard_num_1 != hard_num_3:
            if hard_num_2 != hard_num_3:
                enemy__hard_word = enemy_hard[hard_num_1] + " " + enemy_hard[hard_num_2] + " " + enemy_hard[hard_num_3]
                return enemy__hard_word


def Four():
    Super_hard_enemy = r.get_random_words(minCorpusCount = 10, hasDictionaryDef ="True", minLength=4, maxLength=4, sortBy="alpha", sortOrder="asc",
                                                      limit=4)

    if Super_hard_enemy is None:
        Super_hard_enemy = r.get_random_words(minCorpusCount = 10, hasDictionaryDef ="True", minLength=4, maxLength=4, sortBy="alpha", sortOrder="asc",
                                                          limit=4)

    # print(Super_hard_enemy)

    super_hard_num_1 = random.randint(0, 4 - 1)
    super_hard_num_2 = random.randint(0, 4 - 1)
    super_hard_num_3 = random.randint(0, 4 - 1)
    super_hard_num_4 = random.randint(0, 4 - 1)

    # print(super_hard_num_1)
    # print(super_hard_num_2)
    # print(super_hard_num_3)
    # print(super_hard_num_4)

    while True:
        if super_hard_num_1 == super_hard_num_2:
            super_hard_num_1 = random.randint(0, 4 - 1)
            super_hard_num_2 = random.randint(0, 4 - 1)

        elif super_hard_num_1 == super_hard_num_3:
            super_hard_num_1 = random.randint(0, 4 - 1)
            super_hard_num_3 = random.randint(0, 4 - 1)

        elif super_hard_num_1 == super_hard_num_4:
            super_hard_num_1 = random.randint(0, 4 - 1)
            super_hard_num_4 = random.randint(0, 4 - 1)

        elif super_hard_num_2 == super_hard_num_3:
            super_hard_num_2 = random.randint(0, 4 - 1)
            super_hard_num_3 = random.randint(0, 4 - 1)

        elif super_hard_num_2 == super_hard_num_4:
            super_hard_num_2 = random.randint(0, 4 - 1)
            super_hard_num_4 = random.randint(0, 4 - 1)

        elif super_hard_num_4 == super_hard_num_3:
            super_hard_num_3 = random.randint(0, 4 - 1)
            super_hard_num_4 = random.randint(0, 4 - 1)

        if super_hard_num_1 != super_hard_num_2 and super_hard_num_1 != super_hard_num_3 and super_hard_num_1 != super_hard_num_4:
            if super_hard_num_2 != super_hard_num_3 and super_hard_num_2 != super_hard_num_4:
                if super_hard_num_4 != super_hard_num_3:
                    Super_hard_enemy_word = Super_hard_enemy[super_hard_num_1] + " " + Super_hard_enemy[
                        super_hard_num_2] + " " + Super_hard_enemy[super_hard_num_3] + " " + Super_hard_enemy[
                                                super_hard_num_4]
                    return Super_hard_enemy_word


def reverse(words):
    split = words.split()

    new_str = ' '
    list = []

    i = len(split) - 1
    # Last index of the list
    while i >= 0:
        list.append(split[i])
        i -= 1
    new_str = new_str.join(list)

    return new_str


def reverse2(words):
    length = len(words)
    reversed_string = []
    reversed_string = ''
    index = length
    while index > 0:
        reversed_string += words[index - 1]
        reversed_string.join(words[index - 1])
        index -= 1
    return str(reversed_string)


def Main():
  Easy_Word = One()
  print(Easy_Word)
  Medium_Word = Two()
  print(Medium_Word)
  Hard_Word = Three()
  print(Hard_Word)
  Super_Hard = Four()
  print(Super_Hard)

#     Easy_Word_Reversed = reverse(reverse2(Easy_Word))
#     print(Easy_Word_Reversed)
#     Medium_Word_Reversed = reverse(reverse2(Medium_Word))
#     print(Medium_Word_Reversed)
#
#     Hard_Word_Reversed = reverse(reverse2(Hard_Word))
#
#     print(Hard_Word_Reversed)
#
#     Super_Hard_Reversed = reverse(reverse2(Super_Hard))
#
#     print(Super_Hard_Reversed)
#
#
#Main()
