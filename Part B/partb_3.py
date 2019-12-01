class Smanu:
    def __init__(self,str1=None):
        self.str1=str1
    def reversestr(self):
        l=self.str1.split(" ")
        l.reverse()
        return " ".join([str(x) for x in l])
l=[]
for i in range(3):
    print("Enter string ",i+1,": ")
    l.append(Smanu(str(input())))
l2=[x.reversestr() for x in l]
def sortvowels(st):
    st.lower()
    vowels=['a','e','i','o','u']
    count=0
    for i in st:
        if i in vowels:
            count=count+1
    return count
l2.sort(key=sortvowels, reverse=True)
for i in l2:
    print(i)
