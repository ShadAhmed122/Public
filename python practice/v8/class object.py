class Student:
    skill="Python"
    score=19
    speed=14
    def Show(self):
        print(f'{self.name} {self.roll} {self.clas} {self.skill}')
    def __init__(self,aname,aroll,aclass):
        self.name=aname
        self.roll=aroll
        self.clas=aclass

    @classmethod
    def chngdefault(cls,a,b,c):
        cls.skill=a
        cls.score=b
        cls.speed=c

    @classmethod
    def strcls(cls,a):
        a=a.split()
        return cls(a[0],a[1],a[2])

    @staticmethod
    def printa(a):
        print(f'I am {a}, the printa')


a=Student('Saad',19,14)
print(Student.__dict__)
print(a.name)
print(a.roll)
abah=Student('Saad',19,14)
abah.name="Abdul Ahad"
abah.Show()
a.Show()

strOb=Student.strcls('Kabita 10 16')
strOb.chngdefault('V Fry','100','Max')
strOb.Show()
Student.printa('Sayed')







