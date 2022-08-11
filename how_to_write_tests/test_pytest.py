#!/usr/bin/env python3

import sys
import pytest
import calculation

class TestCal(object):
    @classmethod
    def setup_class(cls):
        print('setUpClass')
        cls.cal = calculation.Cal()

    @classmethod
    def teardown_class(cls):
        print('tearDownClass')
        del cls.cal

    def setup_method(self, method):
        print('setUp')
        print(f"{method.__name__}")
        # self.cal = calculation.Cal()

    def teardown_method(self, method):
        print('tearDown')
        print(f"{method.__name__}")
        # del self.cal

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 2) == 6

    def test_add_num_and_double_with_negative_number(self):
        assert self.cal.add_num_and_double(-1, 2) == 2

    @pytest.mark.skip('skip test_add_num_and_double_with_negative_number')
    def test_add_num_and_double_with_zero(self):
        assert self.cal.add_num_and_double(0, 2) == 4

    @pytest.mark.skipif(sys.version_info < (3, 5), reason='skip test_add_num_and_double_with_negative_number')
    def test_add_num_and_double_raise(self):
        with pytest.raises(TypeError):
            self.cal.add_num_and_double('1', 2) == 5

    def test_add_num_and_double_with_negative_number_raise(self, request):
        os_name = request.config.getoption('--os-name')
        if os_name == 'linux' or os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        with pytest.raises(TypeError):
            self.cal.add_num_and_double(-1, '2') == 1