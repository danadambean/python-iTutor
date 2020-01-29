# Ex 1.

number = int(input("Pick a number: "))

par = []
impar = []
i = 0

reverse_number = str(number)[::-1]
if number == int(reverse_number):
    print("Number is a palindrome!")

while number != 0:
    x = number % 10
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
    i = i + x
    number = int(number / 10)
print("Suma cifrelor: ", i)


if len(impar) == 0:
    print("Toate cifrele sunt pare.\nNmarul cifrelor este: {} iar suma : {}". format(len(par), i))

else:
    print("Numarul cifrelor pare: {} iar suma lor {}".format(len(par), sum(par)))
    print("Numarul cifrelor impare: {} iar suma lor {}".format(len(impar), sum(impar)))


# Ex 2.

nr = []

i = 0
max_number = 0
num = 0

while True:
    num = int(input("Pick a number "))
    nr.append(num)
    if num > max_number:
        max_number = num
    if num % 2 != 0:
        i = i + num
    if num == 0:
        break

r = 0
pozMax = []
count = 0
for r in range(len(nr)-1):
    if nr[r] + 1 == nr[r+1]:
        count += 1
    else:
        pozMax.append(count)
        count = 1
    r += 1


print("Nr maxim: {} Suma nr impare e: {} iar numarul maxim de numere cosecutive: {}".format(max_number, i, max(pozMax)))




