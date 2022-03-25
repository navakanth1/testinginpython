import unittest

def LogIn(username, password):
    if username == "admin" and password == "12345":

        return True
    else:
        return False

class LogIncheck(unittest.TestCase):
    def test_login_check(self):
        username = " admin"

        password = " 12345"

        result = LogIn(username, password)
        self.assertTrue(result)

if __name__=="__main__":

    unittest.main()