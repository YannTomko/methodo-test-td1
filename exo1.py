import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)


def sub(a, b):
    return a - b

class TestSub(unittest.TestCase):
    def test_sub_positive_numbers(self):
        self.assertEqual(sub(3, 2), 1)
    
    def test_sub_negative_numbers(self):
        self.assertEqual(sub(-1, -2), 1)


def mul(a, b):
    return a * b

class TestMul(unittest.TestCase):
    def test_mul_positive_numbers(self):
        self.assertEqual(mul(3, 2), 6)
    
    def test_mul_negative_numbers(self):
        self.assertEqual(mul(-1, -2), 2)


def div(a, b):
    return a / b

class TestDiv(unittest.TestCase):
    def test_div_positive_numbers(self):
        self.assertEqual(div(6, 2), 3)
    
    def test_div_negative_numbers(self):
        self.assertEqual(div(-4, -2), 2)


def exp(a, b):
    return a ** b

class TestExp(unittest.TestCase):
    def test_exp_positive_numbers(self):
        self.assertEqual(exp(6, 2), 36)
    
    def test_exp_negative_numbers(self):
        self.assertEqual(exp(-2, -2), 0.25)



if __name__ == '__main__':
    unittest.main()