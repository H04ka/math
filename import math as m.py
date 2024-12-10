import math as m

def addition_first(n: int):
    try:
        summation = 0
        for i in range(1, n + 1):
            summation = summation + m.sqrt(m.fabs(m.pow(2, i) * m.log(i+1) * m.log(i+2, 3)))
        return round(summation,6)
    except ValueError:
        return "Error: Input is not a valid number"

def addition_second(n: int):
    try:
        summation = 0
        for i in range(n + 1):
            summation = summation + (m.log(i) + m.factorial(i) * m.log(i+1, 5)**2 * m.log2(i))
            return round(summation,6)
    except ValueError:
        return "Error: Input is not a valid number"

def addition_third(n: int):
    try:
        summation = 0
        for i in range(1, n + 1):
            summation = summation + m.pow(m.log2(i) * 3**i - 1 + i*m.log(2, m.e), 3)
        return round(summation,6)
    except ValueError:
        return "Error: Input is not a valid number"

def addition_fourth(n: int):
    try:
        summation = 0
        for i in range(n + 1):
            summation = summation  + m.log(i+1) / m.log10(i+2) * m.log(i+3, 7)
            return round(summation,6)
    except ValueError:
        return "Error: Input is not a valid number"

def addition_fifth(n:int):
    try:
        summation = 0 
        for i in range(1, n + 1):
            summation = summation + (m.exp(i) + m.log(i) * m.log(i+2, 5))**2
            return round(summation,6)
    except ValueError:
        return "Error: Input is not a valid number"

def multiplication_first(n: int):
    try:
        multiplication = 1
        for i in range(1, n + 1):
            multiplication = multiplication * (m.pow(2, -i) * m.log(i+1) + m.pow(1.2, i/12) * m.log10(i+2))
            return round(multiplication,6)
    except ValueError:
        return "Error: Input is not a valid number"

def multiplication_second(n: int):
    try:
        multiplication = 1
        for i in range(1, n + 1):
            multiplication = multiplication * (3* m.log2(i + 2) - (m.exp**-i / m.log10(i + 1)) + 2**1-2*i)
            return round(multiplication,6)
    except ValueError:
        return "Error: Input is not a valid number"

def multiplication_third(n: int):
    try:
        multiplication = 1
        for i in range(1, n + 1):
            multiplication = multiplication * m.sqrt(m.fabs(m.pow(5, i + 1)/ i**3 + m.log(i*2) - m.factorial(i)))
            return round(multiplication,6)
    except ValueError:
        return "Error: Input is not a valid number"

def multiplication_fourth(n: int):
    try:
        multiplication = 1
        for i in range(1, n + 1):
            summation = 0
            for k in range(1, i + 2):
                summation = summation + 1 / k
                multiplication = multiplication * (m.log(i+1) * m.exp(i/7) * summation)
                return round(multiplication,6)
    except ValueError:
        return "Error: Input is not a valid number"
     
def multiplication_fifth(n: int):
    try:
        multiplication = 1
        for i in range(1, n + 1):
            summation = 0
            for k in range(1, i + 2):
                summation = summation + (m.log(i + 1) * m.log2(i+2))
                multiplication = multiplication * summation
                return round(multiplication,6)
    except ValueError:
        return "Error: Input is not a valid number"

def choose():
    while True:
        i = int(input("выберите пример: 1-5(Арифметическая сумма)/ 6-10(Арифметическое произведение)"))
        if i == 1:
            X=float(input("введи:"))
            a = addition_first(i)
            print(a)
        elif i == 2:
            X=float(input("введи:"))
            a = addition_second(i)
            print(a)
        elif i == 3:
            X=float(input("введи:"))
            a = addition_third(i)
            print(a)
        elif i == 4:
            X=float(input("введи:"))
            a = addition_fourth(i)
            print(a)
        elif i == 5:
            X=float(input("введи:"))
            a = addition_fifth(i)
            print(a)
        elif i == 6:
            X=float(input("введи:"))
            a = multiplication_first(i)
            print(a)
        elif i == 7:
            X=float(input("введи:"))
            a = multiplication_second(i)
            print(a)
        elif i == 8:
            X=float(input("введи:"))
            a = multiplication_third(i)
            print(a)
        elif i == 9:
            X=float(input("введи:"))
            a = multiplication_fourth(i)
            print(a)
        elif i == 10:
            X=float(input("введи:"))
            a = multiplication_fifth(i)
            print(a)
choose()
