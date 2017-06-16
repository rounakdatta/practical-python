import matplotlib.pyplot as plt

ycount=[]
xnumber=[]

for i in range(1,100000):
	n=i
	c=0
	xnumber.append(n)
	while(n!=1):
		if(n%2==0):
			n/=2
			c+=1
		else:
			n=(n*3)+1
			c+=1
	ycount.append(c)
#print("\n",xnumber)
#print("\n",ycount)

plt.plot(xnumber, ycount, 'ro')
plt.xlabel('number')
plt.ylabel('cc value')
plt.show()
