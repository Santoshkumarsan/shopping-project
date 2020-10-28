from django.shortcuts import render
from .models import stamp,Contactform
from django.contrib.auth.decorators import login_required 

# Create your views here.
def main_view(request):
    
    return render(request, 'printapp/index.html')

def main_view2(request):
    
    return render(request, 'printapp/index-2.html')
@login_required
def stamps_view(request):
    product=stamp.objects.all()
   

    return render(request, 'printapp/stamps.html',{'product':product})

def contact_us_view(request):
    if request.method=='POST':
        fullname=request.POST.get('fullname','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        message=request.POST.get('message','')
        contact=Contactform(fullname=fullname,email=email,phone=phone,message=message)
        contact.save()

    return render(request, 'printapp/contact.html')

def about_us_view(request):
   

    return render(request, 'printapp/about.html')


def logout_view(request):

     return render(request,'printapp/logout.html') 