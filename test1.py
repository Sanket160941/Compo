name = "Ankur"
batch = "2"
roll_no = 17

# Using concatenation
print("name of the student is " + name + " who is in batch " + batch + " with roll number " + str(roll_no))

# Using f-strings
print(f"name of the student is {name} who is in batch {batch} with roll number {roll_no}")

# Using .format()
print("name of the student is {} who is in batch {} with roll number {}".format(name, batch, roll_no))

# Placeholder for different cases
# Different Cases

a,b = 10,20
print(a)
print(b)
print(a*b)

a,b = 10,20
x, y, z, a, b = 'name',17,'batch', True, 89.97
print(x,y,z,a,b)

name = '''Hello world
sanket
mithbavkar
55
TE IT'''

print(name)