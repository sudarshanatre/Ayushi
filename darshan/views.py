from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # data={
    #     'title':'Home page',
    #     'webpage':'rest apis',
    #     'clist':['apple','mango','banana','sandwich'],
    #     '   ':[
    #     {'name':'sudarshan','phone':9644372441,},
    #     {'name':'testing','phone':9644372441},
    #     {'name':'developer','phone':9644372441}
    #     ]
    # }
    # return render(request,'tommorow.html',data )
    return render(request,'index.html')

def aboutus(request):
    return HttpResponse("<h1>Welcome to my Home</h1>")
def course(request):
    return HttpResponse("Welcome to my Jungle")

def simple(request):
    return HttpResponse("welcome to django service")

def simpledetails(request,simpleid):
    return HttpResponse(simpleid)

def simpleweare(request,simplevalue):
    return HttpResponse(simplevalue)