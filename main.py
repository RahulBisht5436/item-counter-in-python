
li = []
for y in range(1,100):
   z=input("enter element \n")
   li.append(z)
   z=input ("do you want to enter other element \n")
   if z=="no":
     break
   else:
     pass  

l2 = (set(li))
l3 = []
for x in l2:
    print(f"{x} is repeated {li.count(x)} times \n")
    l3.append(li.count(x))
print("items \n")
print(set(li))
print("\n")
print("items repetation \n")
print(l3)
