def char_by_char_concatenation(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    max_len = max(len1, len2)

    i = 0
    word3 = ""
    while i < max_len:
        if i < len1:
            word3 = word3 + word1[i]
        if i < len2:
            word3 = word3 + word2[i]
        i += 1
    return word3


print(char_by_char_concatenation("asdf", "qwert"))