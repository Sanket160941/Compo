d = dict()
print(d)
print(type(d))

d = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6}
print(d)

print(d.get("c"))
print(d.get("e"))
print(d.get('g',False))

d["g"] = 7

d.update({"h":8})
print(d)
print(d.keys())
print(d.values())

d.pop("d")
print(d)

d.clear()
print(d)

del d
print(d)