#!/usr/bin/python3
import time 

zeit = time.gmtime()
stunde = zeit[3]
minute = zeit[4]
sekunde = zeit[5]

#if stunde >= 7 and stunde <12:
if stunde > 21:
    print(f'Gute Nacht, es ist jetzt {stunde}:{minute}:{sekunde}')
elif stunde > 17:
    print(f'Guten Abend, es ist jetzt {stunde}:{minute}:{sekunde}')
elif stunde > 13:
    print(f'Guten Tag, es ist jetzt {stunde}:{minute}:{sekunde}')
elif stunde > 11:
    print(f'Guten Mittag, es ist jetzt {stunde}:{minute}:{sekunde}')
elif stunde > 6:
    print(f'Guten Morgen, es ist jetzt {stunde}:{minute}:{sekunde}')
elif stunde >= 0:
    print(f'Gute Nacht, es ist jetzt {stunde}:{minute}:{sekunde}') 

print(f'{stunde}:{minute}:{sekunde}') 
