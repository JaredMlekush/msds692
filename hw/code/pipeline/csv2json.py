import sys
import mycsv

header, data = mycsv.readcsv(mycsv.getdata())

print("{")
print(f"\"headers\":[")
for col in header:
    print(f'"{col}"', end = ', \n')
print('],')
print("\"data\":[ \n {")


for i, row in enumerate(data):
    new = list(zip(header, row))
    for i, pairs in enumerate(new):
        print(f'"{pairs[0]}":"{pairs[1]}"', end=',')
    if i ==1:
        print('\n},')
    else:
        print('\n},', '\n{')
print(']')
print('}')

