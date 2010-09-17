import unittest

def fizzbuzz(number):
    fizz = []
    for i in range(1, number+1):
        if i % 3 == 0 or  i % 5 == 0:
            append = ""
            if i % 3 == 0:
                append += "Fizz"
            if i % 5 == 0:
                append += "Buzz"
            fizz.append(append)

        else:
            fizz.append(i)
    
    return fizz

class StubTests(unittest.TestCase):
    def testFizz1_2(self):
        self.assertEquals(fizzbuzz(2), [1,2])
    
    def testFizz1_3(self):
        self.assertEquals(fizzbuzz(3), [1,2,'Fizz'])
    
    def testFizz1_5(self):
        self.assertEquals(fizzbuzz(5), [1,2,'Fizz',4,'Buzz'])
    
    def testFizz1_6(self):
        self.assertEquals(fizzbuzz(6), [1,2,'Fizz',4,'Buzz','Fizz'])
        
    def testFizz1_10(self):
        self.assertEquals(fizzbuzz(10), [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz'])

if __name__ == '__main__':
    unittest.main()

