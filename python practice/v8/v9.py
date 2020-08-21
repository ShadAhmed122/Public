#complete this code
class inventory:
  def __init__(self):
    self.sl_no = list()
    self.item_name = list()
    self.purchase_amount = list()
    self.purchase_cost = list() 
    self.list_of_tuples= None

  def create_list_of_tuples(self,a,b,c,d):
    k=self.sl_no
    k.append(a)
    self.sl_no=k
    k=self.item_name
    k.append(b)
    self.item_name=k
    k=self.purchase_amount
    k.append(c)
    self.purchase_amount=k
    k=self.purchase_cost
    k.append(d)
    self.purchase_cost=k
    if self.list_of_tuples==None:
      self.list_of_tuples=[]
    k=self.list_of_tuples
    k.append((a,b,c,d))
    self.list_of_tuples=k


  def sort_by_cost(self):
    k=self.list_of_tuples
    k.sort(key=lambda tup: tup[3])
    k=k[::-1]
    self.list_of_tuples=k
    return self.list_of_tuples
  
  def total_cost(self):
    print('Total Cost is',sum([i[3] for i in self.list_of_tuples]))


mic=inventory()

while True:
  var= input('Enter an entry: ')
  if var==str(0):
    break
  try:
    var=var.split(' ')
    mic.create_list_of_tuples(int(var[0]),var[1],int(var[2]),int(var[3]))
  except Exception as e:
    print(e)
  try:
    mic.sort_by_cost()
  except Exception as e:
    print(e)
  # print(mic.__dict__)

  
mic.total_cost()
n= int(input('Enter index: '))
print(mic.sort_by_cost()[n])