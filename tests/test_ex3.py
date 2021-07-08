from exercicios.ex3 import (
    is_prime,
    word_to_numbers,
    text_info
)


def test_is_prime():
    assert is_prime(7)

def test_word_numbers():
    answer = word_to_numbers('Julio')
    expected = [36, 21, 12, 9, 15]
    assert answer == expected

def info_to_str(is_prime, happy_number, multipl3_5):
    # -- Representação simplificada 
    # --- das info.s da palavra:
    result = [' '] * 3
    if is_prime:
        result[0] = 'P'
    if happy_number:
        result[1] = 'H'
    if multipl3_5:
        result[2] = 'M'
    return ''.join(result)

def test_text_info():
    answer = ''
    for info in text_info('Back to the future'):
        answer += info_to_str(**info)
    assert answer == 'P    M  M H '


EX3_TEST_CASES = [
    test_is_prime,
    test_word_numbers,
    test_text_info,
]
