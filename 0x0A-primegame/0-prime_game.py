#!/usr/bin/python3


"""
Prime Game
"""


def isWinner(x, nums):
    '''
    x = pick
    nums = list of integers left to pick from
    '''
    def isPrime(n):
        '''check if picked number is prime'''
        if n <= 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def playGame(nums, player):
        '''who plays?'''
        if not any(isPrime(n) for n in nums):
            return player

        for n in nums:
            if isPrime(n):
                newNums = [i for i in nums if i % n != 0]
                to_play = "Maria" if player == "Ben" else "Ben"
                winner = playGame(newNums, to_play)
                if winner == player:
                    return player

        return "Maria" if player == "Ben" else "Ben"

    mariaWins = 0
    benWins = 0

    for n in nums:
        winner = playGame(list(range(1, n+1)), "Maria")
        if winner == "Maria":
            mariaWins += 1
        elif winner == "Ben":
            benWins += 1

    if mariaWins > benWins:
        return "Maria"
    elif benWins > mariaWins:
        return "Ben"
    else:
        return None
