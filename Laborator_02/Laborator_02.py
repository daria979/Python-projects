# LABORATOR 02

# Se genereaza aleator 10 numere. Sa se afiseze numerele pare numerotate.

import random

list_par = 1;
for idx in range (10):
    number = random.randint(1, 100);
    if number %2 == 0:
        print(list_par,'->', number);
        list_par += 1;
    else: continue;

print();