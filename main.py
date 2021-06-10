

database = {
    "rahulbisht5436@gmail.com": "infiniteismygoal5436",
    "tsdhgfhkuheuwhefjd": "jgjhsdhggjgdgfgjsj",
    "jygyffgidshdfhetugsdhbd": "hgjchsdgjjhgsdjhgf",
    "uayggfcjdkhsieuygbjjkgjgjdg": "ghgdfgdjgsjgdugbjshhd",
    "1234": "1234"
}
suspension_bit = 0

while True:
    x = input("enter user id\n")
    y = input("enter password\n")
    ques = input("do you want access yes/no \n")
    if ques == "yes":
        for c, v in database.items():
            if c == x and v == y:
                print("permission granted\n")
                permission_bit = True
            else:
                permission_bit = False
        if permission_bit == False:
            print("permission not granted\n")
            ques = input("do you want to continue\n")
            if ques == "yes":

                suspension_bit += 1
                if suspension_bit > 4:
                    print("suspicious behaviour detected")
                    break
                continue
            else:
                break

    break
if permission_bit==True:
  print("you are logged in ")
  print("""
        *
       * *
      * * *   
    * * * * * 
        ||
        ||
        ||
  """)
input(hold)
