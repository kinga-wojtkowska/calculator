import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def calculator():
    operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    if operation == 1 or operation == 3:
        num_comp = int(input("Ile liczb wchodzi w skład działania?: "))
    else:
        num_comp = 2
    
    list_comp = []
    for i in range(num_comp):
        c = i + 1
        x = float(input("Podaj składnik nr %d: " % c))
        list_comp.append(x)

    if operation == 2:
        logging.info("Odejmuję liczby: %s i %s" % (list_comp[0], list_comp[1]))
        result = list_comp[0] - list_comp[1]
        logging.info("Wynik to: %.2f" % result)
    elif operation == 4:
        logging.info("Dzielę liczbę %s przez liczbę %s" % (list_comp[0], list_comp[1]))
        result = list_comp[0] / list_comp[1]
        logging.info("Wynik to: %.2f" % result)
    elif operation == 1:
        logging.info("Dodaję następujące liczby:")
        logging.info(list_comp[0:len(list_comp)])
        result = sum(list_comp)
        logging.info("Wynik to: %.2f" % result)
    elif operation == 3:
        logging.info("Mnożę następujące liczby:")
        logging.info(list_comp[0:len(list_comp)])
        result = 1
        for x in list_comp: 
            result = result * x
        logging.info("Wynik to: %.2f" % result)    

calculator()