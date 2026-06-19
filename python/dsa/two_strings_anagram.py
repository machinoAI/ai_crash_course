def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase for uniform processing
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # If sorted characters match, they are anagrams
    return sorted(str1) == sorted(str2)


print(is_anagram("cl au de", "Claude"))