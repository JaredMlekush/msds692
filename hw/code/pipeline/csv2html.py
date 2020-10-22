
import sys
import mycsv

header, data = mycsv.readcsv(mycsv.getdata())

print("<html>")
print("<body>")
print("<table>")

i = 0
head = '<tr>'
while i < len(header):
    x = f"<th>{header[i]}</th>"
    head += x
    i += 1
head += '</tr>'
print(head)

for rows in data:
    i = 0
    htmlrow = '<tr>'
    while i < len(rows):
        x = f"<td>{rows[i]}</td>"
        htmlrow += x
        i += 1
    htmlrow += '</tr>'
    print(htmlrow)

print("</table>")
print("</bdy>")
print("</html>")

