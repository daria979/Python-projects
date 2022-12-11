# LABORATOR 03

#Sa se afiseze aleator 3 numere si sa se determine valoarea radicalului sumei celor 3 numere.
#Pentru partea zecimala a radicalului afisati doar 5 zecimale.

import random
import math

nr1 = random.randint(1, 100);
nr2 = random.randint(1, 100);
nr3 = random.randint(1, 100);

print("Numerele generate aleator sunt: ", nr1, nr2, nr3);
print();

Sum = nr1 + nr2 + nr3;
print("Suma numerelor este: ", Sum);
print();

result = math.sqrt(Sum);

print("Radical din suma este: ", round(result,5));
print();