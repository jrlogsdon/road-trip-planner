import unittest
import URLify

class MyTestCase(unittest.TestCase):
    def test_spaces(self):
        s = "Mountain Valley"
        res = URLify.URLIfy(s)
        self.assertEqual("Mountain%20Valley", res)

    def test_quotes(self):
        s = "\"Yosemite\""
        res = URLify.URLIfy(s)
        self.assertEqual("%22Yosemite%22", res)


if __name__ == '__main__':
    unittest.main()
