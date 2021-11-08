import unittest
import url_converter

class MyTestCase(unittest.TestCase):
    def test_spaces(self):
        s = "Mountain Valley"
        res = url_converter.string_to_url_format(s)
        self.assertEqual("Mountain%20Valley", res)

    def test_quotes(self):
        s = "\"Yosemite\""
        res = url_converter.string_to_url_format(s)
        self.assertEqual("%22Yosemite%22", res)


if __name__ == '__main__':
    unittest.main()
