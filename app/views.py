from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'name':'RAMANA','age':23}
    return render(request,'data_render.html',context=d)
def if_else(request):
    d={'a':19,'b':35}
    return render(request,'if_else.html',context=d)
def if_elif(request):
    d={'a':19,'b':35,'c':42}
    return render(request,'if_elif.html',context=d)
def nested_if(request):
    d={'a':19,'b':35,'c':42}
    return render(request,'nested_if.html',context=d)
