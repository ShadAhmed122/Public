import os,speechRecognition
print(os.getcwd())
def osfun(pat):
    os.chdir(pat)
    a=os.listdir()

    b =1
    for i in a:
        c=i.split('.')

        if c[1] == 'jpg':

            os.rename(i,f'{b}.jpg')
            b=b+1
        elif c[1] == 'txt':
            os.rename(i,f'{c[0].capitalize()}.txt')
    return 1



a=os.getcwd()
b=osfun(a)
# b='sadfoood'
#
#
# os.rename('sadfod.txt',f'{b}.txt')