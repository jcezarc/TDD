"""
Exercício 1 - Múltiplos de 3 ou 5
---
Dado todos os números naturais abaixo de 10;
Se selecionarmos aqueles que sejam múltiplos de 3 ou 5 temos: 3, 5, 6 e 9.
Se somarmos todos esses valores, teremos o resultado = 23
Desenvolva um sistema que responda às seguintes dúvidas:
* Qual é o valor da soma de todos os números múltiplos de 3 ou 5 de números naturais abaixo de 1000?
* Qual é o valor da soma de todos os números múltiplos de 3 e 5 de números naturais abaixo de 1000?
* Qual é o valor da soma de todos os números múltiplos de (3 ou 5) e 7 de números naturais abaixo de 1000?
"""


def trace_multiples(x, numbers):
    #  Retorna uma lista dizendo se
    #  X é múltiplo de cada número:
    return [x % n == 0 for n in numbers]

def sum_multiples(limit, required_numbers=[], optional_numbers=[]):
    found = []
    for i in range(1, limit):
        if optional_numbers:
            if not any(trace_multiples(i, optional_numbers)):
                continue
        if required_numbers:
            if not all(trace_multiples(i, required_numbers)):
                continue
        found.append(i)
    return sum(found)
