from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,offers
# Create your views here.
def index(request):
    jagal=Product.objects.all()
    arjun=offers.objects.all()
    return render(request,'index.html',{'jagal':jagal,'arjun':arjun})
def about(request):
    return HttpResponse("<h2>This is Jagal Ser</h2>")