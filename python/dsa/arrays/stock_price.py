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
print("Maximum Profit",max_profit)

# Optimising for O(n) time complexity:



