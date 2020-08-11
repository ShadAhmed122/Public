import re
a='''Combine your names.
First name + last name = cliffordchi@domain.com
First name . last name = clifford.chi@domain.com
First name - last name = clifford-chi@domain.com
First name . middle name . last name = clifford.douglas.chi@domain.com
First name - middle name - last name = clifford-douglas-chi@domain.com
First initial + last name = cchi@domain.com
First initial + middle name + last name = cdouglaschi@domain.com
First initial + middle initial +last name = cdchi@domain.com
Shorten your names.
cliffchi@domain.com
cliffdougchi@domain.com
cliffdouglaschi@domain.com
clifforddougchi@domain.com
Combine your name with your profession, city, or degree.
cliffordchiwriter@domain.com
cliffchiwriter@domain.com
cchiwriter@domain.com
cliffordchiboston@domain.com
cliffchiboston@domain.com
cchiboston@domain.com
cliffordchimfa@domain.com
cliffchimfa@domain.com
cchimfa@domain.com
Surprisingly, choosing a professional email address can be quite challenging, especially since you can’t spice it up like you can with your personal one. But, as you can see, there are still plenty of ways for choosing a strong professional email address, and, hopefully, we helped you find one.

'''

a=re.findall(r'[\w.+_%]{2,20}@[\w._]{2,20}.[A-Za-z]{2,3}',a)
a='\n'.join(a)
print(type(a))
print(a)
with open('Emails.txt','w') as f:
    f.write(a)
