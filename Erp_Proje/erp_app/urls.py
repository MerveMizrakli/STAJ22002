from django.urls import path
from .views import RafListView, UrunListView, RafUrunListView, AlisCreateView, SatisCreateView



#hangi urlye hangi view yanıt verecek onu tanımlıyoruz.

urlpatterns = [
    path('raflar/', RafListView.as_view(), name='raf-list'),
    path('urunler/', UrunListView.as_view(), name='urun-list'),  
    path('raf-urun/', RafUrunListView.as_view(), name='raf-urun-list'),
    path('alis/', AlisCreateView.as_view(), name='alis-create'),
    path('satis/', SatisCreateView.as_view(), name='satis-create'),
]


    #URL’e isim vererek reverse lookup yapılmasını sağlar (örneğin template veya başka yerde URL çağırmak için).
    #bu isimler raf list urun list gibi yukardakilerde.