"""
You are given an array prices, where prices[i] is the price of a stock on the i-th day.

You may choose one day to buy one stock and choose a different future day to sell that stock.

Return the maximum profit you can achieve.

If no profit is possible, return 0.

prices = [7,1,5,3,6,4]

Output:5

Buy on day 2 at price = 1

Sell on day 5 at price = 6

Profit = 6 - 1 = 5


"""

prices = [7,1,5,3,6,4]

def buy_sell_stock(nums):
    max_profit = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            profit = nums[j] - nums[i]
            if profit > max_profit:
                max_profit = profit

    return max_profit

max_profit = buy_sell_stock(prices)
print("Maximum Profit:",max_profit)

# Optimising for O(n) time complexity:

def buy_sell_stock(nums):
    max_profit=0
    min_price=nums[0]
    min_index= 0

    for i, num in enumerate(nums):
        if num<min_price:
            min_price=num
            min_index=i

        profit = num-min_price
        if max_profit < profit:
            max_profit= profit


    return max_profit

prices = [7,1,5,3,6,4]
print(buy_sell_stock(prices))










