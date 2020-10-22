import sys

def getdata():
    if len(sys.argv)==1: # if no file given, read from stdin
        data = sys.stdin.read()
    else:
        f = open(sys.argv[1], "r")
        data = f.read()
        f.close()
    return data.strip()

def readcsv(data):
    """
    Read CSV with header from data string and return a header list
    containing a list of names and also return the list of lists
    containing the data.
    """
    data =  data.strip()
    data.split()
    rows = data.split()
    allrows = []
    for row in rows:
        allrows.append(row.split(','))
   
    header =allrows[0]
    data = allrows[1:]
    return header, data
