#!/usr/bin/env python3

import unittest
from add import add


class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()