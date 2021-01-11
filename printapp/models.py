from django.db import models
from django.urls import reverse
from datetime import datetime
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()
    productimage= models.ImageField(upload_to ='categoryproduct/',default="") 
    pricerange=models.CharField(max_length=25,default="Rs:")
    parent = models.ForeignKey('self',blank=True, null=True, on_delete=models.CASCADE,)
    class Meta:
        #enforcing that there can not be two categories under a parent with same slug
        
        # __str__ method elaborated later in post.  use __unicode__ in place of
        
        # __str__ if you are using python 2

        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     

    def __str__(self):                           
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])
    def get_absolute_url(self):
        return reverse('product_detail',args=[self.slug])


#class Main_model(models.Model):


class stamp(models.Model):
    name=models.CharField(max_length=25,default="")
    slug=models.SlugField(default="")
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE,)
    productimage= models.ImageField(upload_to ='productimage/',default="")    
    price=models.CharField(max_length=25,default="Rs:")
    publish=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=('-publish',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.strftime('%y'),self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])
            #insted of public.year i use here strftime(%y0) 
class Contactform(models.Model):
    fullname=models.CharField(max_length=64,default="")
    email=models.EmailField()
    phone=models.CharField(max_length=64)
    message=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=('-time',)
    


class emailsubscribbed(models.Model):   
    email=models.EmailField()
    time=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=('-time',)
    