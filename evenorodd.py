import unittest



def check_even_or_odd(x):
    if x%2 == 0 :
        return "even"
    else:
        return "odd"
def checkdivisibleby7(x):
    if x % 7 == 0:
        return True
    else:
        return False

class myevenorodd(unittest.TestCase):
    def test_case_even_or_odd(self):
        result = check_even_or_odd(2)
        self.assertEqual("even", result)

    def test_case_even_or_odd1(self):
        result = check_even_or_odd(5)
        self.assertEqual("odd", result)

class checkdivisible(unittest.TestCase):
    def test_case_check_divisible(self):
        result = checkdivisibleby7(21)
        self.assertTrue(result)

    def test_case_check_divisible(self):
        result = checkdivisibleby7(2)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()