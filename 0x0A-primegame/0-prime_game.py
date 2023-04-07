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
    '''
    x = number of picks
    nums = array of numbers
    '''
    Maria = 0
    Ben = 0
    if (x < 1 or x != len(nums)):
        return None
    for n in nums:
        winner = primeGame(n)
        if winner == 1:
            Maria += 1
        elif winner == 2:
            Ben += 1
    if Maria == Ben:
        return None
    elif Maria > Ben:
        return "Maria"
    return "Ben"


def primeGame(n):
    """
    Determines the winner of a single round of the Prime Game
    """
    if (n < 1):
        return None
    if (n == 1):
        return (2)
    numbers = list(range(n + 1))
    player = 1
    prime = 2
    primes_used = []
    for num in numbers:
        if (num % prime == 0):
            numbers.remove(num)
    primes_used.append(prime)
    prime = 3
    while (numbers != [1]):
        if (player == 1):
            player = 2
        else:
            player = 1
        for num in numbers:
            if (num % prime == 0):
                numbers.remove(num)
        primes_used.append(prime)
        prime += 2
        flag = 1
        while (flag):
            for num in primes_used:
                if (prime % num == 0):
                    prime += 2
                    break
            else:
                flag = 0
    if (player == 1):
        return 1
    return 2
