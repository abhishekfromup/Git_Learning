a = 2
print("a",id(a))
a = a+1
print("a+1",id(a))
b = 3
print("b",id(b))
c = a+b
print("c",id(c))
c = a+b+c+b
print("sda",id(c))
print("a",id(a+b))
