#TP1

annee = input("Saisissez une année: ");
annee = int(annee);
bix = True;
if (annee % 4) != 0:
    bix = False;
elif (annee % 100) == 0:
    var = annee % 400;
    if var == 0:
        bix = True;
else:
    bix = True;

if bix:
    print (annee, "est une année bissextile");
else:
    print(annee, "n'est pas une année bissextile");
        