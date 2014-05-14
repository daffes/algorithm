from Primes import primeFactors

def eulerTotient(n):
    primes = list(set(primeFactors(n)))
    for p in primes:
        n -= n/p
    return n

import unittest
class Test(unittest.TestCase):
    def testEulerTotient(self):
        self.assertEquals(eulerTotient(1), 1)
        self.assertEquals(eulerTotient(2), 1)
        self.assertEquals(eulerTotient(23), 22)
        self.assertEquals(eulerTotient(60), 16)

if __name__ == '__main__':
    unittest.main()

