"""
Exercício 3 - Palavras em números
Neste problema, dado uma palavra composta somente por letras 
[a-zA-Z], cada letra possui um valor específico, ‘a’ vale 1, 
‘b’ vale 2 e assim por diante, até a letra ‘z’ que vale 26. 
Do mesmo modo ‘A’ vale 27, ‘B’ vale 28, até a letra ‘Z’ que vale 52.

O valor da palavra será a soma total dos valores de todas as letras da palavra.

Você precisa definir se cada palavra em um conjunto de palavras é:
    * Prima ou não;
    * Feliz ou não;
    * Múltipla de 3 ou 5;

Qualquer caracter na palavra que não seja uma letra deve ser desconsiderado.
"""


from string import ascii_letters
from ex1 import trace_multiples, sum_multiples
from ex2 import happy_number


def is_prime(num):
    divided_by = trace_multiples(num, list(range(2, num)))
    return not any(divided_by) and num > 0

def word_to_numbers(word):
    result = []
    for char in word:
        if char not in ascii_letters:
            continue
        if char.isupper():
            value = ord(char)-38
        else:
            value = ord(char)-96
        result.append(value)
    return result

def text_info(text):
    result = []
    for word in text.split():
        num = sum(word_to_numbers(word))
        is_div_by_3_or_5 = any(trace_multiples(num, [3, 5]))
        info = {
            'is_prime': is_prime(num),
            'happy_number': happy_number(num),
            'multiple3_or_5': is_div_by_3_or_5,
        }
        result.append(info)
    return result


if __name__ == '__main__':
    for i in text_info('Back to the future'): print(i)
