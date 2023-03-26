from django.http import HttpResponse
from django.shortcuts import render

from . models import Name


def demo(request):
    obj=Name.objects.all()
    return render(request, "index.html",{'result':obj})
# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return render(request,"contact.html")
# def detail(request):
#     return HttpResponse("Details are written here")
# def thanks(request):
#     return HttpResponse("Thank you..")