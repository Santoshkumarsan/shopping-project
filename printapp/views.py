from django.shortcuts import render,HttpResponseRedirect
from .models import stamp,Contactform
from django.contrib.auth.decorators import login_required 
from .forms import SignUpForm
# Create your views here.
def main_view(request):
    
    return render(request, 'printapp/index.html')

def main_view2(request):
    
    return render(request, 'printapp/index-2.html')

def stamps_view(request):
    product=stamp.objects.all()
   

    return render(request, 'printapp/stamps.html',{'product':product})
def stamps_view_2(request):
    product=stamp.objects.all()
   

    return render(request, 'printapp/stamps2.html',{'product':product})
def contact_us_view(request):
    if request.method=='POST':
        fullname=request.POST.get('fullname','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        message=request.POST.get('message','')
        contact=Contactform(fullname=fullname,email=email,phone=phone,message=message)
        contact.save()
        return HttpResponseRedirect('/contact')

    return render(request, 'printapp/contact.html')
def contact_us_2_view(request):
    if request.method=='POST':
        fullname=request.POST.get('fullname','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        message=request.POST.get('message','')
        contact=Contactform(fullname=fullname,email=email,phone=phone,message=message)
        contact.save()
        return HttpResponseRedirect('/contactus')

    return render(request, 'printapp/contactus.html')
def about_us_view(request):
   

    return render(request, 'printapp/about.html')


def logout_view(request):

     return render(request,'printapp/logout.html') 


def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'printapp/signup.html',{'form':form}) 

