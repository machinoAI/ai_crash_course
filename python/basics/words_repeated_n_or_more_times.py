# Find all words that appear N or more times in a comma-separated text
#
# Input:  "cat,bat,latt,cat,mat,latt,cat,hat,fat,latt,rat,latt"
# N    :  3
# Output: ['cat', 'latt']  (cat appears 3 times, latt appears 4 times)
#
# Approach: Build a frequency dictionary, then filter keys whose count >= N.

mystring = "cat,bat,latt,cat,mat,latt,cat,hat,fat,latt,rat,latt"
n = 3

counts = {}
for word in mystring.split(","):
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

word_list = [key for key in counts if counts[key] >= n]

if word_list:
    print(word_list)
else:
    print("NA")

# Output: ['cat', 'latt']
