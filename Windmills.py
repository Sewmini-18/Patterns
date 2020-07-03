#Windmills pattern
number = input("Enter Number: ")
n =int(number)

pat ="o "
mpat="x "
print("  ")
for i in range(n,0,-1):
    for s in range(0,n+1,1): print("  ",end="")
    for j in range(0,i-1,1): print("  ",end="")
    for k in range(n,i-1,-1): print(pat,end="")
    print("")

for i in range(1,n+1,1):
    for j in range(1,i+1,1): print("  ",end="")
    for s in range(n,i-1,-1): print(pat,end="")

    for k in range(1,n+1,1):
        if(i==1 or k==n or k==1 or i==n or k==i or i==n-k+1):
            print(mpat,end="")
        else: print("  ",end="")
    
    for j in range(1,i+1,1): print(pat,end="")
    print("")
    
for i in range(n+1,-1,-1):
    for s in range(0,n+1,1): print("  ",end="")
    for j in range(0,i-1,1): print(pat,end="")
    if(i!=0):print("")
    
