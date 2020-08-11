import requests,json
def speak(str):
    from win32com.client import Dispatch
    a=Dispatch('SAPI.SpVoice')
    a.Speak(str)

a=requests.get('http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=403ce875297240bbb290147312d0d96c')
te=json.loads(a.text)
print(json.dumps(te,indent=2))
for i in te['articles']:
    speak(i['title'])



# show=json.dumps(a,indent=2)
# print(show)