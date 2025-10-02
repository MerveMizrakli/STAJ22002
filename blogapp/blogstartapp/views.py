from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):    #metod tanımlaması yapık.Bu url çağrıldığında buradaki response döner.
    return render(request,'blogarayuz/index.html') #html sayfası gönderecek

def blogs(request):
    return render(request,'blogarayuz/blogs.html') #blog arayüz dosyası aldındaki blog html dosyası çağrılır

def blogs_details(request,id):  #id de ekstra bir request olarak geleceği için parametre ile tanımlanmalıdır.
    return render(request,'blogarayuz/blog-details.html',{
        'id':id   #burada bir sözlük tanımlaması yaptık.Gönderilen id bilgisi buradaki sözlükle eşlenecek.Bunu html dosyasında da yapacağız
    })

#yani temel olarak şudur ki: sayfa çağrıldığında örnek index sayfası buradaki metodlar ile bu sayfa çağrıldığında ekranda gösterilecekler yazılır.
#request bir parametre olarak gelir.Bu istek anlamındadır.Http response ile bu isteğe gösterilen yanıt verilir.Response ile bir yazı göndermiş oluyoruz.
#def blogs(request):
 #   return HttpResponse('blogs')   bu şekilde olsaydı response döner.