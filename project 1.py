import random
def game(camp,you):
    if camp == you:
        return None    
    elif camp=="snake":
        if you=="water":
            return False
        elif you=="gune":
            return True    
    
    elif camp == "water":
        if you=="gune":
            return False
        elif you=="snake":
            return True
    elif camp=="gune":
        if you=="snake":
            return False
        elif you=="water":
            return True
print("camputer tern:Snake(snake) or Water(water) or Gune(gune) ? ")
randNo =random.randint(1,3)
if randNo==1:
    camp="snake"
elif randNo ==2:
    camp="water"
elif randNo ==3:
    camp ="gune"

you =input("your tern : Snake(snake) Water(water) or Gune(gune)")
a = game(camp,you)
print (f" computer choose: {camp}")
print(f"you choose :  {you}")
if a==None:
    print("the game is tie")
elif a:
    print("You Win !")
else:
    print("You lose !")                 




