
from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractUser,User
# Create your models here.
class User1(AbstractUser):
    is_Doctor = models.BooleanField('Docotr status', default=False)
    is_Patient = models.BooleanField('Patient status', default=False)

class profile_details(models.Model):
    user = models.ForeignKey(User1,related_name='profile_details',on_delete=models.CASCADE)
    imgp=models.FileField(upload_to='imgs',default='default.jpg', null=True,blank=True)
    u_nm=models.CharField(max_length=150)
    fstname=models.CharField(max_length=250)
    secname=models.CharField(max_length=250)
    terimail=models.EmailField()
    timestamp = models.DateTimeField(null=True)
    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
    )
    pincode=models.IntegerField(default=None)
    city = models.CharField(
        "City",
        max_length=1024,
    )
    state = models.CharField(
        "state",
        max_length=1024,
    )
CATEGORY_TYPE=[
    ('Mental Health','Mental Health'),
    ('Physical Health','Physical Health'),
    ('Heart disease','Heart disease'),
    ('Covid','Covid')
]
class blog(models.Model):
    author=models.ForeignKey(profile_details,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    image=models.FileField(upload_to='imgs')
    category=models.CharField(choices=CATEGORY_TYPE,max_length=20)
    summary=models.CharField(max_length=100)
    content=models.CharField(max_length=200)
    as_draft=models.BooleanField(default=False)

    def __str__(self):
        return(self.title)