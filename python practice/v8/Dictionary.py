a={"Saad":19,"Anik":33,"Kam":"O0","Shad":(1,2,3,4,5,6)}
print(type(a))
a["Ahmed"]="Ullah"
print(a)
del a["Kam"]
print(a)
a["hmed"]="Habib"
a.update({"sad":"A+"})
print(a)
print(a.items())
print(a.values())
print(a["Shad"][2])
b=a.copy()
# be aware of pointer
print(b["Shad"])
print(b.get("Shad"),end=" ")
print(a.keys())
