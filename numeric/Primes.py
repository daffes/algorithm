def primeFactors(n):
    """
    Returns all prime factors of n
    Complexity: O(sqrt(n))
    Test: SRM 617 Div 2 Hard
    """
    i = 2
    while i * i <= n:
        while n % i == 0:
            yield i
            n /= i
        i += 1
    if n > 1:
        yield n

import unittest
class Test(unittest.TestCase):
    def testPrimeFactors(self):
        primes = list(primeFactors(2 * 3 * 11 * 7 * 7 * 19))
        self.assertEqual(primes, [2, 3, 7, 7, 11, 19])
        primes = list(primeFactors(1))
        self.assertEqual(primes, [])

if __name__ == '__main__':
    unittest.main()
