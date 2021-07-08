import sys
sys.path.append('.')
sys.path.append('..')
from exercicios.ex2 import (
    sum_squares_of_digits,
    happy_number
)

def test_is_happy_number():
    assert happy_number(7)

def test_not_happy():
    seen = []
    assert not happy_number(43, seen)
    # --- Confirma que o último número visto é duplicado:
    duplicated = sum_squares_of_digits(seen[-1])
    assert duplicated in seen


EX2_TEST_CASES = [
    test_is_happy_number,
    test_not_happy,
]
