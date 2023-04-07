#!/usr/bin/python3


"""
Prime Game
"""


def is_prime(n):
    '''Check if a number picked is prime'''

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def delete_nums(n, nums):
    '''delete numbers by assigning it to zero'''

    for i in range(len(nums)):
        if nums[i] % n == 0:
            nums[i] = 0


def isWinner(x, nums):
    '''
    x = number of picks
    nums = array of numbers
    '''

    nums.sort()
    winner = False
    Maria = 0
    Ben = 0

    nums.sort()
    winner = False
    Maria = 0
    Ben = 0
    for game in range(x):
        # print("game# ", game+1)
        nums2 = list(range(1, nums[game] + 1))
        # print("nums: ", nums2)
        turn = 0
        while True:
            """
            # uncomment to monitor turns
            if turn % 2 != 0:
                print("Ben turn ")
            else:
                print("Maria turn ")
            """
            change = False
            for i, n in enumerate(nums2):
                # print("n: ", n, "i: ", i)
                if n > 1 and is_prime(n):
                    delete_nums(n, nums2)
                    change = True
                    turn += 1
                    break
            # print("movement: ", nums2)
            if change is False:
                break
        if turn % 2 != 0:
            Maria += 1
        else:
            Ben += 1
        # print("Maria: {}, Ben: {}".format(Maria, Ben))
    if Maria == Ben:
        return None
    if Maria > Ben:
        return "Maria"
    return "Ben"
