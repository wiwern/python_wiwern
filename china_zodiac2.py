def china_zodiac():
    year =int(input("wprowadź rok: "))
    
    if year % 12 == 0:
        print("małpa")
    elif year % 12 == 1:
        print("kogut")
    elif year % 12 == 2:
        print("pies")
    elif year % 12 == 3:
        print("dzik")
    elif year % 12 == 4: 
        print("szczur")
    elif year % 12 == 5: 
        print("bawół")
    elif year % 12 == 6:
        print("tygrys")
    elif year % 12 == 7:
        print("królik")
    elif year % 12 == 8:
        print("smok")
    elif year % 12 == 9:
        print("wąż")
    elif year % 12 == 10:
        print("koń")
    elif year % 12==11: 
        print("koza")
    
def main():
    
    while True:
        quest=input('czy chcesz sprawdzić rok w chińskim kalendarzu: t/n ').lower()
        if quest == 't':
            china_zodiac()
        elif quest in ['n', 'nie']:
            break
        else:
            print('nie rozumiem')

main()
    
