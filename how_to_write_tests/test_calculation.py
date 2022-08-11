#!/usr/bin/env python3

import sys
import unittest
import calculation

release_name = 'test_calculation'

class CalTest(unittest.TestCase):
    def setUp(self) -> None:
        print('setUp')
        self.cal = calculation.Cal()

    def tearDown(self) -> None:
        print('tearDown')
        del self.cal

    def test_add_num_and_double(self):
        self.assertEqual(self.cal.add_num_and_double(1, 2), 6)

    def test_add_num_and_double_with_negative_number(self):
        self.assertEqual(self.cal.add_num_and_double(-1, 2), 2)

    @unittest.skip('skip test_add_num_and_double_with_negative_number')
    def test_add_num_and_double_with_zero(self):
        self.assertEqual(self.cal.add_num_and_double(0, 2), 4)

    @unittest.skipIf(sys.version_info < (3, 5), 'skip test_add_num_and_double_with_negative_number')
    def test_add_num_and_double_raise(self):
        with self.assertRaises(TypeError):
            self.cal.add_num_and_double('1', 2)

if __name__ == '__main__':
    unittest.main()
    sys.exit(0)



