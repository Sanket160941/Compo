l = list()
print(l)
print(type(l))


l = ["apple","watermelon","banana","strawberry"]
print(l[2])

l = ["apple","watermelon","banana","strawberry"]
print(l[0:2])

l = ["apple","watermelon","banana","strawberry"]
l[0] = "melon"
print(l)

l = ["apple","watermelon","banana","strawberry"]
print(l)

l = ["apple","watermelon","banana","strawberry"]
l.append("orange")
l.append("lemon")
l.append("chickoo")
print(l)

l = ["apple","watermelon","banana","strawberry"]
l.insert(3,"potato")
print(l)

l = ["apple","watermelon","banana","strawberry"]
l.insert(0,"grapes")
print(l)

l = ["apple","watermelon","banana","strawberry"]
l1 = [1,2,3,4,5]
l.append(l1)
print(l)

l = ["apple","watermelon","banana","strawberry"]
l1 = [1,2,3,4,5,6,7,8,9]
print(l + l1)

l = ["apple","watermelon","banana","strawberry"]
l.remove("banana")
print(l)

l = ["apple","watermelon","banana","strawberry","grapes"]
print(l.pop())
print(l)

l = ["apple","watermelon","banana","strawberry","grapes"]
l.pop(2)
print(l)

l = ["apple","watermelon","banana","strawberry","grapes"]
l.clear()
print(l)

l = ["apple","watermelon","banana","strawberry"]
for i in l:
    print(i)

l1 = [i for i in range(1,21)]
print(l1)

l1 = ['s' for i in range(1,11)]
print(l1)

print([i for i in range(1,21)])

l2 = [6,2,8,1,3,10,4,7,9,5]
l2.sort()
print(l2)

print(len(l2))


l4 = ["apple","watermelon","banana","strawberry"]
del l4
print(l4)