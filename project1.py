import random
computer = random.choice([1,0-1])
youstr = input("Enter your choice: ")
youDict={"s":1,"w":0,"g":-1}

reverseDict={1:"snake" , 0: "water" , -1:"gun"}

you= youDict[youstr]
print(f"You chose {reverseDict[you]} \n Computer choose {reverseDict[computer]}")

if(computer==you):
    print("It's a draw ")
else:
    if(computer==-1 and you ==1):
        print("you win")
    elif(computer==-1 and you ==0):
        print("you Lose")
    elif(computer==1 and you == 0):
         print("you win")
    elif(computer==1 and you ==-1):
        print("you Lose")
    elif(computer==0 and you == -1):
         print("you win")
    elif(computer==0 and you ==1):
        print("you Lose")
    else:
        print("something went wrong ")
