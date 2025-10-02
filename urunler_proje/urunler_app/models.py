from django.db import models

# Create your models here.

class UrunOzellik(models.Model):
    adi=models.CharField(max_length=100)   #bu kısım girilen özelliklerin değerini tutar
    barkod=models.CharField(max_length=50)
    kod=models.CharField(max_length=50)
    fiyat=models.DecimalField(max_digits=10 ,decimal_places=2) 
    fiyat_kuru=models.CharField(max_length=10)    #tl,euro vs

    def __str__(self):   #admin panelinde ürün adı gösterilsin diye var.
        return self.adi
    
    #veritabanı verileri

    #veritabanına kaydetmek ve test etmek için:
    #python manage.py makemigrations
    #python manage.py migrate
    