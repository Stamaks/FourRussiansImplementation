import math
import os


MAGIC_CONSTANT = 10  # if log_n > magic_constant, we do not dump precalculations to the file


def rounded_log(size_n):
    return math.ceil(math.log2(size_n))


def precalculate(size_n):  # O(2^(log_n*2)*log_n) if not in the data folder
    set_zero = set()
    set_one = set()
    log_n = rounded_log(size_n)
    if log_n <= 10 and os.path.exists(f'data/{log_n}'):
        pass  # TODO: подкачка из файла
    else:
        for i in range(2 ** log_n):
            for j in range(i, 2 ** log_n):
                bit_and = i & j  # O(1)
                if bin(bit_and).count('1') % 2:  # O(log_n)
                    set_one.add(bit_and)  # O(1)
                else:
                    set_zero.add(bit_and)  # O(1)

    return set_zero, set_one


def get_cmprsd_matr_size(size_n, vector_size):
    return math.ceil(size_n / vector_size)


def get_compressed_matrix(matrix, size_n, vector_size, is_first_matrix=True):
    size_cmprsd = get_cmprsd_matr_size(size_n, vector_size)

    if is_first_matrix:
        cmprsd_matrix = [[0] * size_cmprsd for i in range(size_n)]
    else:
        cmprsd_matrix = [[0] * size_n for i in range(size_cmprsd)]

    for i in range(size_n):
        for cmprsd_ind, j in enumerate(range(0, size_n, vector_size)):  # from 0 to n, step log_n
            number = 0
            degree = 0
            # if j + vector_size > size_n:
            #     degree = j + vector_size - size_n
            for vec_ind in range(min(j + vector_size - 1, size_n - 1), j - 1, -1):
                if is_first_matrix:
                    number += matrix[i][vec_ind] * 2 ** degree
                else:
                    number += matrix[vec_ind][i] * 2 ** degree
                degree += 1

            if is_first_matrix:
                cmprsd_matrix[i][cmprsd_ind] = number
            else:
                cmprsd_matrix[cmprsd_ind][i] = number

    return cmprsd_matrix


def run_four_russians(matrix_a, matrix_b, size_n):
    if size_n == 1:
        return [[matrix_a[0][0] * matrix_b[0][0]]]

    set_zero, set_one = precalculate(size_n)

    log_n = rounded_log(size_n)

    matrix_c = [[0] * size_n for i in range(size_n)]

    cmprsd_matrix_a = get_compressed_matrix(matrix_a, size_n, log_n, is_first_matrix=True)
    cmprsd_matrix_b = get_compressed_matrix(matrix_b, size_n, log_n, is_first_matrix=False)

    for i in range(size_n):
        for j in range(size_n):
            mult_sum = 0
            for k in range(get_cmprsd_matr_size(size_n, log_n)):
                mult = cmprsd_matrix_a[i][k] & cmprsd_matrix_b[k][j]
                mult_sum += int(cmprsd_matrix_a[i][k] & cmprsd_matrix_b[k][j] in set_one)
            matrix_c[i][j] = mult_sum % 2

    return matrix_c
