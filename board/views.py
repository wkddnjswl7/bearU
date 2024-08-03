from django.shortcuts import render

# Create your views here.
def board(request):
    if request.method == "GET":
        context={
            "title" :"안녕 베어유?"
        }
        return render(request, 'page/index.html',context=context)        #request 객체를 포함해서 index.html로 렌더링(context값도 함께 전달)