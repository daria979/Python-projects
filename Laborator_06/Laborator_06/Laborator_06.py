# LABORATOR 06 - Fisiere si Exceptii

# Se citeste de la tastatura 2 numere naturale. Sa se trateze cazul impartirii la 0.
# Sa se afiseze un mesaj ciorespunzator intr-un fisier.

f = open("TextFile1.txt","r")

str = f.read()
print(str);

#valorile trebuie sa fie separate dupa spatiu
numbers = str.split()

#convertim valorile in tipul de date int
a = int(numbers[0]);
b = int(numbers[1]);

#print(a)
#print(b)
f.close()
def division(a, b):
    # use the try statement where error may occur
    try:
        print(a/b)
    # if the error occurs, handle it !!
    except ZeroDivisionError:
        print("Cannot divide by Zero!!")
		# if no error occurs		
    else:
        print("No Error occured!!")

division(a,b);
