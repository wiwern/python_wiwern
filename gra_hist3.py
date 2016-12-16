score=0
fails=0
print('Jak ma na imię?')
name=input()
while True:
    print('Podaj rok chrztu Polski?')
    pyt1=input()
    if pyt1 in [966, '966']:
        print('Bardzo dobrze %s' %name)
        score+=1
        break
    
    elif pyt1 != 966 or pyt1!="966":
        print('Źle!')
        fails+=1

while True:
    
        
    
    
