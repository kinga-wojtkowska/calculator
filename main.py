import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def add(a):
    return sum(a)

def sub(a):
    return a[0] - a[1]

def mult(a):
    result = 1
    for x in a: 
        result = result * x
    return result

def div(a):
    return a[0] / a[1]

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
    if op == 1 or op == 3:
        num_comp = int(input("Ile liczb wchodzi w skład działania?: "))
    else:
        num_comp = 2
    
    list_comp = []
    for i in range(num_comp):
        c = i + 1
        x = float(input("Podaj składnik nr %d: " % c))
        list_comp.append(x)
    
    logging.info("Wykonuję działanie: {}, dla następujących liczb: {}".format(op_txt[op], list_comp))
    result = operations[op](list_comp)
    logging.info("Wynik to: %.2f" % result)
    return result       

calculator()