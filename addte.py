import unittest


def add(a,b):
    return a+b

class testmyApp(unittest.TestCase):
    def test_case_add(self):
        a = 10
        b = 20
        c = add(a, b)
        self.assertEqual(a+b, c)

    def test_case_add1(self):
        a = 23.4
        b = 34.6
        c = add(a, b)
        self.assertEqual(a+b,c)


if __name__ == "__main__":
    unittest.main()


