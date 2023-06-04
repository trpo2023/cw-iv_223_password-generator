import random
import Lib 

try:
    com=input()
except EOFError:
    com="pwgen"
    print("Exception handled")

upr, lwr, dgt, smb, amb, col = True, True, True, True, False, False
arg, lenth, numb="",10,50

if com[:5]=="pwgen":
    pases=[]
    i1,i2,i3=divide(com)
    arg,lenth,numb = args(com,i1,i2,i3)
    upr, lwr, dgt, smb, amb, col = restr(arg, upr, lwr, dgt, smb, amb, col)
    useable = aloud(upr, lwr, dgt, smb, amb)
    for i in range(0,numb+10,+1):
        pases.append(gen(useable,lenth))
    
    if col:
        for i in range(0,numb,+5):
            print(pases[i],"\t",pases[i+1],"\t",pases[i+2],"\t",pases[i+3],"\t",pases[i+4])
    else:
        for i in range(0,numb,+1):
            print(pases[i])

else:
    print(0)
