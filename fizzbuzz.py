import unittest

def fizzbuzz(number):
    fizz = []
    for i in range(number):
        if i != 0 and i % 3 == 0:
            fizz.append('Fizz')
        elif i != 0 and i % 5 == 0:
            fizz.append('Buzz')
        else:
            fizz.append(i)
    
    return fizz

class StubTests(unittest.TestCase):
    def testFizz0_2(self):
        self.assertEquals(fizzbuzz(3), [0,1,2])
    
    def testFizz0_3(self):
        self.assertEquals(fizzbuzz(4), [0,1,2,'Fizz'])
    
    def testFizz0_5(self):
        self.assertEquals(fizzbuzz(6), [0,1,2,'Fizz',4,'Buzz'])
    
    def testFizz0_6(self):
        self.assertEquals(fizzbuzz(7), [0,1,2,'Fizz',4,'Buzz','Fizz'])
        
    def testFizz0_10(self):
        self.assertEquals(fizzbuzz(11), [0,1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz'])

if __name__ == '__main__':
    unittest.main()
