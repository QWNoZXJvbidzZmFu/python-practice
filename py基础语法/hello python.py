people=['a','b','c','d','e','f','g']
people[1]='e'
people.insert(0,"h")
people.insert(3,"i")
people.append("j")
print(people)
people.sort()
print(people)
print(len(people))
for peoples in people:
    print(peoples)