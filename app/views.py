from django.db.models import Count
from django.shortcuts import render
from django.views import View
from .models import Products 
# Create your views here.

def index(request):
    return render(request, 'index.html')

class CategoryView(View):
    def get(self, request, val):
        product = Products.objects.filter(category=val)
        title = Products.objects.filter(category=val).values('title')
        return render(request, 'category.html', locals())
    
class CategoryTitle(View):
    def get(self, request,val):
        product = Products.objects.filter(title=val)
        title = Products.objects.filter(category=product[0].category).values('titles')
        return render(request, 'category.html', locals())
    
    
class PrdouctDetail(View):
    def get(self, request, pk ):
        product = Products.objects.filter(pk=pk)
        return render(request, 'productdetail.html', locals())