import requests,pickle
a=requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data').text
a=[i.split(',') for i in a.split('\n')]


f=open('picklee.pkl','wb')
pickle.dump(a,f)
f.close()

f=open('picklee.pkl','rb')
read=pickle.load(f)
print(read)
f.close()