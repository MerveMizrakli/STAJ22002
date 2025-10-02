from rest_framework import generics
from .models import Raf, Urun, RafUrun, Alis, Satis
from .serializers import RafSerializer, UrunSerializer, RafUrunSerializer, AlisSerializer, SatisSerializer

# Listeleme
class RafListView(generics.ListAPIView):   #list api view sadece verileri listeler .Yani GET İSTEĞİ.
    queryset = Raf.objects.all()           #tüm raf verileri alınır
    serializer_class = RafSerializer       #raf verileri jsona çevrilir.

class UrunListView(generics.ListAPIView):
    queryset = Urun.objects.all()
    serializer_class = UrunSerializer

class RafUrunListView(generics.ListAPIView):
    queryset = RafUrun.objects.all()
    serializer_class = RafUrunSerializer

# API üzerinden alış ve satış
class AlisCreateView(generics.CreateAPIView):       #create view  ile yeni kayıt oluşturulur.YANİ POST
    queryset = Alis.objects.all()                   #tüm kayıtları (o anki isteğe bağlı) listeler
    serializer_class = AlisSerializer    

     #API üzerinden bir alış işlemi yapılırsa:
     #Alis.save() metodu çalışır.
     # RafUrun’daki ürün adedi otomatik artar (models.py’deki logic sayesinde).



class SatisCreateView(generics.CreateAPIView):    #post isteği ile satış kaydı ekleniyor
    queryset = Satis.objects.all()
    serializer_class = SatisSerializer      #aynı şekilde satış save metodu çalışır.
