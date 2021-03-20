from src.lib.matrices_multiplication import get_cmprsd_matr_size

def test_get_cmprsd_matr_size():
    assert get_cmprsd_matr_size(10, 2) == 5
    assert get_cmprsd_matr_size(10, 3) == 4
