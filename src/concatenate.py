def concatenate(words):
    result = ""
    if not isinstance(words, list):
        raise TypeError("Input must be a list of strings.")

    for i, word in enumerate(words):
        if not isinstance(word, str):
            continue
        if i < len(word):
            result += word[i]
    return result


