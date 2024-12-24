def print_helloworld():
    print("Hello World")
print_helloworld()


def print_name():
    return f"Hello Sanket"
name = input("Please enter your name -> ")
print(print_name())


def print_name(n):
    return f"Hello {n}"
name = input("Please enter your name -> ")
print(print_name(name))


def print_name(n,r):
    return f"Hello {n}, roll number {r}"

name = input("Please enter your name -> ")
roll_no = input("Please enter your roll number -> ")
print(print_name(name,roll_no))


def print_name(l):
    l1 = []
    for i in range(l):
        l1.append(i)
    return l1
print(print_name(11))


def print_name(l):
    l1 = []
    for i in l:
        l1.append(i)
    return l1
print(print_name([1,4,5,7]))


def fun1():
    pass

def fun2():
    pass

def print_name(l):
    pass

def print_name(l=10):
    return l
print(print_name())

def fun3():
    return True
print(fun3())

def fun4(a,b,c):
    return a+b+c
print(fun4(1,2,3))

# args
def fun5(*args):
    s = 0
    for i in args:
        s+=1
        return s
    print(fun5(1,2,3,4,5,6))

# kwargs
def fun6(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
fun6(a=1,b=2,c=3)