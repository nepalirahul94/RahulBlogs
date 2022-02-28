from datetime import datetime
from enum import unique
import random
from django.shortcuts import render
from blogapp.models import Blog, Contact

r = random.randint(1,Blog.objects.count()-2)

def index(request):
    data = Blog.objects.all().order_by('-pub_date')[:r]
    context = { 'blog': data}
    return render(request, 'index.html',context)

def contact(request):
    return render(request,'contact.html')
    
def display(request,slug):
    details = Blog.objects.filter(slug=slug)
    context = { 'bs' : details}

    return render(request, 'display.html', context)

def submitcontact(request):
    if request.method == 'POST':
        c_name = request.POST.get('cname')
        c_email = request.POST.get('cemail')
        c_phone = request.POST.get('cphone')
        c_message = request.POST.get('cmessage')
        contact = Contact( c_name= c_name , c_email = c_email, c_phone = c_phone,
                            c_message = c_message)
        contact.save()  
    
    return render(request, 'contact.html') 

def moreindex(request):
    data = Blog.objects.all().order_by('-pub_date')[r:]
    context = { 'blog': data}
    return render(request, 'index.html',context)





