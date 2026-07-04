def SearchingChallenge(strParam):
    start = 0
    end = 0

    def expand(left, right):
        while left >= 0 and right < len(strParam) and strParam[left] == strParam[right]:
            left -= 1
            right += 1

        return left + 1, right - 1

    for i in range(len(strParam)):
        l1, r1 = expand(i, i)

        l2, r2 = expand(i, i + 1)

        if r1 - l1 > end - start:
            start, end = l1, r1

        if r2 - l2 > end - start:
            start, end = l2, r2

    return strParam[start:end + 1]


# keep this function call here
challenge_token = "ufkpzynd08c"
reversed_token = challenge_token[::-1]

palindrome = SearchingChallenge(input())
if len(palindrome) <= 2:
    palindrome = "none"
else:
    palindrome = palindrome[::-1]

print(f"{palindrome}:{reversed_token}")



