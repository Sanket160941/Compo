a = 10
for i in range(a):
    print(i)

a = 10
for i in range(3,a+1):
    print(i)

a = 10
for i in range(1,a+5,2):
    print(i)


s = "hello world"
for i in s:
    print(i)

s = "hello world"
for i in s:
    print(i,end=',')

s = "hello world"
for i in s:
    print(i,end='/')

s = "hello world"
for i in s:
    print(i,end='/t')


v = "hello world"
for i in range(len(v)):
    print(i)

v = "hello world"
for i in range(2,len(v)+5):
    print(i)

v = "hello world"
l = [2,35,6,21,67,9,0,55]
for i in l:
    print(i)


v = "the greatest time"
for i in v:
    print(i)
else:
    print("done")


# for i in range(10):
#     for j in range(10):
#         print(i*j)


for i in range(10):
    for j in range(10):
        pass

i = 0
while i-10:
    print(i)
    i+=1
else:
    print("completed")

for i in range(10):
    if i == 5:
        continue
    print(i)

for i in range(10):
    if i == 5:
        break
    print(i)