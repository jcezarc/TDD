from test_ex1 import EX1_TEST_CASES
from test_ex2 import EX2_TEST_CASES
from test_ex3 import EX3_TEST_CASES
from test_ex4 import EX4_TEST_CASES


if __name__ == '__main__':
    cases = EX1_TEST_CASES
    cases += EX2_TEST_CASES
    cases += EX3_TEST_CASES
    cases += EX4_TEST_CASES
    # -------------------------------------
    #  Testes manuais para quando 
    # o framework de testes falhar:
    # --------------------------------------
    for func in cases:
        print(func.__name__)
        func()
        print('\t...Ok!')
    print('-'*40)
    print('Testes concluídos com sucesso!!')
