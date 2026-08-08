
words = ["eat", "tea", "tan", "ate"]
Output = [["eat", "tea", "ate"], ["tan"]]


def calculate_anagram(words):

    groups = {}

    for word in words:

        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)


    return list(groups.values())


print(calculate_anagram(words))


# Using Defaultdict

from collections import defaultdict

groups = defaultdict(list)

for word in words:
    key = ''.join(sorted(word))
    groups[key].append(word)

print(list(groups.values()))



# You can avoid sorting by using a 26-character frequency tuple as the key:

from collections import defaultdict

groups = defaultdict(list)

for word in words:
    count = [0] * 26

    for ch in word:
        count[ord(ch) - ord('a')] += 1

    groups[tuple(count)].append(word)

print(list(groups.values()))