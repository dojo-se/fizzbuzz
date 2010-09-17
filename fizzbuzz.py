import unittest

def fizzbuzz(number):
    return range(number)

class StubTests(unittest.TestCase):
    def testFizz(self):
        self.assertEquals(fizzbuzz(3), [0,1,2])

if __name__ == '__main__':
    unittest.main()
