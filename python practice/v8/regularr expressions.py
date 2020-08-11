import re
a='''Saad 22 Sumaiya 17
Asd 456 Kgf 8901'''
print(a)
k=re.findall('\d{1,2}',a)
print(k)
k=re.findall(r'[245]{2}',a)
print(k)
a='''Saad 22 Sumaiya 17
Asd 45 Kgf 89
aad'''
d={}
k=re.findall('\d{1,2}',a)
print(k)
s=re.findall(r'[A-Z][a-z]*',a)
print(s)
c=0
for i in s:
    d[i]=k[c]
    c+=1
print(d)
s=re.search('aad',a)
print(s)
s=re.finditer('aad',a)
for i in s:
    print(i.span())
a='Sat  a s a  mat cat lat'
s=re.findall(r'[A-Z,a-z]at',a)
print(s)
s=re.findall(r'[^A-Z,a-z]at',a)
print(s)
s=re.compile(r'Sat')
s=s.sub('Food',a)
print(s)

a='1 12 123 1234 12345 123456 1234567'
s=re.findall('\d{5,7}',a)
print(s)
# /w=[A-Za-z0-9]
# \W=[^A-Za-z0-9]
a='123-321-456a'
if re.search(r'\w{3}-\w{3}-\w{4}',a):
    print('OK')
if re.search(r'\d{3}-\d{3}-\d{4}', a):
    print('OK')
else:
    print('Not OK')