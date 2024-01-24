from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def djforms(request):
    ENFO=nameform()
    d={'ENFO':ENFO}
    if request.method=='POST':
        NFDO=nameform(request.POST)
        if NFDO.is_valid():
            return HttpResponse(str(NFDO.cleaned_data))
        else:
            return HttpResponse('data is unvalid')
    return render(request,'djforms.html',d)

