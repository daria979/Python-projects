# LABORATOR 8 - Librarii numerice - NumPy

# Sa se afiseze valorile mai mari decat o valoare prestabilita dintr-un vector dat
# si sa se completeze cu true sau false in locul valorilor, intr-o noua lista, 
# care sa respecte conditia data

import numpy as np

arr = np.array([31, 32, 33, 34, 35])

# Lista goala
filter_arr = []

# parcurgem elementele vectorului arr
for element in arr:
  # daca elementul este mai mare decat 33 este True, altfel, False
  if element > 33:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)