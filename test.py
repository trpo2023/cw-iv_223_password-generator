import random
import Lib

upr, lwr, dgt, smb, amb, col = True, True, True, True, False, False
arg, lenth, numb="",10,50

tests=[" ","pwgen qigurfhfehquw","pwgen -aAS0 -10 -10","pwgen - -0 -","pwgen ---0"]

for l in range(0,5,+1):
	try:
		com=tests[l]
		print(com)
		if com[:5]=="pwgen":
			pases=[]
			i1,i2,i3=Lib.divide(com)
			arg,lenth,numb = Lib.args(com,i1,i2,i3)
			upr, lwr, dgt, smb, amb, col = Lib.restr(arg, upr, lwr, dgt, smb, amb, col)
			useable = Lib.aloud(upr, lwr, dgt, smb, amb)
			for i in range(0,numb+10,+1):
				pases.append(Lib.gen(useable,lenth))
			
			if col:
				for i in range(0,numb,+5):
					print(pases[i],"\t",pases[i+1],"\t",pases[i+2],"\t",pases[i+3],"\t",pases[i+4])
			else:
				print("Test ", l , "passed succesfully")
		
		else:
			print(0)
	except Exception as e:
		print(e)
