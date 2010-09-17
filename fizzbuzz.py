import unittest

def fizzbuzz(number):
    fizz = []
    for i in range(number):
        if i != 0 and i % 3 == 0:
            fizz.append('fizz')
            continue
        fizz.append(i)
    return fizz

class StubTests(unittest.TestCase):
    def testFizz0_2(self):
        self.assertEquals(fizzbuzz(3), [0,1,2])
    def testFizz0_3(self):
        self.assertEquals(fizzbuzz(4), [0,1,2,'fizz'])

if __name__ == '__main__':
    unittest.main()
