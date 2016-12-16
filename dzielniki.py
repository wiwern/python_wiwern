def dziel(x):
    dziel=[]
    for i in range(1,x):
        a=x%i
        if a==0:
            dziel.append(i)
    print (dziel)
    print(len(dziel))

liczba=int(input('jakiej liczby dzielników szukasz? '))
dziel(liczba)

