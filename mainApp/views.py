from django.shortcuts import render
from django.http import HttpResponse
from .models import yazilar, iletisim
# Create your views here.

def index(request):
    return render(request, "index.html")


def iletisimm(request):
    if request.method == "POST" and request.POST['name'] != "" and request.POST['mail'] != "" and request.POST['message'] != "":
        name = request.POST['name']
        mail = request.POST['mail']
        message = request.POST['message']
        
        model = iletisim(name=name, mail=mail, message=message)
        model.save()
    return render(request, "iletisim.html")

def hakkimda(request):
    return render(request, "hakkimda.html")

def yazilarr(request):
    model1 = yazilar.objects.all()
    #model11 = model1.get(yaziBenzersizId=100)
    
    
    context = {
        "yazi":model1
    }
    return render(request, "yazilar.html", context)

def yazi1(request, category):
    htmlFilePath = ""
    if category == "yazi1":
        htmlFilePath = "yazilar/yazi1.html"
        model1 = yazilar.objects.get(yaziBenzersizId=100)
    elif category == "yazi2":
        htmlFilePath = "yazilar/yazi1.html"
        model1 = yazilar.objects.get(yaziBenzersizId=101)
    elif category == "yazi3":
        htmlFilePath = "yazilar/yazi1.html"
        model1 = yazilar.objects.get(yaziBenzersizId=102)
    
    first_letter = model1.yazi1[0]
    
    
    
    context = {
        "yazi": model1, "yazi_firstletter": first_letter
    }
    
    return render(request, htmlFilePath, context)