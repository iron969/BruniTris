A=["__","__","__"]
B=["__","__","__"]
C=["__","__","__"]

print("inserisci le coorrdinate in: numero riga, posizione , simbolo")
print("puoi solo usare x e o")
print("per smettere di giocare premere b")
print(A)
print(B)
print(C)

while True:
    n=3

    coordinate = []

    for i in range(n):
        x=input()
        coordinate.append(x)

    c1=coordinate[0]
    c2=coordinate[1]
    s=coordinate[2]

    if c1 =="b":

        print("grazie per aver giocato")
        break

    elif int(c1)==1:
     A[int(c2)-1]=s

    elif int(c1)==2:
       B[int(c2)-1]=s

    elif int(c1)==3:
        C[int(c2)-1]=s

    if A[0]==B[0]==C[0]!="__"or A[1]==B[1]==C[1]!="__" or A[2]==B[2]==C[2]!="__"or \
        A[0]==A[1]==A[2]!="__" or B[0]==B[1]==[2]!="__"or C[0]==C[1]==C[2]!="__" or \
        A[0]==B[1]==C[2]!="__" or A[2]==B[1]==C[0]!="__":

        print("cè un vincitore")
        print(A)
        print(B)
        print(C)
        break

    print(A)
    print(B)
    print(C)
