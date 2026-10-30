def get_float() -> float:
    while True:
        try:
            return float(input(f'Введите A:\n'))
        except ValueError:
            print("\033[31m\033[1mA ДОЛЖНО БЫТЬ ЧИСЛОМ\033[0m")

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

flag = True
while flag:
    print('-'*50)

    print('Давайте выведем все целые степени числа A от 1 до N\n')
    
    a = get_float()
    n = get_int()
    
    print(f"\nВыводим '{a}'^t, где t=[1,...,{n}]", *[a**i for i in range(1, n+1)], sep='\n')

    if input("еще раз? (y/n)\n").lower() not in ["y", 'да']:
        flag = False
     
print("Усё")