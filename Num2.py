from math import factorial as fac, e

def get_float() -> float:
    while True:
        try:
            return float(input(f'Введите X:\n'))
        except ValueError:
            print("\033[31m\033[1mX ДОЛЖНО БЫТЬ ЧИСЛОМ\033[0m")

def get_int() -> int:
    while True:
        try:
            n = int(input(f'Введите N:\n'))
            if n > 0:
                return n
            else:
                int("some word will make an error")
        except ValueError:
            print("\033[31m\033[1mN ДОЛЖНО БЫТЬ НАТУРАЛЬНЫМ ЧИСЛОМ\033[0m")


while True:
    print('-'*50)

    print('Давайте выведем число, являющееся приближённым значением функции exp в точке X (чем больше N, тем точнее приближение)\n')
    
    x = get_float()
    
    flag = True
    while flag:
        try:
            n = get_int()
            print('\nОтвет:', sum([(x**i)/fac(i) for i in range(n+1)]), f'\nТочное значение: e^"{x}" = {e**x}')
            flag = False
            
        except OverflowError:
            print('\033[31m\033[1mСЛИШКОМ БОЛЬШОЕ N\033[0m')
            
    if input("\nеще раз? (y/n)\n").lower() not in ["y", 'да']:
        break
    
print("Усё")
