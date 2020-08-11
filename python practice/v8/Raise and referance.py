a=[12,34,5]
b=a
b.remove(5)
print(a)
print(b)
print(a is b)

a = input("What is your name")
if a=='10':
    raise TypeError("Numbers are not allowed")

print(f"Hello {a}")