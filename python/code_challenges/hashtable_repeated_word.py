from data_structures.hashtable import Hashtable

def first_repeated_word(string):
    if not string:
        return
    string = string.lower()
    word_list = string.split()
    track_words = []
    for word in word_list:
        if "?" in word or "!" in word or "," in word:
            chars = list(word)
            chars.pop()
            word = "".join(chars)
        if word in track_words:
            return word
        else:
            track_words.append(word)

