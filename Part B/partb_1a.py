l1=[]
def unique(num):
	newnum=[]
	for i in num:
		if i not in newnum:
			newnum.append(i)
	return newnum
n=int(input("Enter the number of elements:"))
for i in range(n):
	l1.append(int(input("Enter element: ")))
l2=unique(l1)
print(l2)
l3=[x**2 for x in range(n)]
print(l3)
l4=[x for x in l3 if x%2==0]
l4.reverse()
print(l4)
