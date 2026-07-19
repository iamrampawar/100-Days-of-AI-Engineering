fruits = ["apple","banana","mango","Orange"]

for fruit in fruits:
    print(fruit)

    #method-2:

fruits = ["apple","banana","mango","Orange"]
for i in range(len(fruits)):
    print(i,fruits[i])

    #method-3:

fruits = ["apple","banana","mango","Orange"]
for index , fruit in enumerate(fruits):
    print(index,fruit)
