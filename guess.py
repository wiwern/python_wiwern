import time
import sys
name=raw_input('what\'s Your name?   ')
print 'hello ' +name
like2=raw_input('Do You like history?\n type y [for yes] or n [for no]')
if like2=="y":
    print 'that\'s fine'
elif like2=="n":
    print 'sorry to hear it'
    time.sleep (1)
    print 'by, then'
    sys.exit(0)
else: print 'that is no answer'
time.sleep(1)
print 'try again'