num = int(input("Enter the range: \t "))
 
# i loop for height of the triangle
# j loop for printing star '*'
# s loop for printing space ' '

#function 1
def traingle1():
    for k in range((num - i) - 1): print(end=" ")
    for j in range(i + 1): print("*", end=" ")       

        
#function 2
def traingle2():
  for l in range((i-1) + 1): print(end=" ") 
  for j in range(num-i): print("*", end=" ")
        

#function 3
def space():
    for s in range((num)): print(end="  ")     


#printing pattern using 4 steps
#1        
for i in range(num):
    space()
    traingle1()
    print()

#2       
for i in range(num):
    traingle2()
    space()
    for r in range((i-1) + 1): print(end=" ")
    traingle2()  
    print()

#3
for i in range(num):
    traingle1()
    for j in range((num - i) - 1): print(end=" ")    
    space()
    traingle1()
    print()

#4
for i in range(num):
    space()
    traingle2()
    print()
    