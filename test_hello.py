import math
import unittest
import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")
        self.assertNotEqual(hello.hello(), "Hello! world!")
        self.assertNotEqual(hello.hello(), "Bye, world!")

    def test_add(self):
        self.assertEqual(hello.add(1,2), 3)
        self.assertEqual(hello.add(1,3), 4)
        self.assertNotEqual(hello.add(3,2), 4)


    def test_sub(self):
        self.assertEqual(hello.sub(2,2), 0)
        self.assertEqual(hello.sub(3,2), 1)   
        self.assertNotEqual(hello.sub(3,2), 4)


    def test_mul(self):
        self.assertEqual(hello.mul(1,2), 2)
        self.assertEqual(hello.mul(2,2), 4)
        self.assertNotEqual(hello.mul(1,4), 5)


    def test_div(self):
        self.assertEqual(hello.div(4,2), 2)
        self.assertEqual(hello.div(8,2), 4)
        self.assertNotEqual(hello.div(42,6), 8)

    def test_sqrt(self):
        self.assertEqual(hello.sqrt(4), 2)
        self.assertEqual(hello.sqrt(9), 3)
        self.assertNotEqual(hello.sqrt(5), 3)

    def test_power(self):
        self.assertEqual(hello.power(1,2), 1)
        self.assertEqual(hello.power(1,4), 1)
        self.assertNotEqual(hello.power(3,2), 122)

    def test_log(self):
        self.assertEqual(hello.log(10), 2.302585092994046)
        self.assertEqual(hello.log(math.e), 1)
        self.assertNotEqual(hello.log(math.e), 3)

    def test_exp(self):
        self.assertEqual(hello.exp(1), math.e)
        self.assertEqual(hello.exp(0), 1)
        self.assertNotEqual(hello.exp(3), 4)

    

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)
        self.assertNotEqual(hello.sin(0.5 * math.pi), 2)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)
        self.assertNotEqual(hello.cos(2), 3)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)
        self.assertNotEqual(hello.tan(3), 0.52)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)
        self.assertNotEqual(hello.cot(3), 34)


if __name__ == "__main__":
    unittest.main()
