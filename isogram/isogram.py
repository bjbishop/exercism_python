def is_isogram(phrase):
    phrase = phrase.lower()
    if len(phrase) == 0:
        return True
    phrase_as_list = list(phrase)
    for char in phrase_as_list:
        if not char.isalpha():
            phrase_as_list.remove(char)
    phrase_as_set = set(phrase_as_list)
    return len(phrase_as_list) == len(phrase_as_set)
