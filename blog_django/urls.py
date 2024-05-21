"""
URL configuration for blog_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include

from article import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name= "index"), # kök dizin için '/' değil boşluk bırakıyoruz yoksa django hata verir
    path('about/', views.about , name= "about"),
    path('articles/',include("article.urls")), # "modül_ismi.dosya_ismi" include formulü böyledir
    # bu kısım 2 adet urls.py dosyası birleştirme yani include etme kısmı
    # o yüzden burayı article klasörü içinde ki urls.py dosyasında anlatıcam
    path('user/',include("user.urls")), #user/register , user/login , user/logout
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# URL'LERE İSİM VERMEK
"""
bunun sebebi flaskdaki gibi burdada redirect ile yönlendirme yaparken o fonksiyonun ismiyle ilişkili olan url'ye yönlendirecektir
ana sayfa path'i için name fonksiyonun ismini index yaptık , bu sayede redirect yaparken name'ini index diye belirttiğimizde 
ilişkili olduğu url'yi çağıracak yani kök dizine gidecektir . Bu tüm pathler için geçerlidir o yüzden hepsine ayrı isim vermek mantıklı olacaktır

"""