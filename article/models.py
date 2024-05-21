from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name="Yazar")#bu alanımız user tablosunu işaret ediyor diyoruz
    #foreign key sayesinde farklı bir tabloyu kullandığımızı gösteriyoruz 
    #(ikincil anahtar demek başka tablonun birincil anahtarı demektir)

    #on_delete = models.CASCADE nedir?
    #eğer o user'imiz silinirse buradaki o user'e ait bütün article'lar,modeller de silinsin demektir

    title = models.CharField(max_length = 50,verbose_name="Başlık")
    #content = models.TextField(verbose_name="İçerik")
    #içerik için textfield kullandık
    content = RichTextField(verbose_name="İçerik")
    created_date =  models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    #DateTimeField(auto_now_add=True) ne işe yarar?
    #auto_now_add=True sayesinde içerik eklendiği zamanı otomatik olarak alır ve created_date objesine atar

    article_image = models.FileField(blank=True,null=True,verbose_name="Medya Kısmı")
    #models.FileField: Bu, Django'da bir dosya yolu depolamak için kullanılan bir model alanı türüdür. Bu, medya dosyalarını (resimler gibi) saklamak için kullanılır.
    #blank=True: Bu parametre, bu alanın boş bırakılmasına izin verir. Yani, bu alana bir dosya eklemek zorunlu değildir.
    #null=True: Bu parametre, bu alanın veritabanında null değerini kabul edeceğini belirtir. Yani, bir dosya yüklenmediğinde, bu alana null değeri atanabilir.
    #verbose_name="Medya Kısmı": Bu, bu alanın insanlar tarafından daha iyi anlaşılabilmesi için verilen açıklayıcı bir ad. 

    def __str__(self):
        return self.title
    
    class Meta:
        #makalelerin en yeni olanları en üstte gözüksün diye sıralama yapıyoruz
        ordering = ['-created_date']




    # DEFTER İÇİN YAPTIKLARIMIZI SIRASIYLA ANLATIYORUM

    """
    ------->>  models.py dosyasındayız

---------------------------------------------------------------------------
    1 - yeni sınıf oluşturduk ve otomatik import idilen models içerisinden miras aldık
    2 - author oluşturduk o kısmı gpt ile araştır biraz karışık
    3- title,content,created_date oluşturduk

    !!! yukarıda oluşturduğumuz modeli kaydetmemiz gerekiyor o yüzden admin.py dosyasına gidiyoruz
---------------------------------------------------------------------------

    ------->> admin.py dosyasındayız    

    1- oluşturduğumuz models klasöründen oluşturduğumuz sınıfı import ediyoruz (nesne tabanlı programlama hatırlarsın)
        .models = yani bulunduğumuz klasörden models isimli dosyayı al ve onun içinden sadece Article sınıfını import et
    2- admin panelinde göstermek için kayıt(register) etmemiz gerekiyor 
        admin.site.register(model adı)
    
    !!! bu kısım bitti ama biz app oluşturup bunu django'ya söylemedik şimdide settings.py dosyasında onu belirtiyoruz
---------------------------------------------------------------------------


    ------->> settings.py

    1- oluşturduğumuz article app'ini installed_apps listesine ekliyoruz
        'article', yapmamız yeterli


    !!! oluşturduğumuz article app'inin içindeki modelleri veritabanında oluşturmadık şimdi onları yapıyoruz

---------------------------------------------------------------------------
*** her yeni model oluşturduğumuzda makemigrations yapmamız gerekiyor
    ------->> terminale gidiyoruz

    1- python manege.py makemigrations'u yapıp oluşturduğumuz programdaki migrationsa getirtiyoruz (kod sayesinde)

    bu işlemi yaptıktan sonra otomatik olarak oluşan 0001_inital.py dosyasına gidiyoruz

    2- python manage.py migrate yapıyoruz 

    bu neden yaptık çünkü makemigrations ile oluşturduğumuz migrations dosyasını(0001_initial.py) migrate etmiş olduk
    (yani veritabanımızda oluşturduğumuz tabloyu kaydettik bu sayede gidip kontol edebilirsin ve admin sayfasından girdiğinde article sayfasında bu tabloyu görebileceksin)
    yani admin panelindeki article içindeki article_article'yi oluşturduk,migrate ettik



    ------->> 0001_initial.py gidiyoruz

    1-biz tablomuzu oluştururken id ve primary key belirtmediğimiz için migrations yaptığımızda django bunu algılayıp otomatik olarak tabloya ekler (ai yani otomatik arttırımlı)
    
---------------------------------------------------------------------------
    ------->> sitenin admin sayfasından article ekle kısmına gidiyoruz

    1- author yani article yazan kişi admin kullanıcıları arasından seçiyoruz
    2- created_date neden yok çünkü onu auto_now_add=True yaptığımız için biz vermiyoruz otomatik alıyor
    3- oluşturduğumuz article'nin yazarı silinirse article de silinir çünkü tabloyu oluştururken author'a on_delete = models.CASCADE verdik

    """
    

class Comment(models.Model):
    #her articlenin birden fazla commenti olabilir o yüzden commentleri Article Modelimiz ile foreign key yardımıyla bağlıyoruz
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Yorumun Gönderildiği Makale", related_name="comments")
    #Article modelini bağladık, on_delete ile eğer article silinirse yorumlarda silinsin diye belirttik
    #related_name nedir? ilerde Article modeline erişirsek o modelin şu tablosuna erişmek istiyorum derken related_name değişkeniyle erişiyoruz
    comment_author= models.CharField(max_length=50,verbose_name="Yazar")
    comment_content = models.CharField(max_length=200, verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)#şuanki zamana göre otomatik eklenecek

    def __str__(self):
        return (f"{self.comment_author}'nın Yorumu: --> {self.comment_content}") #admin panelinden baktığında tabloda gözükecek olanı seçiyoruz
    

    class Meta:
        #yorumların en yeni olanları en üstte gözüksün diye sıralama yapıyoruz
        ordering = ['-comment_date']