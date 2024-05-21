from django.contrib import admin

from .models import Article,Comment


# Register your models here.


admin.site.register(Comment)

#admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','author','created_date']
    list_display_links = ['title', 'author']

    search_fields = ['title']
    

    """
    !!! DEĞERLER TUPLE(DEMET) OLARAK VERİLİR ve sen değerden sonra virgül atmazsan o tuple değil int olur :) --> (5) ve (5,) = int ve tuple

    ÖRNEK OLARAK EKLENEBİLECEK DEĞERLER:
        ordering = ('created_date',) # Sonuçların sıralanma şekli.
        date_hierarchy = 'created_date' # Tarih tabanlı navigasyon
        raw_id_fields = ('author',) # Yazar alanını ID ile seçmek için.
    
    """

    list_filter = ['created_date']
    class Meta:
        model = Article






#YUKARIDA CLASS ARTICLE ICIN NELER YAPTIK?
"""
1- admin.site.register(Article) kaldırdık bunu farklı yolla yapacağımız için(ben yorum satırı bıraktım unutmamak için)
2- admin.register'i decorator olarak oluşturuyoruz
3- ArticleAdmin class'ı oluşturup bunu import ettiğimiz admin'den ModelAdmin sınıfından miras alıyoruz
4- Django'nun da önerdiği gibi sınıf içinde sınıf oluşturup(class meta'yı anlamana gerek yok ezberle yeterli)
    model = Article yaparak bu ArticleAdmin class'ı ile @admin.register içindeki Article'yi bağlıyoruz yani ilişkilendiriyoruz
    unutma class Meta django tarafından desteklenen bir sınıf o yüzden ismini veya sistemini değiştiremezsin sadece ilişkilendiğin değişken değişir.
5- Oluşturduğumuz tabloyu(sınıfı) bu şekilde ekledikten sonra özelleştirme işlemlerine devam edebiliriz -> anlatim.py devam
6- list_display özelliği ekleyerek article'leri görüntülerken hangi tablo objelerinin görüntüleneceğini seçiyoruz(fonksiyon bu işe yarıyor)
7- list_display_links ile hangi tablo objelerinin üstüne basıldığında düzenlemeye gidileceğini belirtiyoruz
8- search_fields ile siteye arama kutusu ekledik ve başlık üzerinden aranılacağını belirttik(iki şey birden olmaz istersen silip author yazabilirsin)

"""

