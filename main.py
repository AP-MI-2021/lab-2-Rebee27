'''
1. Gaseste ultimul numar prim mai mic decat un numar dat.
param n: numarul dat
param is_prime: verifica daca un numar este  prim
return : ultimul numar prim mai mic decat numarul dat
'''


def printMeniu():
    print("1.Citire lista")
    print("2.Determina ultimul numar prim mai mic decat  numarul dat")
    print("3.Determinati daca un numar este palindrom")
    print("4.Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime.")
    print("x.Iesire")


def citireNumar():
    n = int(input("Dati un numar"))
    return n


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


'''
5. Determinati daca un numar este palindrom.
param n: int, un numar introdus de utilizator.
param copy: int, copia numarului introdus.
param palindrom: int, o variabila in care se va stoca palindromul numarului introdus.
return: palindromul unui numar.
'''


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


'''
12. Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime. 
'''


def is_superprime(n: int) -> bool:
    while n > 0:
        if is_prime(n):
            return False
        n = n // 10
    return True


def test_is_superprime():
    assert is_superprime(233) == True
    assert is_superprime(237) == False
    assert is_superprime(29) == True


def main():
    test_is_superprime()
    test_is_palindrom()
    test_get_largest_prime_below()
    while True:
        printMeniu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            n = citireNumar()
        elif optiune == "2":
            print(get_largest_prime_below(n))
        elif optiune == "3":
            if(is_palindrom(n)):
                print("True")
            else:
                print("False")
        elif optiune == "3":
            print(is_superprime(n))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati!")
