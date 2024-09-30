#!/usr/bin/python3
"""Module defining is_winner function for the prime game."""


def is_winner(x, nums):
    """Function to determine who won the most rounds in the prime game."""
    if x == 0 or not nums:
        return None

    # Precompute primes up to the maximum possible n (10,000)
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins_count = 0
    ben_wins_count = 0

    # Iterate over each game round
    for num in nums:
        # Count of prime numbers in the current round
        prime_count = sum(primes[1:num + 1])

        # Maria wins if the count of primes is odd, Ben wins if it's even
        if prime_count % 2 == 1:
            maria_wins_count += 1
        else:
            ben_wins_count += 1

    # Determine the overall winner
    if maria_wins_count > ben_wins_count:
        return "Maria"
    elif ben_wins_count > maria_wins_count:
        return "Ben"
    else:
        return None


def sieve_of_eratosthenes(n):
    """Returns a list indicating prime numbers up to n using the Sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    p = 2

    while (p * p) <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1

    return sieve
