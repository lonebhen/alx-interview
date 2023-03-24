#!/usr/bin/python3

"""
    Making Change
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.

"""


def makeChange(coins, total):
    '''Making change'''

    if total <= 0:
        return -0

    if coins is None or len(coins) == 0:
        return -1

    change = 0

    all_coins = sorted(coins, reverse=True)

    amount_rem = total

    for coin in all_coins:
        while (amount_rem % coin >= 0 and amount_rem >= coin):
            change += int(amount_rem/coin)
            amount_rem = amount_rem % coin

    change = change if amount_rem == 0 else -1

    return change


# print(makeChange([1, 2, 25], 37))
