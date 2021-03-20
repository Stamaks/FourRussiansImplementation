from src.lib.matrices_multiplication import get_cmprsd_matr_size, rounded_log


def test_rounded_log():
    assert rounded_log(10) == 4
    assert rounded_log(8) == 3


def test_get_cmprsd_matr_size():
    assert get_cmprsd_matr_size(10, 2) == 5
    assert get_cmprsd_matr_size(10, 3) == 4
