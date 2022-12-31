from django.shortcuts import render

# Create your views here.
def functiona(request):
    n={'a':100,'b':200}
    return render(request, 'functiona.html',context=n)
