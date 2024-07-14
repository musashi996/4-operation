x=int(input("1. number: "))
y=int(input("2. number: "))
i=int(input("(1(+),2(-),3(/),4(*)) operation: "))
t=int
if i==1:
    t=x+y
elif i==2:
    t=x-y
elif i==3:
    t=x/y
elif i==4:
    t=x*y
else:
    print("error")
    
print(t)
