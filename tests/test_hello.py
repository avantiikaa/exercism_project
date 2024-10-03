import unittest
from solutions.hello import hello

class HelloTest(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello('Alice'), 'Hello, Alice!')
        self.assertEqual(hello('Bob'), 'Hello, Bob!')
        self.assertEqual(hello(), 'Hello, World!')

if __name__ == '__main__':
    unittest.main()
