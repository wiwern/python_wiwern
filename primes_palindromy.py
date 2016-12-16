def prime():
    #szuka liczb pierwszych w podanym zakresie
    start = int(input("Podaj od jakiej liczby szukasz liczb pierwszych: "))
    stop= int(input("Podaj do jakiej liczby szukasz: "))
    primes=[]

    for num in range(start,stop + 1):
       # liczby pierwsze są większe niż 1
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               primes.append(num)
    if len(primes)>100:
        pyt=input('czy chcesz wydrukować listę liczb pierwszych -liczy ponad 100 elementów? t/n ').lower()
        if pyt=='t':
            print('To są liczby pierwsze w podanym zakresie')
            print(primes)
    return primes


def palindromes(primes):
    palindrom=[]
    for x in primes:
            a=[int(i) for i in str(x)]#zamiana liczby na listę
            if a==a[::-1]:#sprawdzenie czy lista jest taka sama 'z przodu'
                #jak i 'z tyłu'
                palindrom.append(a)
    print('To są liczby pierwsze - palindromy w podanym zakresie:')
    print(palindrom)
            

def main():
    primes=prime()
    palindromes(primes)

def startowa():
    print('Program autorstwa wiwern: szuka liczb pierwszych będących palindromami')
    while True:
        pyt=input('czy chcesz uruchomić program PALINDROMY-liczby pierwsze t/n ').lower()
        if pyt in ['t', 'tak']:
            main()
        elif pyt in ['n', 'nie']:
            break
        else:
            print('nie rozumiem')

startowa()
