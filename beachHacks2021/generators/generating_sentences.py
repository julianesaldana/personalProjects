import random

def sentence_generator():
    names = ["Rei Angelo Amurao","San Pedro", "Kingpin", "Batman","Spiderman", "Noah Jacinto", "Julian Saldana","Superman", "Mekhi Hart Dela Cruz", "Ronald McDonald","Steve Jobs", "Bill Gates", "Donald Trump", "Obama"]

    verbs = ["purchased", "draws","loves","wants","pats","tickles","laughs with", "whacks", "lightly taps", "smacks","stares at","earns","feeds","wafts","befriends","morphs into","jumps on","spins", "saves", "hunts", "fries", "warms up", "freezes", "hugs", "quarrels with","needs"]

    nouns = ["dogs", "cats", "elephants", "planes", "buildings","chickens","cows","humans","trees","houses", "Long Beach", "Calfornia", "CSULB", "LBCC", "ants", "walruses","dolphins","hamburgers",
    "tacos", "waffles", "wasps","chimichangas", "chicken-tenders", "choco-milk","spaghetti","Q-Tips","quesadillas","xylophones","sadndwiches,", "dino nuggies", "jalapenos", "jellies"]

    number = ["one hundred million", "two hundred", "three","one","two","four","five","six","seven","eight","nine","ten","a thousand","zero","infinity","negative one","half",""]

    punctuation = ["!", "?", "...",".",".","."]

    B1 = "Peter Piper picked a peck of pickled peppers."

    B2 = "Betty Botter bought some butter But she said the butter’s bitter." 

    B3 = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"

    B4 = "She sells seashells by the seashore."

    B5 = "How can a clam cram in a clean cream can?"

    B6 = "I scream, you scream, we all scream for ice cream!"

    B7 = "I saw Susie sitting in a shoeshine shop."

    B8 = "Fuzzy Wuzzy was a bear. Fuzzy Wuzzy had no hair."

    B9 = "Can you can a can as a canner can can a can?"

    B10 = "He would chuck, he would, as much as he could, and chuck as much wood"
    
    B11 = "As a woodchuck would if a woodchuck could chuck wood"
    
    B12 = "So it was better Betty Botter bought a bit of better butter."

    B13 = "But a bit of better butter will make my batter better."

    B14 = "If I put it in my batter, it will make my batter bitter."

    B15 = "If Peter Piper picked a peck of pickled peppers."

    B16 = "A peck of pickled peppers Peter Piper picked."

    random_sentence_1 = random.choice(names) + " " + random.choice(verbs) + " " + random.choice(number) + " " + random.choice(nouns) + random.choice(punctuation)
    
    random_sentence_2 = random.choice(names) + " " + random.choice(verbs) + " " + random.choice(names) + random.choice(punctuation)

    random_tounge = random.choice([B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16])

    types = [random_sentence_1, random_sentence_2, random_tounge]

    types_string = random.choice(types)
    return types_string
    
Normal_Sentence = sentence_generator()

#print(Normal_Sentence)

