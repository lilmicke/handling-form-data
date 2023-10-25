from django.shortcuts import render

def home(request):
    return render(request,'index.html')
def register(request):
    name = request.POST.get("a")
    email = request.POST.get("b")
    password = request.POST.get("c")
    context = {
        "jina": name,
        "arafa": email,
        "siri": password
    }

    return render(request, 'register.html', context)