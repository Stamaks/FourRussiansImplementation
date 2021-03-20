import math
import os


MAGIC_CONSTANT = 10  # if log_n > magic_constant, we do not dump precalculations to the file


def precalculate(size_n):  # O(2^(log_n*2)*log_n) if not in the data folder
    set_zero = set()
    set_one = set()
    log_n = math.floor(math.log2(size_n))
    if log_n <= 10 and os.path.exists(f'data/{log_n}'):
        pass  # TODO: подкачка из файла
    else:
        for i in range(2 ** log_n):
            for j in range(i, 2 ** log_n):
                bit_and = i & j  # O(1)
                if bin(bit_and) % 2:  # O(log_n)
                    set_one.add(bit_and)  # O(1)
                else:
                    set_zero.add(bit_and)  # O(1)


def run_four_russians(matrix_a, matrix_b, size_n):
    if size_n == 1:
        return [[matrix_a[0][0] * matrix_b[0][0]]]

    pass
