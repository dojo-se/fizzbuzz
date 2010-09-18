import unittest

def fizzbuzz(number):
    def procuraFizz(num):
        if num % 3 == 0 or '3' in str(num):
            return "Fizz"
        else: 
            return ""
        
    def procuraBuzz(num):
        if num % 5 == 0 or '5' in str(num): 
            return "Buzz"
        else: 
            return ""
    
    fizz = []
    for num in range(1, number+1):
        fizzbuzz = procuraFizz(num)+procuraBuzz(num)
        if fizzbuzz == "": fizz.append(num)
        else: fizz.append(fizzbuzz)
    
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
    
    def testFizz1_13(self):
        self.assertEquals(fizzbuzz(13), [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz', 11, 'Fizz', 'Fizz'])
        
    def testFizz1_15(self):
        self.assertEquals(fizzbuzz(15), [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz', 11, 'Fizz', 'Fizz', 14, 'FizzBuzz'])
    
    def testFizz1_23(self):
        self.assertEquals(fizzbuzz(23), [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz', 11, 'Fizz', 'Fizz', 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 'Fizz'])
    
    def testFizz1_52(self):
        self.assertEquals(fizzbuzz(51)[-1],'FizzBuzz')


if __name__ == '__main__':
    unittest.main()

