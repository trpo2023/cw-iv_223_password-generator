UC_let = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LC_Let = UC_let.lower()
digits = "0123456789"
symbols = "(){}[]<>.,/|@!#$%^&*"
LokLik = "l|I10Oo8B"

def StrSub(str1,str2):
    for i in range(0,len(str2)-1,+1):
        str1=str1.replace(str2[i],'')
    return str1

def divide(inp):
    i=4
    i1,i2,i3=-1,-1,-1
    while inp[i]!='-':
        if i<len(inp)-1:
            i+=1
        else:
            break
    if(inp[i]=='-'):
        i1=i
    if i<len(inp)-1:
        i+=1
    else:
        return i1+1, i2+1, i3+1
    while inp[i]!='-':
        if i<len(inp)-1:
            i+=1
        else:
            break
    if(inp[i]=='-'):
        i2=i
    if i<len(inp)-1:
        i+=1
    else:
        return i1+1, i2+1, i3+1
    while inp[i]!='-':
        if i<len(inp)-1:
            i+=1
        else:
            break
    if(inp[i]=='-'):
        i3=i
    return i1+1, i2+1, i3+1

def args(inp,i1,i2,i3):
    arg1=''
    arg2=''
    arg3=''
    if (i1!=0) and (i2!=0):
        arg1=inp[i1:i2-1]
    elif (i1!=0) and (i2==0):
        arg1=inp[i1:]
    if (i2!=0) and (i3!=0):
        arg2=inp[i2:i3-1]
    elif (i2!=0) and (i3==0):
        arg2=inp[i2:]
    if (i3!=0):
        arg3=inp[i3:]
    if arg1=='':
        arg1=" "
    if arg2=='':
        arg2=10
    if arg3=='':
        arg3=50
    return arg1, int(arg2), int(arg3)

def restr(inp, upr, lwr, dgt, smb, amb, col):
    i=0
    while i<len(inp):
        if inp[i]=='0':
            dgt=False
        if inp[i]=='A':
            upr=False
        if inp[i]=='S':
            smb=False
        if inp[i]=='a':
            lwr=False
        if inp[i]=='B':
            amb=True
        if inp[i]=='C':
            col=True
        i+=1
    return upr, lwr, dgt, smb, amb, col

def aloud(upr, lwr, dgt, smb, amb):
    useable = ""
    if upr:
        useable += UC_let
    if lwr:
        useable += LC_Let
    if dgt:
        useable += digits
    if smb:
        useable += symbols
    if amb:
        useable = strsub(useable,LokLik)
    return useable

def gen(use,lent):
    pas=""
    for i in range(0,lent,+1):
        try:
            pas+=use[random.randint(0,len(use)-1)]
        except:
            pas+=' '
    return pas
