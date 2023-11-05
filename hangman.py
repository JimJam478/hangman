import random


def get_random_word(wordlist="/usr/share/dict/words"):
    good_words = []
    with open(wordlist) as f:
        words = [x.strip() for x in f]
        for word in words:
            if not word.islower(): 
                continue
            if not word.isalpha(): 
                continue
            if len(word) < 5: 
                continue
            good_words.append(word)
    unmasked = random.choice(good_words)
    return unmasked

def get_masked_word(word,guesses):
    ret = []
    for i in word:
        if i in guesses:
            ret.append(i)
        else:
            ret.append("-")
    return "".join(ret)

def get_status(word, tries_remaining, guesses):
    masked_word = get_masked_word(word,guesses)
    guesses = "".join(guesses)
    return f"""Secret word : {masked_word}
    turns remaining : {tries_remaining}
    guessed letters : {guesses}"""

def run_gameplay(word,guesses,guess,tries_remaining):
    if guess in guesses and guess.isalpha():
        guesses = "".join(guesses)
        return guesses, tries_remaining,"next"
    guesses.append(guess)
    guesses = "".join(guesses)
    if guess in word and tries_remaining >= 1:
        if "-" not in get_masked_word(word,guesses):
            return guesses,tries_remaining,"game won"
        else:
            return guesses,tries_remaining,"next"
    
    elif tries_remaining > 1 :
        tries_remaining -= 1
        return guesses,tries_remaining,"next"
    
    else:
        tries_remaining -= 1
        return guesses,tries_remaining,"game lost"



    