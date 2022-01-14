#!/usr/bin/python3

dict = {"obst":[], "menge":[], "price":[]}

b = list(dict.values())

name = b[0]

quantity = b[1]

price = b[2]

cost = 0
totalcost = 0
coasta=0
t_cost=0
#print("in order to leave the program and to see your shopping list PRESS 'AA'")

a = True
while a == True:
    x= input("Which product would you like to add to the shopping list ? ")
    if x == "AA" :
        break
    else :
        name.append(x)

    y= input("In which amount would you like to have ? ")
    if y == "AA" :
        break
    else :
        y = int(y)
    quantity.append(y)

    c = input("What is unit price of the item in Euro ? ")
    if c == "AA" :
        break
    else :
        c = int(c)
    price.append(c)
    cost= y * c
    totalcost = totalcost + cost

    for i in range(len(name)) :
        print(f"""Product :: {name[i]}45 Quantity :: {quantity[i]}Price :: {price[i]} """)

    # print(f"Product :: {name[i]} Quantity :: {quantity[i]} Price :: {price[i]} sep='\n'")

        print(f"Total cost = {totalcost} Euro")
        print(dict)

    for i in range(len(quantity)) :
        costa = quantity[i] * price[i]
        t_cost =t_cost + costa
        print(t_cost)
