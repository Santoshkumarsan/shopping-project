from django.shortcuts import render,HttpResponseRedirect,get_object_or_404,get_list_or_404
from .models import stamp,Contactform,emailsubscribbed,Category
from django.contrib.auth.decorators import login_required 
from .forms import SignUpForm
from django.utils import timezone 
from django.conf import settings
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


# Create your views here.
# def stamp_detail_view(request,year,month,day,post):
#     post=get_list_or_404(stamp,slug=post,publish__year=year,publish__month=month,publish__day=day)
#     return render(request,'printapp/stamps.html',{'post':post})
    # print(post)





class stamp_detail_view(DetailView):
    model = stamp
    template_name='printapp/stamp_details.html'
    context_object_name = 'con'

class list_view(ListView):
    model = stamp
    template_name='printapp/indexlist.html'
    context_object_name = 'my_fav'


def main_view(request):
    product=Category.objects.all()
    if request.method=='POST':
        email=request.POST.get('email','')
        contact=emailsubscribbed(email=email)
        contact.save()
        return HttpResponseRedirect('/')


    return render(request, 'printapp/index.html',{'product':product})

def main_view2(request):
    product=Category.objects.all()
    
    return render(request, 'printapp/index-2.html',{'product':product})

def stamps_view(request,id):
    #post=get_object_or_404(stamp,slug=post)
    product=stamp.objects.get(Pk=id)
   
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

