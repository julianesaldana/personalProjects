import Levenshtein

def stringCheck(userInput, randomWord):
    ratio = Levenshtein.ratio(userInput, randomWord) # Percent accurate
    player_attack = int(ratio * len(randomWord))

    penalty_points = Levenshtein.distance(userInput, randomWord) # Difference in letters
    
    return [player_attack, penalty_points]
