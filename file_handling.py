f = open('file.txt','r')
print(f.readlines())
f.close()


f = open('file.txt','r')

for i in f.readlines():
    s = i.strip('\n')
    print(s)

f.close()


with open('file.txt','r') as f:
    print(f.readlines())