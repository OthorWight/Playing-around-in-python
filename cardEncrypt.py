import math
import hashlib


print(hashlib.sha1(b"salt" + b"1").hexdigest())

#i = pow(5915587277,-1)
#def cardEncrypt(n):
#	return pow(n,5915587277, 1234567890)
#for x in range(1,53):
#	y = cardEncrypt(x)
#	z = pow(int(y),int(i), 1234567890)
#	print (str(x) + " = " + str(y) + " = " + str(z))
