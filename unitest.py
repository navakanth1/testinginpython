import unittest

class mpApp2(unittest.TestCase):
    def test_case3(self):
        self.assertEqual("hi","hi")


class myApp(unittest.TestCase):

    def test_case1(self):
        a=10
        b=20
        c=a+b
        self.assertNotEqual(a+b,c)
    def test_case2(self):
        self.assertNotEqual("hi","hello")

if __name__ == "__main__":
    unittest.main()