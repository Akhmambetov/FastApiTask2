from random_word import RandomWords

rw = RandomWords()

def get_random_word(max_len: int = 8) -> str:
    while True:
        word = rw.get_random_word()
        if word and len(word) <= max_len:
            return word