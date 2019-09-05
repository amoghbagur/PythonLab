stud={1:'Asha',2:'Dutt',3:'Rekha',4:'Amogh'}
list1=["Value2","Value2","Value3","Value4"]
list2=[""]
i=0
j=0
k=0
for i in stud:
print('key is',i,'value is',stud[i])
list1[j]=stud[i]
list2[k]=i
j=j+1

print( 5 in list1)
print(list2)
print(stud.keys())
print(stud.values())
print(stud.items()