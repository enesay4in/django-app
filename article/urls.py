from django.contrib import admin
from django.urls import path

from . import views # from olarak belirtmemiz lazım django da (olduğumuz klasörü belirtirken . koyuyoruz)

# uygulama ismi belirtme sebebimiz : redirect işlemi yaptığımızda şu uygulamanın içindeki şu url ismine göre redirect yap diyoruz o yüzden app name veriyoruz

app_name = "article"

urlpatterns = [
    path('create/',views.index,name= 'index'),
    path('dashboard/',views.dashboard,name= 'dashboard'),
    path('addarticle/',views.addarticle,name= 'addarticle'),
    path('article/<int:id>/',views.detail,name= 'detail'),
    path('update/<int:id>/',views.updatearticle,name= 'update'),
    path('delete/<int:id>/',views.deletearticle,name= 'delete'),
    path('',views.articles,name= 'articles'),
    path('comment/<int:id>/',views.addcomment,name= 'comment'),
]


# 2 adet urls.py dosyasını include ile birleştirmek
"""
1- article klasörü içinde yeni bir urls.py dosyası açıyoruz
2- diğer urls.py dosyasındaki importları tekrar dahil ediyoruz
3- views dosyamızı import etmemiz gerekiyor from . import views yapıyoruz ( üstte belirttiğim . sebebi klasör belirtmek)
4- blog_django içindeki urls.py dosyasından buna erişmek için uygulama ismi oluşturmak zorundayız , app_name = "article" yapıyoruz
5- blog_django içindeki urls.py dosyasında ki gibi urlpatterns listesi açıp path belirtiyoruz 
   burada ki path belirtme işlemi önceki gibi ama include ettiğimiz yerde birleştirmeyi yapacağız o yüzden burasını yapmayı zaten biliyorsun
6- blog_django içindeki urls.py dosyasına gidip path olarak iki urls.py dosyasını birleştiriyoruz
   path('articles/',include("article.urls")), --> burada yaptığımız işlem articles/ olarak geldiğinde onu al ve include ettiğim url dosyasınla birleştir demektir
   yani -> 'articles/' + 'create/' yapıyoruz ve böylelikle articles/create sayfası çağrıldığında views.index fonksiyonumuz çalışacak
   2 urls.py dosyasını birleştirip ayrı ayrı linkleri anadizin bir olursa onun üzerinden çağrılma işlemi yapıldığında istediğimiz fonksiyonu çalıştırmayı gördük
# bunun böyle yapılma sebebi nedir? , bunları tek bir sayfada da yapabilirdik gibi soruların cevabı :
  çünkü proje dosyası büyüdükçe karmaşıklaşacaktır , her bir işlemi böyle es geç bir arada yap yaparsak ilerde düğüm olacaktır . 
  bizim böyle yapma yani parçalama sebebimiz projeyi daha modüler ve kullanışlı tutma çabası ki django'nun en temel olayı da budur
  hepsini bir klasör içinde de hatta bir dosya içinde bile yapmayı deneyebilirsin çalışacaktır ama olay daha modüler, daha anlaşılır ve daha temiz kod yazmak


"""