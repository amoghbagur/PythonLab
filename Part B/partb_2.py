storetemp=[]
def fartocel(deg):
	ans=(deg-32)*(5/9)
	storetemp.append((deg,ans))
	return ans
def celtofar(deg):
	ans=deg*(9/5)+32
	storetemp.append((deg,ans))
	return ans
while(True):
    print("1.Convert to celsius\n2.Convert to fahrenheit\n3.Show all conversions\n4.Exit")
    ch=int(input("Enter choice:"))
    if ch==1:
    	deg=float(input("Enter temperature in fahrenheit:"))
    	print(fartocel(deg),"Celsius")
    elif ch==2:
    	deg=float(input("Enter temperature in celsius:"))
    	print(celtofar(deg),"Fahrenheit")
    elif ch==4:
        exit()
    elif ch==3:
        print('Choose sorting method:\n1.From value\n2.To value')
        ch1=int(input("Enter choice:"))
        if ch1==1:
            for i in sorted(storetemp,key = lambda x:x[0]):
                print(i)
        elif ch1==2:
            for i in sorted(storetemp,key = lambda x:x[1]):
                print(i)
        else:
            print('Invalid Choice')
    else:
        print("Invalid choice")
