import sys
sys.path.append('.')
sys.path.append('..')
from exercicios.ex1 import sum_multiples


def test_multiples3_or_5():
    answer = sum_multiples(
        optional_numbers=[3, 5], 
        limit=10
    )
    assert answer == 23

def test_mult3_or_5_in1000():
    answer = sum_multiples(
        optional_numbers=[3, 5], 
        limit=1000
    )
    assert answer == 233168

def test_mult3_and_5_in1000():
    answer = sum_multiples(
        required_numbers=[3, 5], 
        limit=1000
    )
    assert answer == 33165

def test_mult3_or_5_and_7():
    answer = sum_multiples(
        optional_numbers=[3, 5],
        required_numbers=[7],
        limit=1000
    )
    assert answer == 33173


EX1_TEST_CASES = [
    test_multiples3_or_5,
    test_mult3_or_5_in1000,
    test_mult3_and_5_in1000,
    test_mult3_or_5_and_7,
]
