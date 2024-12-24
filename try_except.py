print("start")

try:
    print(0/0)
except:
    print("Error occured")

print("end")


print("start")

try:
    print(0/0)
except:
    print("Cannot divide by 0")
finally:
    print("In finally")

print("end")


print("start")

try:
    print(1/1)
except:
    print("Cannot divide by 0")
finally:
    print("In finally")

print("end")

import traceback

try:
    print(0/0)
except:
    print(traceback.format_exc())


import traceback

try:
    print(0/0)
except:
    raise Exception("Cannot divide by 0")