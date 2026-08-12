"""
nums = [2,4,3,6]

output = [0,1,0,2]

    Explanation: 2 is the first element so there is 0 divisor
                - 4 is divisible by 2 so there is only 1 divisor of 2
                - 3 is not divisible by  2 or 4. so 0
                - 6 is divisible by 2 & 3 so-> 2
"""

def find_divisor(nums):

    freq = {}
    result =[]

    for num in nums:
        count = 0

        for d in range(1, int(num**0.5) + 1):
            if num % d == 0:

                count  +=freq.get(d, 0)
                other = num //d

                if other !=d:
                    count +=freq.get(other, 0)

        result.append(count)

        freq[num] = freq.get(num, 0) +1

    return result


nums = [2,4,3,6]
print(find_divisor(nums))