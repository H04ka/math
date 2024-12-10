import math as m


def addition_first(e=0.000001) -> float:
    n = 1
    summation = 0
    while True:
        increment = 1 / n
        summation = summation + increment
        n = n + 1
        if m.fabs(increment) < e:
            break
        print(f'n = {n}')
        return summation
    
def addition_second(e=0.000001):
    try:
        n = 1
        summation = 0
        while True:
            increment = n / n**2
            summation = summation + increment 
            n = n + 1
            if m.fabs(increment) < e:
                break
        print(f'n = {n}')
        return summation
    except ValueError:
        return "Error: Input is not a valid number"

def addition_third(e=0.000001):
    try:
        n = 2
        summation = 0
        while True:
            increment = m.log(n)/n
            n = n + 1
            if m.fabs(increment) < e:
                break
        print(f"n = {n}")
        return summation
    except ValueError:
        return "Error: Input is not a valid number"

def addition_fourth(e=0.000001):
    try:
        n = 2
        summation = 0
        while True:
            increment = m.sin(n)/m.log(n)
            summation = summation + increment
            n = n + 1
            if m.fabs(increment) < e:
                break
        print(f'n = {n}')
        return summation
    except ValueError:
        return "Error: Input is not a valid number"

def multiplication_first(e=0.000001):
    try:
        n = 2
        multiplication = 1
        while True:
            increment = 1 / n * m.log(n)
            multiplication = multiplication * (1 + increment)
            n = n + 1
            if m.fabs(increment) < e:
                break
        print(f'n = {n}')
        return multiplication
    except ValueError:
        return "Error: Input is not a valid number"
    
def multiplication_second(e=0.000001):
    try:
        n = 2
        multiplication = 1
        while True:
            increment =  n / (n - 1)*(n + 2)
            multiplication = multiplication * (1 + increment)
            n = n + 1
            if m.fabs(increment) < e:
                break
        print(f'n = {n}')
        return multiplication
    except ValueError:
        return "Error: Input is not a valid number"

def multiplication_third(e=0.000001):
    try:
        n = 1
        multiplication = 1
        while True:
            increment = m.cos(n) / m.sin(m.pow(n, 2))
            multiplication = multiplication * (1 + increment)
            n = n + 1
            if m.fabs(increment) < e:
                break
            print(f'n = {n}')
            return multiplication
    except ValueError:
        return "Error: Input is not a valid number"

def multiplication_fourth(e=0.000001):
    try:
        n = 1
        multiplication = 1
        while True:
            increment = m.atan(n) / (m.exp(n) - m.pi)
            multiplication = multiplication * (1 + increment)
            n = n + 1
            if m.fabs(increment) < e:
                break
            print(f'n = {n}')
            return multiplication
    except ValueError:
        return "Error: Input is not a valid number"


def choose():
    while True:
        n = int(input("выберите пример: 1-4(Арифметическая сумма)/ 5-8(Арифметическое произведение)"))
        if n == 1:
            X=float(input("введи:"))
            a = addition_first(n)
            print(a)
        elif n == 2:
            X=float(input("введи:"))
            a = addition_second(n)
            print(a)
        elif n == 3:
            X=float(input("введи:"))
            a = addition_third(n)
            print(a)
        elif n == 4:
            X=float(input("введи:"))
            a = addition_fourth(n)
            print(a)
        elif n == 5:
            X=float(input("введи:"))
            a = multiplication_first(n)
            print(a)
        elif n == 6:
            X=float(input("введи:"))
            a = multiplication_second(n)
            print(a)
        elif n == 7:
            X=float(input("введи:"))
            a = multiplication_third(n)
            print(a)
        elif n == 8:
            X=float(input("введи:"))
            a = multiplication_fourth(n)
            print(a)
choose()
