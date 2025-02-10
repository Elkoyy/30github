def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Введите число: "))

if is_prime(num):
    print(f"{num} — простое число")
else:
    print(f"{num} — составное число")
