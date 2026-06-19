
def seq_even_generator(nums):

    for item in nums:
        if item%2==0:
           yield item ** 2


nums = [1,2,3,4,5,6]
print(list(seq_even_generator(nums)))