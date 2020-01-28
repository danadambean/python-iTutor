# Ex1.


def parcurge_numar(valoare):
    suma = 0
    for i in range(valoare + 1):
        if i % 2 == 0:
            suma = suma + i
        if i < 10:
            print(i)
        elif i < 20:
            continue

    return suma


print(parcurge_numar(100))

# Ex2.


def afiseaza_numar(val):
    for num in range(val + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


print(afiseaza_numar(100))