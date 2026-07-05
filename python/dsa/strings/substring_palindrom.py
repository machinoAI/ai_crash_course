def SearchingChallenge(strParam):
    start = 0
    end = 0

    # Starting from middle and stretching like rubber:
    def expand(left, right):
        while left >= 0 and right < len(strParam) and strParam[left] == strParam[right]:
            left -= 1             # Going towards left till -1
            right += 1            # Going towards, right till end

        return left + 1, right - 1   #string between these are palindrome

    for i in range(len(strParam)):

        # Odd palindrome
        l1, r1 = expand(i, i)

        # Even palindrome
        l2, r2 = expand(i, i + 1)

        # comparing the index
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



