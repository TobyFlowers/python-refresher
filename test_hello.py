import math
import unittest
import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")

    def test_add(self):
        self.assertEqual(hello.add(1,2), 3)

    def test_sub(self):
        self.assertEqual(hello.sub(2,2), 0)   

    def test_mul(self):
        self.assertEqual(hello.mul(1,2), 2)

    def test_div(self):
        self.assertEqual(hello.div(4,2), 2)

    def test_sqrt(self):
        self.assertEqual(hello.sqrt(4), 2)

    def test_power(self):
        self.assertEqual(hello.power(1,2), 1)

    def test_log(self):
        self.assertEqual(hello.log(10), 2.302585092994046)

    def test_exp(self):
        self.assertEqual(hello.exp(1), math.e)

    

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)


if __name__ == "__main__":
    unittest.main()
