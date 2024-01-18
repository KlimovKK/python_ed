def counts_max_rep(string):
    char_rep = {}
    max_rep = 0
    for ch in string:
        if ch in char_rep:
            char_rep[ch] += 1
        else:
            char_rep[ch] = 1

        if max_rep < char_rep[ch]:
            max_rep = char_rep[ch]

    return max_rep


line = input()
print(counts_max_rep(line))
