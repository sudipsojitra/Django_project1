from django.shortcuts import render, HttpResponse

def index(request):
    data = {
        "Python" : "Python code",
        "PHP" : "PHP code"
    }
    return render(request, 'index.html',data)
    
def about(request):
    return render(request, 'about.html')
    
def contactUs(request):
    return render(request, 'contact.html')
    
def services(request):
    return render(request, 'services.html')
