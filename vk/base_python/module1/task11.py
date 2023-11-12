PUNCT = '!,.?;:#$%^&*(),'

text = input()

text = ''.join(ch for ch in text if ch not in PUNCT).lower().split()
res = set()
for word in text:
    if len(word) >= 5 and text.count(word) > 2 and len(set(word)) >= 4:
        res.add(word)

res = list(res)
res.sort()
print(*res, sep='\n')
