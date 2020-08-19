import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def add(a, b, *args):
    return a + b + sum(args)

def sub(a, b):
    return a - b

def mult(a, b, *args):
    result = a * b
    for x in args: 
        result = result * x
    return result

def div(a, b):
    return a / b

operations = {
    1: add,
    2: sub,
    3: mult,
    4: div
}

op_txt = {
    1: 'dodawanie',
    2: 'odejmowanie',
    3: 'mnożenie',
    4: 'dzielenie'
}

def calculator():
    op = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    args = []
    a = float(input("Podaj składnik nr 1: "))
    b = float(input("Podaj składnik nr 2: "))
    if op == 1 or op == 3:
        num_comp = int(input("Podano 2 składniki, ile liczb chcesz jeszcze dodać do działania?: "))
        for i in range(num_comp):
            c = i + 3
            x = float(input("Podaj składnik nr %d: " % c))
            args.append(x)
    else:
        num_comp = 2
            
    
    logging.info("Wykonuję działanie: {}, dla następujących liczb: {}, {}, {}".format(op_txt[op], a, b, args))
    result = operations[op](a, b, *args)
    logging.info("Wynik to: %.2f" % result)
    return result       

calculator()