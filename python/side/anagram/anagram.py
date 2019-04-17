def find_anagrams(word, candidates):
    result = []
    l_word = word.lower()
    for k in candidates:
        k_lower = k.lower()
        if sorted(k_lower) == sorted(l_word) and k_lower != l_word:
            result.append(k)
    return result
