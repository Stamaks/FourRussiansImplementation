from src.lib.matrices_multiplication import get_cmprsd_matr_size, rounded_log, run_four_russians, precalculate

import json
import os


TEST_CASES_PATH = 'ut/test_data/test_run_four_russians'


def test_rounded_log():
    assert rounded_log(10) == 4
    assert rounded_log(8) == 3
    assert rounded_log(1) == 0


def test_precalculate():
    assert precalculate(2) == {1, 2}
    assert precalculate(3) == {1, 2, 4, 7}
    assert precalculate(4) == {1, 2, 4, 7, 8, 11, 13, 14}

    assert os.path.exists('.data/2')
    assert os.path.exists('.data/3')
    assert os.path.exists('.data/4')


def test_get_cmprsd_matr_size():
    assert get_cmprsd_matr_size(10, 2) == 5
    assert get_cmprsd_matr_size(10, 3) == 4


def bool_matrices_multiplication(matrix_a, matrix_b, size_n):
    matrix_c = [[0] * size_n for i in range(size_n)]
    for i in range(size_n):
        for j in range(size_n):
            mult_sum = 0
            for k in range(size_n):
                mult_sum += matrix_a[i][k] * matrix_b[k][j]
            matrix_c[i][j] = mult_sum % 2
    return matrix_c


def load_test_case(test_case_path):
    with open(os.path.join(test_case_path, 'matrix_a.json'), 'r') as f:
        matrix_a = json.load(f)
    with open(os.path.join(test_case_path, 'matrix_b.json'), 'r') as f:
        matrix_b = json.load(f)
    with open(os.path.join(test_case_path, 'expected_output.json'), 'r') as f:
        matrix_c = json.load(f)

    numbers = [int(i) for i in test_case_path.split('_') if i.isdigit()]
    size_n = numbers[-1]

    return matrix_a, matrix_b, matrix_c, size_n


def test_check_test_data():
    for test_case in os.listdir(TEST_CASES_PATH):
        matrix_a, matrix_b, matrix_c, size_n = load_test_case(os.path.join(TEST_CASES_PATH, test_case))

        assert all(len(matrix_a[i]) == len(matrix_a) for i in range(len(matrix_a)))
        assert all(len(matrix_b[i]) == len(matrix_b) for i in range(len(matrix_b)))
        assert all(len(matrix_c[i]) == len(matrix_c) for i in range(len(matrix_c)))
        assert len(matrix_a) == len(matrix_b) == len(matrix_c) == size_n

        assert bool_matrices_multiplication(matrix_a, matrix_b, size_n) == matrix_c


def test_run_four_russians():
    for test_case in os.listdir(TEST_CASES_PATH):
        matrix_a, matrix_b, matrix_c, size_n = load_test_case(os.path.join(TEST_CASES_PATH, test_case))

        assert run_four_russians(matrix_a, matrix_b, size_n)

        if size_n > 1:
            assert os.path.exists(f'.data/{size_n}')
