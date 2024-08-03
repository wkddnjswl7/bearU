from django.shortcuts import render # type: ignore

def signin(request):
    if request.method=="GET":
        return render(request,'page/signin.html')
