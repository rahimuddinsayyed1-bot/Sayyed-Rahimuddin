a=int(input("enter a value"))
b=int(input("enter b value"))
print('add:',(a+b))
print('sub:',(a-b))
print('mul:',(a*b))
print('div:',(a/b))
print('mod:',(a%b))
print('pow:',(a**b))
print(a==b)
print(a>b)
print(a<b)
print(a!=b)
if(a>b):
    print(a)
else:
    print(b)
l=[2,4,6,4,7]
print("for loop:")
for i in l:
    print(i)

print("while loop:")
i=0
while i< len(l):
    print(l[i])
    i=i+1  

dict={"name":"Rahimuddin","Age":21,"Branch":"Aim"}
list=[1,2,3,4,5]
tuple=(1,2,3,4,5)
set={1,2,3,4,5}

print("\n",dict,"\n",list,"\n",tuple,"\n",set)