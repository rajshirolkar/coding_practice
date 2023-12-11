from collections import Counter

chars = "atach"
words = ["cat", "bt", "hat", "tree", "ataa"]


def count_chars(words, chars):
    char_count = Counter(chars)
    for word in words:
        word_count = Counter(word)
        for key in word_count:
            if key not in char_count or word_count[key] > char_count[key]:
                break
        else:
            yield word

goodwords = list(count_chars(words, chars))
ans = 0
for i in goodwords:
    for j in i:
        ans += 1

print(ans)