# LABORATOR 05

# Se dau 3 puncte in plan cu coordonate aleatoare - valori intregi.
# Sa se determine Aria triunghiului determinat de cele 3 puncte daca ele NU sunt coliniare.
# Sa se determine ecuatia celor 3 laturi ale triunghiului 

import random
import math
global xA, yA, xB, yB, xC, yC, coliniaritate;

def ecuatia_laturii(x1,y1,x2,y2):
        coef_a = y1 - y2;
        coef_b = x2 - x1;
        coef_c = x1*y2 - x2*y1;
        
        if coef_b > 0 and coef_c > 0:
            print(coef_a,"X + ",coef_b,"Y + ",coef_c);
        elif coef_b > 0 and coef_c < 0:
            print(coef_a,"X + ",coef_b,"Y - ",abs(coef_c));
        elif coef_b < 0 and coef_c > 0:
            print(coef_a,"X - ",abs(coef_b),"Y + ",coef_c);
        elif coef_b < 0 and coef_c < 0:
            print(coef_a,"X - ",abs(coef_b),"Y - ",abs(coef_c));

# coordonate punct A
xA = random.randint(-50, 50);
yA = random.randint(-50, 50);
print("A(",xA,",",yA, ")");

# coordonate punct B
xB = random.randint(-50, 50);
yB = random.randint(-50, 50);
print("B(",xB,",",yB, ")");

# coordonate punct C
xC = random.randint(-50, 50);
yC = random.randint(-50, 50);
print("C(",xC,",",yC, ")");

coliniaritate = (xA*yB + xB*yC + xC*yA - xC*yB - xA*yC - xB*yA);
if coliniaritate == 0:
    print("Punctele sunt coliniare.");
else:
       aria = abs(coliniaritate)/2;
       print("Aria triunghiului este: ", aria);
       print();

       print("Ecuatia dreptei AB: "); ecuatia_laturii(xA,yA,xB,yB); print();
       print("Ecuatia dreptei BC: "); ecuatia_laturii(xB,yB,xC,yC); print();
       print("Ecuatia dreptei AC: "); ecuatia_laturii(xA,yA,xC,yC); print(); print();

 
