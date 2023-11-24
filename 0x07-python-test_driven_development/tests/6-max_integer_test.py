#!/usr/bin/python3
'''Unittest for max_integer([..])'''
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''Making a Unittest.'''

    def test_no_arg(self):
        '''Unittest for no args'''
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        '''Unittest for embty list'''
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        '''Unittest for one int'''
        self.assertEqual(max_integer([88]), 88)

    def test_identical(self):
        '''Unittest for same int'''
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_start(self):
        '''Unittest for max number first'''
        self.assertEqual(max_integer([5, 0, 1, 2]), 5)

    def test_ordered(self):
        '''Unittest for orderd list'''
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)


    def test_positives_and_negatives(self):
        '''Unittest for + & -'''
        self.assertEqual(max_integer([-23, 66, 41, -24, -1024, 48, 98, 108, -26, -512]), 108)

    def test_negatives(self):
        '''Unittest for negative int'''
        self.assertEqual(
            max_integer(
                [-6105619, -854849, -562553, -3088955, -6711290, -4817844,
                    -1907189, -8110534, -6601769, -5837524, -4726702,
                    -8433749, -7251403, -5117635, -2979207, -1335257,
                    -6867266, -9073637, -6224732, -1080801, -1080228,
                    -6801278, -8351954, -1736432, -746131, -4376995,
                    -967891, -46638691, -781562, -7153670, -8038202,
                    -7893047, -93750883, -1132134, -3675971, -8495354,
                    -9158229, -96310087, -69319598, -8961209, -4906000,
                    -386471, -6439929, -26769965, -6881679, -6258057,
                    -5490677, -1107298, -41990148, -5933601, -9917695,
                    -7759849, -1045734, -48858006, -9485075, -5119579,
                    -4147063, -7622811, -46719781, -5439539, -840414,
                    -3671742, -4400074, -35493473, -9146070, -6071672,
                    -7213213, -107446, -3936098, -52415520, -9162654,
                    -6129976, -5791439, -3481890, -7828832, -6954726,
                    -5272933, -492516, -6115545, -8333464, -7271456,
                    -4097027, -4342575, -8400559, -8235052, -4373818,
                    -8054214, -8565596, -639225, -2292452, -4269529,
                    -7202853, -689036, -4379807, -7955196, -1536591,
                    -2839083, -2586661, -9941097, -3136620, -5]), -5)

    def test_ints_and_floats(self):
        '''Unittest for ints & floats'''
        self.assertEqual(
            max_integer(
                [10, 99.8, -100, -0.1, 1000, 9999, -100000, 9998.9]), 9999)

    def test_floats(self):
        '''Unittest for only floats'''
        self.assertEqual(
            max_integer(
                [.00123, .4575658, .02345, .234243434, .4561175674, .68678, .867090,]), 0.86709)

    def test_numeric_string(self):
        '''Unittest for numbers as string'''
        self.assertEqual(max_integer("19283544754"), "9")

    def test_string(self):
        '''Unittest for string'''
        self.assertEqual(max_integer("Hassan"), "s")

    def test_lists(self):
        '''Unittest for a number list'''
        self.assertEqual(max_integer([[], [2], [4], [2, 9]]), [4])

    def test_inf(self):
        '''Unittest for inf'''
        self.assertEqual(max_integer([99, float('inf'), float('-inf')]), float('inf'))

    def test_nan(self):
        '''Unittest for nan'''
        self.assertEqual(max_integer([99, float('nan'), 100]), 100)

    def test_mixed_list(self):
        '''Unittest for mixed list'''
        with self.assertRaises(TypeError):
            max_integer([[], [2], [4], [2, 9], 99, "Hassan"])

    def test_none(self):
        '''Unittest for none'''
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_dict(self):
        '''Unittest for dictinory'''
        with self.assertRaises(TypeError):
            max_integer([{20: 45, 14: 45}, {"a": "b"}])

if __name__ == '__main__':
    unittest.main()
