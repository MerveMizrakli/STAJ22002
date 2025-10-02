"""
URL configuration for blogapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include #include ile gelecek url leri dahil ediyoruz.


#http://127.0.0.1:8000/            
#http://127.0.0.1:8000/index         #aşağıda include ettiğimiz yerde path kısmına parametre verirsek örn user olsun.
#http://127.0.0.1:8000/blogs         #bu user eki hepsinin başına gelir yani örn:user/index   , user/blogs gibi
#http://127.0.0.1:8000/blogs/3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blogstartapp.urls'))  #burada blogstartappte tanımladığımız sayfa urllerini projeye dahil ediyoruz
]
