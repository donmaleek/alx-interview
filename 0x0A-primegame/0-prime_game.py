#!/usr/bin/python3
"""Module defining isWinner function."""

def isWinner(x, nums):
    """Function to get who has won in prime game"""
    if x == 0 or not nums:
        return None

    mariaWinsCount = 0
    benWinsCount = 0

    # Iterate over each game round
    for num in nums:
        roundsSet = list(range(1, num + 1))
        primesSet = primes_in_range(1, num)

        # If no prime numbers exist, Ben wins by default
        if not primesSet:
            benWinsCount += 1
            continue

        isMariaTurns = True

        while primesSet:
            # Maria and Ben alternate turns; they remove multiples of primes
            smallestPrime = primesSet.pop(0)
            roundsSet.remove(smallestPrime)
            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]

            isMariaTurns = not isMariaTurns

        # Determine who made the last valid move
        if isMariaTurns:
            benWinsCount += 1
        else:
            mariaWinsCount += 1

    # Return the overall winner
    if mariaWinsCount > benWinsCount:
        return "Maria"
    elif benWinsCount > mariaWinsCount:
        return "Ben"
    else:
        return None


def is_prime(n):
    """Returns True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """Returns a list of prime numbers between start and end (inclusive)."""
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    return primes
