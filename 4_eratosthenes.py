def primes(num):
    """ Return list of primes number. """
    sieve = [1] * num
    for i in range(3, int(num ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [0] * ((num - i * i - 1) // (2 * i) + 1)
    return [1, 2] + [i for i in range(3, num, 2) if sieve[i]]


if __name__ == "__main__":
    n = 50
    print(f"Eratosthenes:\n\tinp {n}\n\tout {primes(n)}")