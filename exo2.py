import unittest
from io import StringIO
from unittest.mock import patch

def prog(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


class TestProg(unittest.TestCase):
    def test_prog(self):
        lines = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
        output = "\n".join(lines) + "\n"
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            prog(15)
            self.assertEqual(fake_out.getvalue(), output)

if __name__ == '__main__':
    unittest.main()
