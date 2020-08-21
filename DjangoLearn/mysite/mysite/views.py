from django.http import HttpResponse

def index(request):
    return HttpResponse("Assalamualikum")
def about(request):
    return HttpResponse("Assalamualikum about")
def yt(request):
    return HttpResponse(r"Assalamualikum about<br><a href='https://www.youtube.com/'>Go to Youtube<a>")