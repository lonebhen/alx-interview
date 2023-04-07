#!/usr/bin/python3


"""
Prime Game
"""


# def is_prime(n):
#     '''Check if a number picked is prime'''

#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# def delete_nums(n, nums):
#     '''delete numbers by assigning it to zero'''

#     for i in range(len(nums)):
#         if nums[i] % n == 0:
#             nums[i] = 0


def isWinner(x, nums):
    """Solves Prime Game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not sieve[i]:
            continue
        for j in range(i*i, n + 1, i):
            sieve[j] = False

    sieve[0] = sieve[1] = False
    c = 0
    for i in range(len(sieve)):
        if sieve[i]:
            c += 1
        sieve[i] = c

    winner = ''
    player1 = 0
    for n in nums:
        player1 += sieve[n] % 2 == 1
    if player1 * 2 == len(nums):
        winner = None
    if player1 * 2 > len(nums):
        winner = "Maria"
    else:
        winner = "Ben"
    return winner
