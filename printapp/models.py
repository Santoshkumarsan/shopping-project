from django.db import models

# Create your models here.
class stamp(models.Model):
    name=models.CharField(max_length=25,default="")
    productimage= models.ImageField(upload_to ='productimage/',default="")    
    price=models.CharField(max_length=25,default="Rs:")
    publish=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=('-publish',)
    def __str__(self):
        return self.name

class Contactform(models.Model):
    fullname=models.CharField(max_length=64,default="dgdd")
    email=models.EmailField()
    phone=models.CharField(max_length=64)
    message=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=('-time',)
    


    