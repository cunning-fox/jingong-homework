Python 3.7.1rc1 (v3.7.1rc1:2064bcf6ce, Sep 26 2018, 14:21:39) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[]
>>> for m in range(1,2001):
	b=[]
	for n in range(1,m):
		if(m%n==0):
			b.append(n)
	if(m==sum(b)):
		a.append(m)

		
>>> a
[6, 28, 496]
>>> 
