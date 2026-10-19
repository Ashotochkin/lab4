def get_int(text: str) -> int:

    while True:

        try:

            a = int(input(f'Введите {text}\n'))

            if a <= 1:
                print("\n\033[31m\033[1mЧИСЛО ДОЛЖНО БЫТЬ БОЛЬШЕ 1\033[0m\n")
                continue

            return a
        
        except ValueError:
            
            print("\n\033[31m\033[1mДОЛЖНО БЫТЬ ЧИСЛО\033[0m\n")

flag = True
while flag:
    print('-'*50)

    print('Давайте найдём для какого минимального k:  1+(1/2)+(1/3)+...+(1/k) > A, где A>1')
    
    a = get_int('A')
    
    if a<=1: print("\n\033[31m\033[1mN - целое и больше единицы\033[0m\n"); continue
    
    k = 0
    s = 0

    while s <= a:
        k += 1
        s += 1 / k

    print("K = {}\nСумма = {}".format(k, s))

    if input("еще раз? (y/n)\n").lower() not in ["y", 'да']:
        flag = False

print("Усё")
