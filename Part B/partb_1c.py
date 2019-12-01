l1=[]
def findmax(l=[]):
    if len(l)==0:
        return 0
    else:
        return max(l[0],findmax(l[1:]))
n=int(input("Enter the number of elements:"))
for i in range(n):
	l1.append(int(input("Enter element: ")))
print('Max value:',findmax(l1))
