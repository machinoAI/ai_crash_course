
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
