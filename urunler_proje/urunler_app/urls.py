from django.urls import path
from .views import UrunListCreateView

urlpatterns= [
    path('urunler/',UrunListCreateView.as_view(),name='urun-list')
]


#UrunListCreateView.as_view() ListCreatApi viewden türer.  As view kısmı sınıfı djangonun çalıştırabileceği view fonksiyonuna çevirir.
#List create view hem görüntüleme hem de listeleme özelliğine sahiptir.(Post-get)
#name kısmı da bu url ye bir isim veriyor.Dinamik işlemler için önemli.