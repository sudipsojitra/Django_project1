from django.shortcuts import render, HttpResponse

def index(request):
    data = {
        "Python" : "Python code",
        "PHP" : "PHP code"
    }
    return render(request, 'index.html',data)
    
def about(request):
    return HttpResponse("This is about page")
    
def contactUs(request):
    return HttpResponse("This is contactUs page")
    
def services(request):
    return HttpResponse("This is services page")