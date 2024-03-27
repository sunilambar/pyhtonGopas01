def add(a,b):
    return a+b

number=123
names=['eva', 'adam']

def greeting():
    print("hello")

def validate_city_line(line,delimiter=','):
    x=line.split(delimiter)
    if len(x)!=3:
        return None,None,None
    if not ( x[0].isascii() and x[0].isupper() and len(x[0])==2): #checks country code
        return None,None,None
    if not (len(x[2])>0 and x[2].isdigit()): #checks population
        return None,None,None
    if not( len(x[1])>1 and x[1][0].isupper() and x[1][1:].islower() ): #check city name
        return None,None,None
    return x