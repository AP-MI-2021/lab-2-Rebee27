"""
1. Gaseste ultimul numar prim mai mic decat un numar dat.
param n: numarul dat
param is_prime: verifica daca un numar este  prim
return : ultimul numar prim mai mic decat numarul dat
"""


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


def get_largest_prime_below(n):
    for i in range(n - 1, 0, -1):
        if is_prime(i):
            return i


def test_get_largest_prime_below():
    assert get_largest_prime_below(3) == 2
    assert get_largest_prime_below(10) == 7
    assert get_largest_prime_below(24) == 23
    assert get_largest_prime_below(2) is None


test_get_largest_prime_below()
number = int(input("Dati un numar pentru a afla ultimul numar prim mai mic decat acesta = "))
print("ultimul numar prim mai mic decat numarul dat este ", get_largest_prime_below(number))


"""
5. Determinati daca un numar este palindrom.
param n: int, un numar introdus de utilizator.
param copy: int, copia numarului introdus.
param palindrom: int, o variabila in care se va stoca palindromul numarului introdus.
return: palindromul unui numar.
"""


def is_palindrom(n):
    copy = n
    palindrom = 0
    while n > 0:
        last_digit = n % 10
        palindrom = palindrom * 10 + last_digit
        n = n // 10
    if copy == palindrom:
        return True
    else:
        return False


def test_is_palindrom():
    assert is_palindrom(123) == False
    assert is_palindrom(32323) == True
    assert is_palindrom(111) == True
    assert is_palindrom(7) == True


test_is_palindrom()
number = int(input("Dați un număr pentru a afla daca este palindrom = "))
if is_palindrom(number):
    print("True")
else:
    print("False")


'''

'''
