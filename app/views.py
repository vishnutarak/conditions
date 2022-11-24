from django.shortcuts import render

# Create your views here.
def condition(request):
    d=context={'a':200,'b':400,'c':300}
    return render(request,'conditions.html',d)
