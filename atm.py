# atm
''' this is a atm project'''
a='''1.withdraw balence
2.deposit
3.check balence
4.exit'''

name="sharath"
password=513
print("welcome to sharath national bank")
user_name=(input("enter the name:"))
user_password=int(input("enter the password:"))
while True:
    if user_name == name and user_password == password:
        print(a)
        option=int(input("enter the option 1 to 4:"))
        balence=1000
        if option == 1:
            debit_amount=int(input("enter the amount:"))
            if debit_amount<=0:
                print("enter the possitive number")
            elif debit_amount<=balence:
                balence-=debit_amount
                print("your withdrawl sucessful ")
                print(f"current balence is: {balence}")
            else:
                print("invalid funds")
              
             
        elif option== 2:
            creadit_amount=int(input("enter the amount:" ))
            if creadit_amount<=0:
                balence+=creadit_amount
                print("your deposit amount is deposited sucessfully")
                print(f"current balence is: {balence}")
            else:
                print("invalid transactons ")

        elif option== 3:
            print(f"current balence is {balence}")

        elif option== 4:
            print("thank you for visiting our bank")
        else:
            print("invalid option!  choose correct option")
            break

    else:
        print("invalid user_name and password")


 

       
    

