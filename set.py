s = set()
print(s)
print(type(s))


s.add(1)
s.add("apple")
s.add(10.0)
s.add(True)
s.add("apple")
s.add("banana")
s.add(False)
s.add(0)

print(s)

if 0:
    print("in if")
else:
    print("in else")

if True:
    print("in if")
else:
    print("in else")

if [0]:
    print("in if")
else:
    print("in else")

if ():
    print("in if")
else:
    print("in else")

s.update(["blueberry","strawberry","orange"])
print(s)

s.remove("apple")
print(s)

s.discard(4)
print(s)

s.add(100)
print(s)


s1 = set()
s1.update(["apple","banana","carrots","raddish","potato","mango","jackfruit","chickoo"])
print("s1 ->",s1)

print("union ->",s.union(s1))
print("difference ->",s.difference(s1))
print("intersection ->",s.intersection(s1))