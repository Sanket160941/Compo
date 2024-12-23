t = tuple()
print(t)
print(type(t))

t = tuple()
t = ("apple","banana","brocolli","carrots","raddish","potato","mango","jackfruit","chickoo")
print(len(t))

print(t)

print(t[2])

print(t[3:6])

l = list(t)
print(type(l))

l[2] = "blueberry"

t = tuple(l)
print(type(t))

for i in t:
    print(i)


t = ("apple","banana","brocolli","carrots","raddish","potato","mango","jackfruit","chickoo")
a, b, c, d, e, f, g = t[0],t[1],t[2],t[3],t[4],t[5],t[6]
print(a,b,c,d,e,f,g)

t = ("apple","banana","brocolli","carrots")
a, b, c, d = t
print(a,b,c,d)

a, b, *c= t
print(a,b,c)