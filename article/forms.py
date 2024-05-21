from django import forms

from .models import Article

# bu sefer diğer
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content','article_image'] # yani burada gösterilecek alanların listesi



# yaptığımız işlemler 
"""
bu sefer diğer(user > forms.py) dosyasındaki gibi değil daha işlevsel şekilde form oluşturacağız
önceden forms.Form dan miras alıp sınıfı oluşturuyorduk

1- model form django diye aratıp ilk sayfaya giriyoruz dokümentasyon ->(https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/)
dokümentasyondan bakarak ilerliyoruz

2- Article'ı import ediyoruz (models.py dosyasındaki Article sınıfını) -> from .models import Article
3- Class metayı sınıfın içine ekliyoruz bu sayede article ve form ilişkilendiriliyor(bunu bir kez daha yapmıştık hatırlarsan)
    class Meta:
...         model = Article
-şimdi bizim models.py dosyasındaki Article sınıfımızın içinde author,title,content ve created_date  alanları var 
-biz created_date alanını zaten auto_now_add=True olarak belirttik , bu yüzden djangodan bu alana input oluşturmasını istemiyoruz yani bunu katmayacağız

-aynı şekilde author alanından da input oluşturulmasını istemiyoruz çünkü bu panele gelebilmek için zaten giriş yapmak gerekiyor ve giriş yaptığı için
biz kullanıcıyı biliyoruz o yüzden kullanıcıdan yazar inputu verisi almamıza gerek yok 

- KISACA: yani bizim djangodan istediğimiz şey title ve content alanı için 2 tane form objesi oluşturmak . Bunu nasıl yaparız ?
  > fields = ['title','content']  yaparak bunu djangoya söylüyoruz

2.yol ile birlikte ModelForm kullanarak yaptığımız işlem şu : Bir formu kullanarak daha rahat bir şekilde yeni bir form oluşturmak
"""