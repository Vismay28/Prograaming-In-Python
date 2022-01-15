#20CE154 Vismay Vachhani
#creating a tuple
kalpesh = (7, 1, 0, 55, 33, 17)
print(kalpesh)
#using merge of tuples with the + operator you can add an element and it will create a new tuple, because tuples are immutable
kalpesh =kalpesh + (94,)
print(kalpesh)
#adding items in a specific index
kalpesh= kalpesh[:5] + (25, 2, 56) + kalpesh[:5]
print(kalpesh)
#converting the tuple to list
listx = list(kalpesh)
#use different ways to add items in list
listx.append(30)
kalpesh = tuple(listx)
print(kalpesh)