import sys
import mycsv

header, data = mycsv.readcsv(mycsv.getdata())

for i, value in enumerate(header):
    header[i] = value.replace(' ', '_')

x = ','.join(header)

print('<?xml version="1.0"?>')
print('<file>')
print(f'<headers>{x}</headers>')
print('<data>')
for row in data:
    new = list(zip(header, row))
    print('<record>')
    for i, pair in enumerate(new):   
        print(f'  <{pair[0]}>{pair[1]}</{pair[0]}>', end='')
    print('\n</record>')
print('</data>')
print('</file>')
