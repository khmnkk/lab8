from django.shortcuts import render
from .models import Client,Product,Sale
import datetime

def info(request):
 clients = Client.objects.all()
 products = Product.objects.all()
 sales = Sale.objects.all()
 return render(request, 'info.html', {
 'project_name': 'Django-project lab8',
 'student_name': 'Khomenko Tanya',
 'group': 'KiB21016b',
 'clients': clients,
 'products': products,
 'sales': sales,
 })