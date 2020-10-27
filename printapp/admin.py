from django.contrib import admin
from .models import stamp,Contactform

# Register your models here.
class stampAdmin(admin.ModelAdmin):
    
    list_display=['name',]   
    search_fields=('name',)    
    

admin.site.register(stamp,stampAdmin)

class ContactformAdmin(admin.ModelAdmin):
    
    list_display=('fullname','email','phone',)
    list_filter=['fullname','email']
    search_fields=('fullname',)    
    

admin.site.register(Contactform,ContactformAdmin)


