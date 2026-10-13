current_number=0
while current_number<10:
    current_number+=1
    if current_number%2==0:
        continue       #break退出while循环，continue退出单步循环
    print(current_number)

responses={}
active=True
while active:
    name = input("What is your name?")
    response = input("Which mountain would you like to climb someday?")
    responses[name]=response
    repeat = input("Would you like to let another person respond?(Yse/No)")
    if repeat.lower()=="no":
        active=False
for name,response in responses.items():
    print(f"\n{name} would like to climb {response}")