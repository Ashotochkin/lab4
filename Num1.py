def get_int(text:str) -> int:

    while True:

        try:

            return int(input(f'Введите {text}\n'))
        
        except:
            
            print("\n\033[31m\033[1mДОЛЖНО БЫТЬ ЧИСЛО\033[0m\n")

flag = True
while flag:
    print('-'*50)

    print('Давайте выведем все целые степени числа A от 1 до N\n')
    
    a = get_int('А')
    n = get_int('N')

    if n <= 0: print("\n\033[31m\033[1mN - целое и больше нуля\033[0m\n"); continue
    
    print([a**i for i in range(1, n+1)])

    if input("еще раз? (y/n)\n").lower() not in ["y", 'да']:
        flag = False
     
print("Усё")