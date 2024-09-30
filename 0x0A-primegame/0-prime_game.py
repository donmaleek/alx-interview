#!/usr/bin/python3
"""Module defining isWinner function."""


def is_winner(x, nums):
    """Function to determine who has won in the prime game."""
    if x == 0 or not nums:
        return None

    maria_wins_count = 0
    ben_wins_count = 0

    # Iterate over each game round
    for num in nums:
        rounds_set = list(range(1, num + 1))
        primes_set = primes_in_range(1, num)

        # If no prime numbers exist, Ben wins by default
        if not primes_set:
            ben_wins_count += 1
            continue

        is_maria_turns = True

        while primes_set:
            # Maria and Ben alternate turns; they remove multiples of primes
            smallest_prime = primes_set.pop(0)
            rounds_set.remove(smallest_prime)
            rounds_set = [x for x in rounds_set if x % smallest_prime != 0]

            is_maria_turns = not is_maria_turns

        # Determine who made the last valid move
        if is_maria_turns:
            ben_wins_count += 1
        else:
            maria_wins_count += 1

    # Return the overall winner
    if maria_wins_count > ben_wins_count:
        return "Maria"
    elif ben_wins_count > maria_wins_count:
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
    return [n for n in range(start, end + 1) if is_prime(n)]
