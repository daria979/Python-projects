# LABORATOR 04

#Sa se scrie primele n patrate perfecte folosindu-se dictionarul

n=int(input("Introdu un numar: "));
dictionary = dict()

for x in range(1,n+1):
    dictionary[x]=x*x;

print();
print(dictionary);
