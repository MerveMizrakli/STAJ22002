from django.shortcuts import render

# Create your views here.

from rest_framework import generics   #generics otomatik olarak api işlemleri metodlarını içinde bulundurur.crud işlemleri
from .models import UrunOzellik
from .serializers import UrunOzellikSerializer

class UrunListCreateView(generics.ListCreateAPIView):
    serializer_class = UrunOzellikSerializer    #apinin hangi serializer class ile çalşacağını belirler.
 
    def get_queryset(self):    #list işlemleri sırasında hangi verilerin döneceğini belirler.
        queryset = UrunOzellik.objects.all()   #veritabanındaki tüm bilgileri getir.
        fiyat_max = self.request.query_params.get('fiyat_max')   #urldeki sorgu parametrelerini alır.
        barkod = self.request.query_params.get('barkod')
        fiyat_min =self.request.query_params.get('fiyat_min')
        fiyat_cikar=self.request.query_params.get('fiyat_cikar')

        if fiyat_max is not None:
            queryset = queryset.filter(fiyat__lte=fiyat_max) 
        if fiyat_min is not None:
            queryset = queryset.filter(fiyat__gte=fiyat_min)
        if fiyat_cikar is not None:
            queryset=queryset.filter().exclude(fiyat=fiyat_cikar)
               #istenilen değer değişken çıkarma.

             #fiyat büyük veya eşit olan kısımları sonuç döndürür. bu lte kısmı ile yapılır.
        if barkod is not None:
            queryset = queryset.filter(barkod=barkod)

        return queryset    #queryset veritabanındaki verileri sorgulayabildiğimiz veri sorguları bütünüdür.
    


    
#from urunler_app.models import UrunOzellik   python manage.py shell komutunu terminalde çalıştırıp test için ekleyeceğin kod.

#UrunOzellik.objects.create(adi="Kalem", barkod="123", kod="KLM001", fiyat=20, fiyat_kuru="TL")
#UrunOzellik.objects.create(adi="Defter", barkod="456", kod="DFT002", fiyat=55, fiyat_kuru="TL")
#UrunOzellik.objects.create(adi="Silgi", barkod="789", kod="SLG003", fiyat=10, fiyat_kuru="TL")  exit()


#from urunler.models import UrunOzellik → urunler adlı uygulamanın models.py dosyasındaki UrunOzellik sınıfını (tabloyu) import ediyor.

#.objects.create(...) → Django’ya “Bu değerlerle yeni bir satır ekle” diyor.