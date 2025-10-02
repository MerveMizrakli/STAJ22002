#url tanımlamalarının bulunacağı liste tanımlaması yapılacak
#http://127.0.0.1:8000/             : index yani anasayfaya yönlendirme yapılır.
#http://127.0.0.1:8000/index        : tekrar anasayfaya yönlendirme yapılır.
#http://127.0.0.1:8000/blogs        : blogs kısmına yönlendirme yapılır.Bu sayfaya istek gönderilmiştir.
#http://127.0.0.1:8000/blogs/3      :veritabanında 3 sayısına karşılık gelen blog bilgisini alır.Örneğin details

from django.urls import path #isteklerin alınacağı url ler path metodu ile tanımlanır.
from .import views  #gönderilecek isteklerin metodları views dosyasından alınacak.Aynı dizin içerisinde bulunduğu için . ile belirttik

urlpatterns=[
 path("",views.index),  #bunla url sonunda hiç bir şey olmayan sayfa dönecek.Yani anasayfa.
 path("index",views.index),#index olan dönecek yine anasayfa
 path("blogs",views.blogs), #blog sayfası dönecek.
 path("blogs/<int:id>",views.blogs_details) #blog detay sayfası dönecek.İd bilgisi int ile alınacğı için int id kısmı ile bu sayı alınır.
]