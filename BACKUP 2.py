#fruit
fruitlist=["apple","orange","banana","grape","tomato","mango"]
print(fruitlist[0],fruitlist[4])
print(fruitlist[1:3])

#fruitappend
fruit=["apple","orange","banana","grape","tomato","mango"]
fruit[1] = "kiwi" #change value at position 1
print(fruit)

vfruit = fruit.pop() #removes last element
print(vfruit)

sfruit = fruit.pop(0) #removes first element
print(sfruit)

fruit.remove("banana") #removes specific thing
print(fruit)

pfruit = fruit.index("tomato")
print(pfruit)

#fruit.append("kiwi") adds it to the end



#numbers
num=[1,2,3,4,5]
numm=[12,13,14,15]
print (num+numm)





def f_relief():
    global relief
    elief = input(print("Do you wanna take some pills/go to the doctor? Please say either 'pills', 'doctor', or 'no"))
    relief = str.lower(elief)
