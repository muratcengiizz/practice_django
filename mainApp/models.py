from django.db import models

# Create your models here.


class yazilar(models.Model):
    on_baslik = models.CharField(max_length=100)
    alt_baslik = models.CharField(max_length=300)
    main_image = models.ImageField(null=True, blank=True, upload_to="images/")
    tarih = models.CharField(max_length=50)
    
    image1 = models.ImageField(null=True, blank=True, upload_to="images/")
    yazi1 = models.TextField(max_length=5000)
    
    image2 = models.ImageField(null=True, blank=True, upload_to="images/")
    yazi2 = models.TextField(max_length=5000)
    
    image3 = models.ImageField(null=True, blank=True, upload_to="images/")
    
    yaziBenzersizId = models.CharField(max_length=10)
    yazi_path = models.CharField(max_length=100, default="")
    
    
class iletisim(models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=300)
    message = models.TextField(max_length=5000)