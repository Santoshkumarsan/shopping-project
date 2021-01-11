from django.contrib import admin
from .models import Category, stamp,Contactform,emailsubscribbed
#from .forms import ContactForm
# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Category,categoryAdmin)
class stampAdmin(admin.ModelAdmin):
    
    list_display=['name','publish']   
    search_fields=('name',)    
    

admin.site.register(stamp,stampAdmin)
class emailsubscribbedAdmin(admin.ModelAdmin):
    
    list_display=['email','time']   
    search_fields=('email',)    
    

admin.site.register(emailsubscribbed,emailsubscribbedAdmin)
class ContactformAdmin(admin.ModelAdmin):
    
    list_display=['fullname','email','phone','message']
    list_filter=['fullname','email']
    search_fields=('fullname',)    
    

admin.site.register(Contactform,ContactformAdmin)


