import random


def get_random_word(wordlist="/usr/share/dict/words"):
    good_words = []
    with open(wordlist) as f:
        words = [x.strip() for x in f]
        for word in words:
            if not word.islower(): # if it is a proper noun
                continue
            if not word.isalpha(): # if there is punctuation
                continue
            if len(word) < 5: # Too short
                continue
            good_words.append(word)
    unmasked = random.choice(good_words)
    return unmasked