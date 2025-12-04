print("liczenie pola wpisz liczbe")
print("1-kwadrat,2-trójkąt,3-koło,4-prostokąt")
numer=int(input("numer"))
a=int(input("podaj bok"))
h=int(input("podaj wysokość"))
b=int(input("podaj drugi bok"))
r=int(input("podaj promień"))
if numer==1:
  wynik=a*a
  print("pole", wynik)
elif numer==2:
  wynik=a*h/2
  print("pole", wynik)
elif numer==3:
  wynik=3.14*r*r
  print("pole", wynik)
elif numer==4:
  wynik=a*b
  print("pole", wynik)
else:6
print("nie ma takiej figury")