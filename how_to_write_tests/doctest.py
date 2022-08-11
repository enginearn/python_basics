#!/usr/bin/env python3


class Cal(object):
    def add_num_and_double(self, a, b):
        """add_num_and_double(a, b) -> a + b

        Args:
            a (int): int
            b (int): int

        Returns:
            int:(a + b) * 2

        >>> Cal().add_num_and_double(1, 2)
        6
        """
        return (a + b) * 2


if __name__ == '__main__':
    import doctest
    doctest.testmod()


