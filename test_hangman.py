import os

import hangman

def test_random_word_lowercase():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["Grape\n", "apple\n", "Mango\n"])
        
    for _ in range(100):
        assert hangman.get_random_word(fname) == "apple"

    os.unlink(fname)

def test_random_word_no_punctuation():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["pineapple\n", "mango's\n", '"beryl"'])

    for _ in range(100):
        assert hangman.get_random_word(fname) == "pineapple"

    os.unlink(fname)

def test_random_word_min_length_5():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["pineapple\n", "ape\n", 'dog\n', 'bear\n'])

    for _ in range(100):
        assert hangman.get_random_word(fname) == "pineapple"
        
    os.unlink(fname)

def test_random_word_no_repeated_words():
    words = {hangman.get_random_word() for _ in range(10)}
    assert len(words) == 10

def test_maskedWord_no_guesses():
    word = "umbrella"
    guesses = []
    masked_word = hangman.get_masked_word(word,guesses)
    assert masked_word == "--------"

def test_maskedWord_oneCorrect_guess():
    word = "universe"
    guesses = ["u"]
    masked_word = hangman.get_masked_word(word,guesses)
    assert masked_word == "u-------"

def test_maskedWord_twoCorrect_guess():
    word = "universe"
    guesses = ["e"]
    masked_word = hangman.get_masked_word(word,guesses)
    assert masked_word == "----e--e"

def test_maskedWord_multipleCorrect_guess():
    word = "universe"
    guesses = ["u","e"]
    masked_word = hangman.get_masked_word(word,guesses)
    assert masked_word == "u---e--e"

def test_display():
    word = "universe"
    guesses = ["i","e","r"]
    tries_remaining = 6
    display = hangman.get_status(word, tries_remaining, guesses)
    assert display == """Secret word : --i-er-e
    turns remaining : 6
    guessed letters : ier"""  

def test_gameRules_correct_input():
    word = "universe"
    guesses = []
    guess = 'u'
    tries_remaining = 6
    
    guesses, tries_remaining,next_action = hangman.run_gameplay(word,guesses,guess,tries_remaining)
    assert tries_remaining == 6
    assert next_action == "next"
    assert guesses == ['u']

def test_gameRules_incorrect_input():
    word = "universe"
    guesses = []
    guess = 'z'
    tries_remaining = 6
    
    guesses, tries_remaining,next_action = hangman.run_gameplay(word,guesses,guess,tries_remaining)
    assert tries_remaining == 5
    assert next_action == "next"
    assert guesses == ['z']

def test_gameRules_correctInput_Final_round():
    word = "universe"
    guesses = ['u','n','i','e','r','s']
    guess = 'v'
    tries_remaining = 6
    
    guesses, tries_remaining,next_action = hangman.run_gameplay(word,guesses,guess,tries_remaining)
    assert tries_remaining == 6
    assert next_action == "game won"
    assert guesses == ['u','n','i','e','r','s','v']

def test_gameRules_incorrectInput_Final_round():
    word = "universe"
    guesses = ['a','b','c','d','f']
    guess = 'z'
    tries_remaining = 1
    
    guesses, tries_remaining,next_action = hangman.run_gameplay(word,guesses,guess,tries_remaining)
    assert tries_remaining == 0
    assert next_action == "game lost"
    assert guesses == ['a','b','c','d','f','z']

def test_gameRules_repeated_input():
    word = "universe"
    guesses = ['u','r']
    guess = 'r'
    tries_remaining = 1
    
    guesses, tries_remaining,next_action = hangman.run_gameplay(word,guesses,guess,tries_remaining)
    assert tries_remaining == 1
    assert next_action == "next"
    assert guesses == ['u','r']

def test_gameRules_non_alphabetic_input():
    word = "universe"
    guesses = ['u','r']
    guess = '%'
    tries_remaining = 1
    
    guesses, tries_remaining,next_action = hangman.run_gameplay(word,guesses,guess,tries_remaining)
    assert tries_remaining == 1
    assert next_action == "next"
    assert guesses == ['u','r']