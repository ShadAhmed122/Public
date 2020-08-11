import time
print(time.process_time())
def fun1(s,*d,**f):
    print(s)
    print(d)
    for i,j in f.items():
        print(i,j)

a=1
b=[1,2]
c=[1,2,3]
h={'1':'assa','2':'21'}
fun1(a,*c,**h)


print(time.ctime())
# print(time.localtime()-time.sleep(70))
print(time.asctime())
print(time.perf_counter())
print(time.process_time())
print(time.thread_time())