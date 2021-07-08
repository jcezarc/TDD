"""
Exercício 2 - Números felizes 
Os números felizes são definidos pelo seguinte procedimento: 
Começando com qualquer número inteiro positivo, o número é substituído pela soma dos quadrados dos seus dígitos. 
Repete-se esse processo até que o número seja igual a 1. 
Tomamos o 7, que é um número feliz: 
● 7² = 49 
● 4² + 9² = 97 
● 9² + 7² = 130 
● 1² + 3² + 0² = 10 
● 1² + 0² = 1 
Um número não é feliz quando, em seu processo de cálculo, em algum momento ele entra em loop, ou seja, ele passe por um número que ele já passou anteriormente (não é possível determinar um número específico que ele sempre irá passar).
"""


def sum_squares_of_digits(num):
    return sum([int(digit)**2 for digit in str(num)])


def happy_number(num, seen=[]):
    while num not in seen:
        seen.append(num)
        num = sum_squares_of_digits(num)
        if num == 1:
            return True
    return False
