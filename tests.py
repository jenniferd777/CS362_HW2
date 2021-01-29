# Name: Jennifer Daniels
# Assignment: HW2
# Description: Program performs tests on a function using white box testing


import unittest
from contrived_func import contrived_func


class TestCase(unittest.TestCase):
    """
    Class
    """

    def test1(self):
        # Test for value in range of 101 and 149
        # Test True for first If statement
        self.assertFalse(contrived_func(101),
                         msg='contrived_func()'.format())

    def test2(self):
        # Test for value 6, Test False for first If statement,
        # True for first elif statement, and then True for if statement
        self.assertFalse(contrived_func(6),
                         msg='contrived_func()'.format())

    def test3(self):
        # Test for value 46, Test False for first If statement,
        # True for first elif statement, False for if statement
        self.assertFalse(contrived_func(46),
                         msg='contrived_func()'.format())

    def test4(self):
        # Test for value 19, Test False for first If statement,
        # False for first elif statement, True for second elif statement
        self.assertTrue(contrived_func(19),
                         msg='contrived_func()'.format())

    def test5(self):
        # Test for value 47, Test False for first If statement,
        # False for first elif statement, True for second elif statement
        self.assertTrue(contrived_func(47),
                         msg='contrived_func()'.format())

    def test6(self):
        # Test for value 150, Test False for first If statement,
        # False for first elif statement, True for second elif statement
        self.assertTrue(contrived_func(150),
                         msg='contrived_func()'.format())

    def test7(self):
        # Test for value 150, Test False for first If statement,
        # False for first elif statement, False for second elif statement
        self.assertTrue(contrived_func(151),
                         msg='contrived_func()'.format())


if __name__ == '__main__':
    unittest.main(verbosity=2)
