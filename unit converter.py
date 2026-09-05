#Convert your no. or value into meter,centim,inches,feet

print ("  ")
print ("="*100)
a = "m to cm" 
b="km to m"
c="km to cm"
d= "m to km"
e= "cm to m"
f= "cm to km"
g="f to i"
h="i to f"


print("----please enter your digit/number and operataions----") 

user=int(input("enter your digit:-  "))
#task to do 

while True:
    task=input("please type yoour operation(like:-m to cm, f to i (for feet to inches)):-  ")
    task=task.lower().strip()
    if task==a:
        print("your answer in cm is :-",user*100)
        break
    if task==b:
        print("your answer in m :- ",user*1000)
        break
    elif task==c:
        print("your answer in cm is :- ",user*100000)
        break
    elif task==d:
        print("your answer in km is :- ",user/1000)
        break
    elif task==e:
        print("your answer in m is :- ",user/100)
        break
    elif task==f:
        print("your answer in km is :- ",user/100000)
        break
    elif task==g:
        print("your answer in inches is:- ",user*12)
        break
    elif task==h:
        print("your answer in feets is :- ",user/12)
        print("="*100)
        break
    else:
        print("please check your operations if it is correcrt then check spacing")
    
print("thanks for using ")
print(" ")
print("="*100)