print('ten program testuje wiedzę historyczną')
studenci={}

while True:
    points=0
    fails=0
    ocena=0
    
    print('czy chcesz zdawać test? Tak lub Nie')
    dec=input()
    if dec in ['nie', "NIE", "Nie", 'n']:
        break
    else:
        print('Podaj nazwisko')
        name=input()
        print('podaj imię')
        fname=input()
        print('Cześć %s!' %fname)
        while True:
            print('Kiedy miał niejsce Chrzest Polski?')
            odp1=input()
            if odp1 in ['966', 966]:
                print('Bardzo dobrze!')
                points=points +1
                break
            else:
                print('źle!')
                fails+=1
                break

        while True:
            print('Kiedy miała miejsce bitwa pod Legnicą?')
            odp1=input()
            if odp1 in ['1241', 1241]:
                print('Bardzo dobrze!')
                points=points +1
                break
            else:
                print('źle!')
                fails+=1
                break

        while True:
            print('Kiedy ogłoszono Konstytucję 3 maja?')
            odp1=input()
            if odp1 in ['1791', 1791]:
                print('Bardzo dobrze!')
                points=points +1
                break
            else:
                print('źle!')
                fails+=1
                break

        while True:
            print('''Kiedy Polska odzyskała niepodległość, podaj rok?''')
            odp1=input()
            if odp1 in ['1918', 1918]:
                print('Bardzo dobrze!')
                points=points +1
                break
            else:
                print('źle!')
                fails+=1
                break
        while True:
            print('''Kiedy wybrano sejm kontraktowy''')
            odp1=input()
            if odp1 in ['1989', 1989]:
                print('Bardzo dobrze!')
                points=points +1
                break
            else:
                print('źle!')
                fails+=1
                break

        if fails==0:
            print('bardzo dobrze, odpowiedziałeś dobrze %s razy, nie pomyliłeś się ani razu' %points)
        else:
            print('W teście odpowiedziałeś poprawnie %s, pomyliłeś się %s razy' %(points, fails))

        if fails>=points:
            print('oblałeś test')
        else:
            print('zdałeś test')
        a=points/5*100
        print('odpowiedziałeś na %s procent pytań' %a)

        if a==100:
            ocena=ocena +5
        elif a<100 and a>=75:
            ocena=ocena +4
        elif a<75 and a>50:
            ocena+=3
        elif a<50:
            ocena=2
        print('otrzymałeś ocenę równą %s' %ocena)
        studenci[(name, fname)]=ocena
        print(studenci)


print(studenci)
studenci2=str(studenci)
students=open('students2.txt', 'w')
students.write(studenci2)
students.close()
oceny=list(studenci.values())
import statistics as s
srednia=s.mean(oceny)
print('średnia ocen to %s' %srednia)



