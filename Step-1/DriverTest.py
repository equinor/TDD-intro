import unittest

def fun(x):
    return x + 1

class MyTest2(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)

