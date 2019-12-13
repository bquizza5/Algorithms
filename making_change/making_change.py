#!/usr/bin/python

import sys

def making_change(amount, denominations):
  cache = [0] * (amount + 1)
  cache[0] = 1
  for coin in denominations:
    for higher_amount in range(coin, amount+1):
      cache[higher_amount] += cache[higher_amount - coin]

  return cache[amount]

print(making_change(200, [1, 5, 10, 25, 50]))

# def making_change(amount, denominations):
#   if denominations[amount] == 0:

#     if amount < 5:
#       return 1
#     elif amount > 4 and amount < 10:
#       return 2
#     elif amount > 9 and amount < 15:
#       return 4
#     elif amount > 14 and amount < 20:
#       return 6
#     else:
#       denominations[amount] = (making_change(amount-5, denominations) + making_change(amount-5, denominations) - making_change(amount-10, denominations) + 1)
#       return (making_change(amount-5, denominations) + making_change(amount-5, denominations) - making_change(amount-10, denominations) + 1)
#   else:
#     return denominations[amount]

# print(making_change(5, [0 for i in range(201)]))
# print(making_change(10, [0 for i in range(201)]))
# print(making_change(15, [0 for i in range(201)]))
# print(making_change(20, [0 for i in range(201)]))
# print(making_change(25, [0 for i in range(201)]))
# print(making_change(30, [0 for i in range(201)]))
# print(making_change(35, [0 for i in range(201)]))
# print(making_change(40, [0 for i in range(201)]))
# print(making_change(45, [0 for i in range(201)]))
# print(50,making_change(50, [0 for i in range(201)]))
# print(55,making_change(55, [0 for i in range(201)]))
# print(60, making_change(60, [0 for i in range(201)]))
# print(65, making_change(65, [0 for i in range(201)]))



# if __name__ == "__main__":
#   # Test our your implementation from the command line
#   # with `python making_change.py [amount]` with different amounts
#   if len(sys.argv) > 1:
#     denominations = [1, 5, 10, 25, 50]
#     amount = int(sys.argv[1])
#     print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
#   else:
#     print("Usage: making_change.py [amount]")