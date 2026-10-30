def get_float() -> float:

    while True:
        try:
            a = float(input(f'Введите A:\n'))
            if a <= 1:
                int('')
            return a
        except ValueError:
            print("\n\033[31m\033[1mA - ЧИСЛО > 1\033[0m\n")

while True:
    print('-'*50)

    print('Давайте найдём для какого минимального k:  1+(1/2)+(1/3)+...+(1/k) > A, где A>1')
    
    A = get_float()
    
    k = 0
    s = 0

    while s <= A:
        k += 1
        s += 1 / k

    print(f"\nK = {k}\nСумма = 1+(1/2)+(1/3)+...+(1/{k}) = {s} > {A}")

    if input("\nеще раз? (y/n)\n").lower() not in ["y", 'да']:
        break

print("Усё")
