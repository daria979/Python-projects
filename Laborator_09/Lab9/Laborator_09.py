# LABORATOR 9 - Machine Learning

# Sa se determine:

import numpy

valori_inregistrate = [98,84,87,68,111,86,103,87,84,78,100,95,84,106]

print("Valorile sunt:")
print(valori_inregistrate)
print()

#mean value
mean = numpy.mean(valori_inregistrate)
print("--->Mean value:",mean)

#median value

#sortam lista
valori_inregistrate.sort()
print(valori_inregistrate)
print()

median = numpy.median(valori_inregistrate)

print("--->Median value:",median)
print()

#mode value - care apare de cele mai multe ori
from scipy import stats

mode = stats.mode(valori_inregistrate);
print()
print("--->Mode value",mode)
print()

