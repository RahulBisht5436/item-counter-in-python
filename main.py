# # # # # exercise

# # # # question 1
# # # string=input("type")

# # # i=0
# # # j=0
# # # k=0

# # # x=len(string)
# # # for z in range(0,x):

# # #     for y in range(0,x):
# # #       if string[i]==string[j]:
# # #         j+=1
# # #         k+=1
# # #       else:
# # #         j+=1
# # #       print(f"{string[i]}:{k}")
# # #       i+=1

# # # i=0

# # # li=[1,2,"rahul",'a','t',3,4,5,]
# # # print(li[2:7:2])
# # # print(li)
# # # x=len(li)
# # # for x in range(0,x):
# # #   if li[i]=="rahul":
# # #     li[i]="bisht"

# # #   else:
# # #     pass
# # #     i+=1
# # # print(li)
# # li=[[1,2,3,4,4,4],"rahul",1,2,3,4]
# # print(li[0][2])
# # li.append(1000000000000)
# # li[0].insert(4,57654)
# # li.pop()
# # li.pop()
# # li.remove(3)
# # print(list(range(1,101)))
# # print(li)
# # # print(li.index(57654))
# # print(li[0].count(4))
# # li2="     ".join(["a","b","c"])
# # print(li2)

# x="ugyggdgsc"
# d1={
#   "a":1,
#   "bisht":"rahul",
#   "rahul":["a","b","c"],
#   x:"gjjhghgf"
# }

# print(d1[x])
# print(x)
# d2=d1.keys()
# print(d2)
# y=input("what is value\n")

# z=(y in d1)
# if z== False:
#   print("it doesnt exist\n")
#   k=input("do you want to add it??\n")
#   if k=="yes":
#     value=input("give value\n")
#     d1[y]=value
#     print(d1)
#   else:
#     pass
# else:
#   print("it exist")
# x=input("")
# print("z") if x=="rahul" else  print("jgjhgxdf")
# magician=False
# expert=True

# if magician and expert:
#   print("expert magician")
# elif magician:
#   print("you are magician")
# else:
#   print("you need magic")
# dict={
#   "name":"rahul ",
#   "roll no":190095010064,
#   "class":"stcs"
# }

# print(dict.keys() )
# for x in dict.items():
#   print(x )
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
