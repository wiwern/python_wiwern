def alc():
    gram=0
    sgram=0
    i=int(input('Ile rodzajów napojów alk. piłeś? '))
    for x in range(0,i):
        x=float(input('jak mocny jest napój- w procentach? '))
        y=float(input('ile wypiłeś, w litrach? '))
        sgram=(x/100)*(y*1000)*0.79
        sgram=round(sgram,1)
        print('w napoju było %s gram alkoholu' %sgram)
        gram+=sgram
    gram=round(gram,1)
    print('łącznie wypiłeś %s gram alkoholu' %gram)
    return gram

               

def promil(gram):
    waga=float(input('ile ważysz? '))
    sex=input('podaj płeć m/k ').lower()
    if sex=='m':
        ustr=waga*0.7
        if gram>40:
            print('Uwaga- bezpieczna ilość alkoholu dla mężczyzn to mniej niż 40 gram')
    elif sex=='k':
        ustr=waga*0.6
        if gram>20:
            print('Uwaga- bezpieczna ilość alkoholu dla kobiet to mniej niż 20 gram')
    promil=gram/ustr
    promil=round(promil,2)
    print('po spożyciu masz %s promila we krwi' %promil)
    


    

def main():
    gram=alc()
    promil(gram)

main()

    
