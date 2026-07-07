class Solution:
    def buyChoco(self, prices, money):
        prices.sort()

        cost = prices[0] + prices[1]

        if cost <= money:
            return money - cost
        else:
            return money