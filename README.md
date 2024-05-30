#BLOG PROJESİNİN ADIMLARI 

1-  cmd -> cd onedrive/belgeler/py klasörünü seçtik (cd ile)

2-  cmd -> django-admin startproject blog_django yapıp projeyi başlattık (bu kod dosyaları otomatik oluşturdu)

3-  settings.py -> Dil(tr), Time Zone(Europe/Istanbul) ayarlarnı değiştirdik . Debug en son değiştiririz şimdilik kalsın.

4-  terminal -> python manage.py runserver yaparak dosyamızı çalıştırdık(terminal otomatik olarak dosyanın olduğu konumu seçer zaten)

5-  terminal -> python manage.py migrate yaparak oluşan modelleri veritabanına kaydettik bu sayede sitede görebileceğiz

6-  terminal -> python manage.py createsuperuser yaparak admin(superuser) kullanıcısı oluşturup admin paneline giriş yaptık

7-  terminal -> python manage.py startapp article yaparak kendi uygulamamızı(app) oluşturduk ve ismini article yaptık

8-  models.py -> article class'ı(tablosu) oluşturduk 

9-  admin.py -> from .models import Article yaparak import ettik

10- admin.py -> admin.site.register(Article) yaparak  admin paneline tablomuzu ekledik,kayıt ettirdik

11- settings.py ->  INSTALLED_APPS altına -> 'article', ekliyoruz(virgül'ü unutma) 

12- terminal -> python manage.py makemigrations yaparak oluşturduğumuz tabloyu programa getirtiyoruz(article klasoru oluştur ve içinde 0001_initial.py)

13- terminal -> python manage.py migrate yaparak oluşturduğumuz migrations'u veritabanına kaydedip sitemizde görüntülüyoruz

14- 0001_initial.py -> sayfasına gidip oluşan tabloya bakabilirsin. Bilerek primary key oluşturmamıştık django farkedip kendisi id primary key oluşturdu.

15- localhost:8000/admin -> sayfasına gidip yeni article ekledik 

16- models.py -> tablo objelerine verbose_name ekleyerek sitede gözükeceği ismi belirttik(normalde obje ismi görünüyordu)

17- models.py -> def __str__ fonksiyonu oluştururak localhost:8000/admin/article/article/ sayfasında article object(1)..(99) diye gösterilen article 

    başlıklarını 'return self.title' yaparak article'nin başlığını döndürdük(unutma fonksiyonu sınıf içine yazıyoruz)
    eğer ki orada başka bilgi mesela articlenin başlığını değilde yazarını görüntülemek istersen 'return self.author' 
    mantığı anladın zaten oluşturduğun tablo elemanlarından herhangi birini döndürebilirsin
    doküman -> https://docs.djangoproject.com/en/5.0/ref/contrib/admin/

18- admin.py -> sayfasına gidip register işlemini daha komplike yaparak decorator ile ilişkilendirdik(orada anlattım ne yaptığımızı)

19- admin.py -> dokümandan list display özelliğini bakarak article'nin sadece başlığını değil yazarını,başlığını ve oluşturulma tarihini gösterebilmeyi yapıyoruz

    zaten __str__ ile başlığı döndürüyorduk ama buradan title'ı silersen o fonksiyon işe yaramaz çünkü öncelik list displayda(yani buraya da ekle)
    bu da demek oluyor ki __str__ fonksiyonu işlevsiz kalıyor gerek yok ama ben silmiyorum dursun özel admin registeri kullanmadan nasıl yapıldığını görmek için
    
20- admin.py -> sayfasına gidip list_display_link ile başlığa ve yazara link özelliğini ekledik bu sayede tıklanınca güncellemeye gidecektir

21- admin.py -> sayfasında gidip search_field özelliği ile arama işlevi ekledik ve title üzerinden aranılacağını belirttik

22- admin.py -> sayfasına gidip list_filter ile içeriğin tarihlerine göre filtreleme özelliğini ekledik(istediğin filtreleme kullanabilirsin başlık vb.)

#TERMİNAL ÜZERİNDEN YENİ KULLANICI VEYA MAKALE OLUŞTURMA

23- yeni terminal açıyoruz -> ' python manage.py shell ' yazıyoruz çünkü django ve orm sorgularını yazabileceğimiz python shell'ine ihtiyacımız var 

24- shell ->  (InteractiveConsole) için yaptığımız işlemler:

    1)' from django.contrib.auth.models import User ' djangonun kendi içindeki user tablosunu,modelini almak için dahil ediyoruz (INSTALLED_APPS'e bakabilirsin uygulama orada gözükür)
    2)' from article.models import Article ' kendi oluşturduğumuz modül içindeki Article sınıfını dahil,import ettik 
        yani hem User class'ını hem de Article class'ını ayrı ayrı modüllerden dahil ettik ki bunlardan objeler oluşturabilir ve veritabanına kayıt edebiliriz
    3) newUser = User(username = "denemekullanici",password = "123") yaptık ve yeni kullanıcı oluşturduk
        User tablosunun çok daha fazla parametresi var fakat biz bu iki tanesiyle oluşturduk , veritabanından inceleyebilir veya siteye gidip kullanıcılara bakabilirsin
        tabi bakabilmek için bir sonraki adımda yaptığımız kayıt işlemini yaptıktan sonra inceleyebilirsin
    4) newUser.save() işlemini yaparak oluşturduğumuz kullanıcıyı veritabanına kaydediyoruz
    5) newUser2 = User(username = "denemekullanici2") ilk kullanıcıya normal parola verdik bu yüzden veritabanında parolası şifrelenmemiş olarak gözüküyor
    6) newUser2.set_password("123") yaparak User2'nin parolasını belirliyor ve belirlenen parolayı encrypt yani şifreliyoruz
    7) newUser2.save() yaparak oluşturduğumuz ikinci kullanıcıyıda veritabanına kaydediyoruz
    8) newUser3 = User() yeni boş bir kullanıcı oluşturduk sebebi ise oluşturduktan sonra da parametrelerini verebildiğimizi göstermek
        newUser3.username = "denemekullanici3"
        newUser3.set_password = "333"
        newUser3.first_name = "kullanici3_ismi"
        newUser3.save() yaparak sadece belirttiğimiz parametreleri önceden oluşturduğumuz kullanıcıya vermiş olduk ve veritabanına kaydettik
    9)  article1 = Article(title="Django Shell",content="DS içerik",author= newUser1) yaparak makalemizi oluşturduk
    10) article1.save() yaparak oluşturduğumuz article1'i kaydettik
    11) article2 = Article() yeni boş bir makale oluşturduk sebebi ise oluşturduktan sonra da parametrelerini verebildiğimizi tekrardan göstermek
        article2.title = "2.Makalenin Başlığı"
        article2.content = "2.Makalenin içeriği"
        article2.author = newUser1
        article2.save()
    12) article3 = Article.objects.create(title="Makale 3",content="Makale 3 içerik",author= newUser1) 
            yaparak da makale oluşturabilirsin bu sayede hem tüm işlemleri tek seferde yapabilirsin hem de otomatik kaydeder 
        article3.title = "Makale 3'ün başlığı değişti" yaparak oluşturduğumuz makalenin parametresini sonradan değiştirebiliriz (kaydetmeyi unutma)
        article3.save() yaparak değişikliği veritabanına kaydediyoruz
    13) Article.objects.all() = Article sınıfındaki tüm objeleri gösterir -> sınıf_ismi.objects.all()
        article5 = Article.objects.get(title="Makale 3'ün başlığı değişti") bu kod sayesinde article3'ün değerleri article5'e eşitlendi -> article3 = article5
            burası biraz karışık olabilir hemen daha detaylı anlatıyorum ve neden böyle yaptığımı gösteriyorum 
            öncelikle filtreleme özelliği ile veritabanındaki tüm makaleler arasından başlığı şu olan diye alıp article5'e atadık çünkü bunu yapabildiğimizi göstermek için
            sonra atadığımız değeri silmeyi göstereceğim bu sayede hem silme işlemini öğreneceğiz hemde aynı değere sahip atadığımız 2 objeyi silersek noluru göreceğiz
        article5.delete() yaparak makalemizi siliyoruz
        article6 = Article.objects.get(id = 2) yaparak da id numarasına göre sorgulayıp objeye atayabiliriz
    14) Article.objects.filter(title__contains="She") burada Article sınıfındaki objelerin başlıklarının içinde 'She' geçenleri al dedik
            kullanımı = sınıf_ismi.objects.filter(sütünismi__contains="içinde_geçen_aranılacak_harf_veya_kelime")
            dokümentasyon = https://docs.djangoproject.com/en/5.0/topics/db/queries/ 

25- settings.py -> dosyasına gidip TEMPLATES kısmını buluyoruz ve oradan 'DIRS' : [] bölümüne html templateslerimizin olacağı klasörün adını giriyoruz
    yani templates yazıyoruz . Bunun sebebi ise django templates arayacağı zaman belirttiğimiz klasöre yani directory'e gidecektir. -> 'DIRS' : ['templates']
    
26- html templateslerimizi koyacağımız klasörü oluşturuyoruz . Direkt ana klasörün içersine (blog_django) oluşturuyoruz

27- templates klasörü içersine index.html dosyamızı oluşturup body içersine denemelik h3 etiketinde anasayfa metni ekliyoruz

28- views.py -> dosyanına gidip HttpResponse'u importa dahil ettik sonra index fonksiyonumuzu oluşturduk ve içine HttpResponse ile yazılabilecek deneme metnini gönderdik

29- urls.py -> dosyanına gidip view.py de oluşturduğumuz fonksiyonu dahil ettik (from article.views import index yaparak )

30- urls.py -> anasayfamız için path oluşturup , çağrıldığında çalıştıracağı fonksiyonu belirttik (index fonksiyonu çalışacak)
    bu denemeydi çünkü şuanda index fonksiyonu sadece HttpResponse ile ekrana düz metin basıyor şimdi onu değiştirelim ve kendi templates'imizi verelim
    
31- views.py -> return HttpResponse("anasayfa5") ' yi silip dahil ettiğimiz render fonksiyonunu yazıyoruz -> return render(request,"index.html")
    artık anasayfamız belirlediğimiz index.html sayfası oldu bu sayede 2 yöntemle url göndermeyi gördük (render ve HttpResponse)

#DOCUMENTATION STATIC DOSYALAR İÇİN (https://docs.djangoproject.com/en/5.0/howto/static-files/)
32- settings.py -> Siteden gördüğün üzere kullanabilmek için 2 adet işlem yapmak lazım

    1-  INSTALLED_APPS içinde " django.contrib.staticfiles " olması gerekiyor 
    2- STATIC_URL = "static/" olarak belirtmen gerekiyor 
    #ama şöyle güzel bir detay var biz startproject yaptığımızda django bunları bizim yerimize otomatikman yapıyor(ilk 2) sen sadece kontrol et var mı diye
    3- static klasörünü oluşturup ve içine  css,img,js dosyalarını koyabilirsin
33- articles klasörünün altına static klasörünü oluşturduk ve içinede style.css dosyasını oluşturduk (örnek kodla çalıştırıp deniyelim)

34- index.html -> dosyasına css için bağlantı linki oluşturuyoruz <head> etiketi içersine <link rel="stylesheet" href="../static/style.css"> yaptık

35- index.html -> style.css içersine p {background: red;} yapmıştık o yüzden index'in içersine p etiketli deneme yazısı ekledik ve sitede arkaplanının değiştiğini kontrol ettik

    index.html sayfasına static eklemenin 3 yolu var birisi normal olarak üstteki şekilde ikincisi ile django komutuyla 
        1) <link rel="stylesheet" href="../static/style.css"> bağlantısıyla static dosyamızı belirttik
        2)  1.  {% load static %} kodunu ekledik
            2.  <link rel="stylesheet" href="{% static 'style.css' %}"> ve koduyla static dosyamızın yerini belirttik
        3) static dosyamız app'lerin altında değilde ana dizin altındaysa yani genel bir static dosyamız varsa
            1. settings.py -> dosyasına gidip 
                STATICFILES_DIRS = [ BASE_DIR / "static",] ekledik
            2. index.html sayfasına {% load static  %} ekledik
            3. index.html sayfasına <link rel="stylesheet" href="{% static 'style.css' %}"> ekledik
        # 3. işlem 2.olana çok benziyor çünkü aynı şey sadece aralarındaki fark static dosyası app içinde değil ana dizinde bulunuyor
36- layout.html sayfası oluşturduk ve boostrap 4 cdn diye aratarak introduction için quick startı dahil ettik ( flask ile aynı işlem ) 

37- layout.html -> div class container oluşturduk ve içine block oluşturduk bu sayede extend ettiğimizde içersine ekleme yapabileceğiz 

38- index.html -> tüm kodları silip django komutu yani extend ekleyip layout.html'i belirttik ve block body'i ekleyip içersine deneme metin ekledik

    sitede görünüyor mu diye kontrol ettik ve göründü . Kısaca görünmesi için yaptıklarımız :
        1) views.py dosyasında index fonksiyonu oluşturduk
        2) urls.py dosyasında index fonksiyonunu import ettik ve url path'i oluşturup kök dizin için index fonksiyonunu çalıştırmasını belirttik
        3) index.html sayfasını oluşturduk (layout.html'den extend etme sebebimiz navbar)
        
39- urls.py -> 

    bundan sonra daha fazla fonksiyon ve url için path yapacağımız için import etmeyi daha kullanışlı yapıyoruz
    from article import views yaparak import edebilir ve direkt views içindeki bütün fonksiyonları çağırabiliriz
    !! fakat bunu yaptığımızda fonksiyonu belirtirken direkt isim değil views.fonksiyon_ismi olarak belirtmemiz gerekiyor
    örneğin: from article import views yaptık ve path içinde about fonksiyonu belirtirken --> path('/about', views.about , name= "about") olarak belirtmeliyiz
    
40- index.html -> flask dosyamızdan index.html için yaptığımız div class jumbotron'u alıp buraya yapıştırdık (hoşgeldiniz ekranı gibi bir şey)

41- templates altına includes klasörü oluşturup onun içine de navbar.html dosyasını oluşturduk ve içeriğini flask navbar'dan alıp yapıştırdık (blog sayfam,hakkımda ve makaleler)

42- hakkımda sayfası oluşturuyoruz 

    1) templates altına about.html dosyasını açtık ve içine extend layout.html ve block body ekledik
    2) views.py kısmına gidip def about fonksiyonu ekleyip render about.html olduğunu belirttik
    3) urls.py kısmına gidip path için url'yi /about olarak ve fonksiyonu da views.about olduğunu belirttik (path bittikten sonra virgül atmayı unutma)
43- Siteye veri gönderme işlemi nasıl yapılır?

    oluşturduğumuz fonksiyon içersindeki Render() hangi değerleri alır üstüne gelip bakabilirsin
    veri göndermek için üçüncü değer yani Context olanı veriyoruz ama sözlük olarak girmemiz gerekiyor örneğin:
    örnek 1) 
    def index(request):
        context= {
            'title': 'Home',
            'message':'Welcome to my website!',
            #'name': request.GET['name'],
            'name': request.GET.get('name','Guest'),
            }
        return render(request,'index.html',context) --> bu kısım sayesinde context = {...} 
        # diye belirttiğimiz sözlüğün tüm verileri siteye gönderilmiş oldu ve sitede bu veriler context.title, context.message gibi kullanılabilir
        index.html -> veriyi direkt gönderdiğimiz için ismini python yorumlayıcısı içersinde söylemek yeterli olacaktır
            <p> {{title}} --> context başlığı</p>
            <p> {{name}} --> context ismi</p>
            <p> {{message}} --> context mesajı</p>  yaparak sitede bunları görüntüleyebiliriz

    örnek 2)
        context= {
            "numbers" : [1,2,3,4,5,6,7,8,9],
            }
    return render(request,'index.html',context)

    index.html -> 
    <ul>
        {% for number in numbers  %}
            <li>{{number}}</li>
        {% endfor %}
    </ul>   yaparsak for döngüsüyle liste içindeki her elemanı sitede listeleyecektir 

44- Dinamik URL nasıl yapılır ?

    1) views.py -> 
        def details(request,id):
            return HttpResponse("Details:" + str(id)) -> fonksiyonumuzu oluşturduk (httpresponse ile verme sebebim sadece örnek bu )
    2) urls.py -> 
        path('details/<int:id>/',views.details, name='details') flask uygulamasından tek farkı string değil int dinamik değer alır.

45- article klasörü içinde urls.py dosyası açtık ve 2 urls.py dosyasını birleştirip, include edip bir link üzerinden fonksiyon çalıştırdık
    bu işlemi burada anlatmadım urls.py(article) dosyasında detaylı anlattım oraya bakabilirsin

46- Yeni bir User uygulaması(app) oluşturuyoruz fakat models.py içine modül oluşturmayacağız çünkü django'nun user sınıfı ile oluşacaklar zaten.

    (admin.py içine register yapmaya da gerek yok)
    1) terminal ->  python manage.py startapp user ile uygulamayı oluşturduk
    2) user klasörü içine urls.py dosyasını oluşturduk
    3) diğer urls.py dosyasından dahil ettiklerimizi ve urlpatterns'i aldık düzenledik
    4) uygulamamıza isim verdik app_name="user"
    5) register,login ve logout olmak üzere 3 tane path ekledik ve fonksiyonlarını belirttik(fonksiyonları sonradan oluşturacağız şimdilik yazıyoruz)
    6) user klasöründeki views.py dosyası -> pathler için belirttiğimiz fonksiyonları oluşturduk (register,loginUser ve logoutUser) pass yaptık şimdilik
    7) blog_django > urls.py -> path('user/',include("user.urls")), ekledik çünkü  user/register , user/login , user/logout adreslerini burdan include edeceğiz
    8) templates > register.html dosyasını oluşturduk ve layout.html'i extend ettik ve block body'i ekledik
    9) templates > login.html dosyasını oluşturduk ve layout.html'i extend ettik ve block body'i ekledik
    10) user > urls.py -> register ve login fonksiyonlarına return render ile oluşturduğumuz html sayfalarını döndürdük ve siteye gidip user/register ve user/login denedik

47- Uygulamayı djangoya belirtmeyi unuttuk ama uygulama hata da vermedi neden?

    Çünkü user uygulamamızın içersinde model oluşturmadık ve djangonun kendi user modelini kullandık
    Django zaten kendisi belirttiği uygulamaları migrate ettiği için bizim uygulamamızın içinde model olmadığından hata vermeden çalıştı
    Ama biz yine de şimdi djangoya belirtiyoruz çünkü uygulama içersinde ileride model oluşturabiliriz
    settings.py -> içersine girip "INSTALLED_APPS" listesi içersine "user",   diye ekledik

48- User tablasu için form classlarını oluşturacağımız dosyayı açıyoruz
    User uygulaması içersine 'forms.py' adlı dosya açtık
    Forms dosyası için bilgileri dosya içine kaydettim oradan devam edebilirsin

49- views.py -> forms.py üzerindeki işlemleri bitirdikten sonra oluşturduğumuz formu sitemizde göstermemiz gerekiyor
    şuan sadece formu sitede göstermek için bu işlemleri yapacağım , detaylarını sonra göstereceğim

    register fonksiyonu için:
    from .forms import RegisterForm yaparak bulunan dizinden forms modülü içindeki RegisterForm'unu import ettik
    form = RegisterForm() yaparak boş bir sınıf objesi oluşturduk
    context sözlük oluşturup formu(boş sınıf objesi çünkü amaç sadece göstermek) içine ekledik
    context'i siteye gönderdik

    register.html -> sayfasına gidip form etiketi açıp içine sitede formumuzu göstermek için django kodunu yazıyoruz '{{form.as_p}}'
    bu kod sayesinde oluşturduğumuz formu sitede gösterebiliriz

50- views.py -> sayfada şuanda sadece get request olduğunda formumuzu sayfada görüntülüyorduk onu if request.method ile düzenledik 
    def register için oluşturduğumuz clean (password ve confirm eşleştirmesi) fonksiyonunun nasıl yapıldığını gösterdik
    daha detaylı anlatımı user > views.py sayfasında görüntüleyebilirsin

51- CSRF ->  (Cross Site Request Forgery) form işlemini korumak için django tarafından güvenlik protokolü sayılabilir
    register.html sayfasındaki form için views.py de ki işlemlerimiz bitti şimdi bu hatayı alıyoruz , onu da şöyle düzeltebiliriz

    register.html -> sayfasına gidip form etiketi içersine '{% csrf_token %}' ekliyoruz ve django ataklardan böyle kurtuluyor

52- DJANGO MESSAGES (flask flash message ile benzer) bilgilendirme, ekranda mesaj gösterme

    dokümentasyon: https://docs.djangoproject.com/en/5.0/ref/contrib/messages/
    normalde kullanabilmek için kurulum işlemi var ama biz django-admin startproject ile otomatik proje açtığımızdan django onları yapmıştı
    1- öncelikle import, dahil ediyoruz (kullanmak istediğin her sayfa için dahil etmek lazım '.py olanlara')
        views.py ->  from django.contrib import messages
    2- messages.mesaj_türü(request, 'mesaj içeriği') olarak kullanıyoruz örnek -> messages.success(request,'başarıyla kayıt olundu')
       djangoda normalde danger mesajı kullanılmıyor
    3- sitede mesajın görünmesi için dokümentasyondaki django message display kodunu alıp ana html sayfamıza yapıştırıyoruz
       buradaki olay şu neden biz bunu layout.html sayfasına koyuyoruz çünkü diğer tüm sayfalar bunu extend ediyor bu sayede
       sadece layout.html sayfasına ekleyerek diğer tüm sayfalarda da gözükmesini sağlıyoruz
        layout.html -> dokümentasyonda ki django message display kodunu body > div içine ekliyoruz bu sayede yukarıda ama navbar'ın altına gözükecek
    4- aslında işlem tamamlandı ama mesajı daha güzel hale getirmek için ul etiketini silip li'yi div yaptım ve 
       class'ını alert alert-{mesaj} yaparak views.py de messages.mesaj_türü olarak belirttiğimiz tür neyse onu bastırsın diye düzenledik

    !! EĞER Kİ DANGER MESAJINI KULLANMAK İSTERSEK NASIL YAPARIZ ?
    - önce mantığı anlatayım : dangeri kullanmak için herhangi bir mesaj türüne sen danger ol diyebiliriz kabaca x türü çağrılınca onu danger'a çeviriyorsun

    nasıl yapılır bunu kendi yaptığımız django message display da gösteriyorum

    {% if messages %}
            {% for message in messages %}
                {% if message.tags == "info" %}
                <div class="alert alert-danger">{{ message }}</div>
                {% else %}
                <div class="alert alert-{{ message.tags }}">{{ message }}</div>
                {% endif %}
            {% endfor %}
    {% endif %}

    # ne yaptık basitçe anlatmak gerekirse, 
    eğer mesaj etiketi info olarak gelirse onu dangera çevir , aksi takdirde ne geldiyse onu ekrana bastır dedik 
    bu sayede belirli bir türü dangera çevirdik(ben sayfada info kullandığım için onu gösterdim istediğin herhangi birisi olur)

53- LOGİN SAYFASI/FORMU YAPIYORUM

    1- forms.py -> login formu oluşturduk 
    2- login.html -> form etiketi açıp içine csrf token , buton ve formumuzu yazdık
    3- views.py(user) ->
        1> ilk önce login formumuzu dahil ediyoruz
        2> LoginUser fonsiyonunu düzenledik (if bloğuna kadar)
        3> from django.contrib.auth import authenticate dahil ediyoruz 
            # authenticate = bu fonksiyon aldığı username ve password bilgisine göre eğer kullanıcı varsa bize bilgisini dönücek
            # eğer kullanıcı yoksa bize none değerini dönücek bu sayede değer eğer none ise diye koşul da açabiliriz sonra
            # user = authenticate(username=username, password=password) -> yaparak kontrolü sağlıyoruz
        4> user is none ile uyuşan kullancı yoksa hata mesajı gösteriyoruz
        5> user is none girmiyorsa kullanıcı uyuşuyor demektir hoşgeldin mesajı ve login işlemi yapıp yönlendirme yapıyoruz
        6> eğer ki form.is_valid() ' e hiç girmemişse return render(request, 'login.html',context) yapıp aynı sayfaya yönlendiriyoruz
    
54- Djangoda ki formlarımızı bootstrap 4 grids ile düzenliyoruz

    > siteden div etiketi alıp sonra login.html sayfasındaki verileri divin içine taşıyoruz
    > bu sayede responsive bir tasarım yaptık pencere küçülse de yazı hep pencere içinde ortalanıyor
    > sonraki işlemleri 55.maddede gösteriyorum orayı ayrı belirtme sebebim farklı bir konu ama ikisini bir yaptım

55- DJANGO FORMLARIMIZA BOOTSTRAP DAHİL ETMEK İSTERSEK DJANGO CRISPY FORMS(3.parti yazılım) İLE YAPIYORUZ 

    1- ' pip install django-crispy-forms ' koduyla cmd üzerinden bilgisayara yüklüyoruz
    2- settings.py ->  installed apps listesi içersine crispy formsu ekliyoruz 
    INSTALLED_APPS = (
        ...
        'crispy_forms',
    )
    3- settings.py -> dosyasına bunu ekliyoruz ve projeye dahil ediliyor --> CRISPY_TEMPLATE_PACK = 'bootstrap4' 
    4- html sayfalarında formları dahil etmek için kullandığımız {{form.as_p}} kodunu artık crispy kullanacağımız için düzenliyoruz 
       1> {% load crispy_forms_tags %} ile öncelikle sayfaya crispyi dahil ediyoruz block body içersine üste koydum
       2> {{ form |crispy }} olarak form çekmeyi düzeltiyoruz ve tamamdır
    !! derste böyle oluyordu ama ben hata aldım ve bunu normal olarak anlatmıcam derse ek olarak anlatıcam o yüzden burdan sonrakiler eğer hata alırsan
       settings.py ->
       1> installed apps içersine "crispy_bootstrap4", de ekledim
       2> CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4" diye en alta da ekledim # bunu kaldırınca da oluyor ama ne olur ne olmaz kalsın
       
56- LOGOUT İŞLEMİNİ YAPIYORUM 

    1- views.py -> from django.contrib.auth import logout dahil ediyoruz
    2- views.py -> def logoutUser fonksiyonu içersine logout(request) eklememiz yeterli 
    3- views.py -> def logoutUser fonksiyonu içersine ekrana mesaj bastırabilirsin ve sonra redirect ile yönlendirme yapıyoruz , bu kadar

57- SESSION KULLANIMI YANİ KULLANICI GİRİŞ YAPTI MI

    > Session neden kullanırız bazı sayfalar vardır tüm kullanıcılar görüntüleyebilir örnek veriyorum anasayfa çünkü içerik herkese yöneliktir
      fakat kontrol paneli gibi makalelerin kontrolünü yaptığımız sayfaya herkesin erişmesini session ile engelliyoruz daha doğrusu onun kontrolü ile izin vermiyoruz
    1- Navbar.html -> sayfasındaki butonları düzenledik normalde ben hep düzenliyorum ama buraya yazmıyordum şimdi belirttiklerimi yap yeterli
      > sağ taraf için -> soldan sağa sıralıyorum --> admin-kontrol paneli-kayıt ol-giriş yap-çıkış yap (bunları ekledim)

    !! KONTROLÜ NE YAPAR? -> request.user.is_authenticated -> True veya False döner , True ise giriş yapıldı False ise giriş yapılmadı demektir
    2- navbar'a gidip eğer kullanıcı giriş yaptıysa sadece çıkış yapı ve kontrol panelini göster(giriş yap ve kayıt olu gösterme) gibi kullanımlar yapıyoruz
      > {% if request.user.is_authenticated %} yani kullanıcı giriş yaptıysa true dön yapmadıysa false dön
      > {{request.user.username}} true dönerse bunu yapıyoruz yani giriş yapan kullanıcının adını alıyoruz
      > else yani false dönerse giriş yapılmadı diyoruz ----> detaylarına navbar.html'den bakabilirsin
      > giriş yapılanlara -> çıkış yap,kontrol paneli ekledim | giriş yapılmayanlara -> kayıt ol,giriş yap ekledim | admin koşul içinde değil herkes görebilir

58- KONTROL PANELİNİ OLUŞTURUYORUZ (MAKALELERİ DÜZENLEYECEĞİZ O YÜZDEN ARTICLE UYGULAMASI ÜZERİNDEN DEVAM)

    1- article > views.py -> def dashboard oluşturuyoruz
    2- article > urls.py -> path('dashboard/',views.dashboard,name= 'dashboard'), urlpatternse ekliyoruz

    !! şöyle bir önemli nokta var hatırlamazsın diye yazıyorum biz blog_django > urls.py dosyasında include işlemi yapmıştık
    path('articles/',include("article.urls")), --> yani oluşturduğumuz fonksiyon /dashboard ile değil article/dashboard ile çalışacak
    diğer yaptığımız create mantığı gibi düşün (45.madde de belirttiğim gibi article > urls.py dosyasında anlattım mantığını)
    3- templates > dashboard.html oluşturduk ve extend layout , block body defaultlarımızı koyduk
    4- dasboard.html -> makale ekle linki koyuyoruz ve urlsini article/addarticle yapıyoruz
    böyleylikle dashboard işlemi şuanlık bitti , makale eklemek için sayfamızı ve sayfadaki formumuzu oluşturacağız

59- MAKALE EKLEMEK VE FORM SAYFASINI OLUŞTURMAK

    1- article > urls.py -> path('addarticle/',views.addarticle,name= 'addarticle'), urlpatternse ekliyoruz
    2- article > views.py -> def addarticle oluşturduk
    3- templates > addarticle.html oluşturduk ve  extends layout girdikten sonra block body da ekledik

    4- article > forms.py dosyasını oluşturduk ve oradaki işlemleri yaptık # bunu orada anlattım inceleyip buradan devam et
    5- article > views.py ->  from .forms import ArticleForm  yaparak modelimizi dahil ediyoruz
       > form = ArticleForm() yaparak sadece get request yapılınca formu gösteriyoruz ve işlem bitiyor 
       > render içine context(sözlük) oluşturup sitemize formumuzu gönderiyoruz (farklı yol olarak böyle de yapılıyor direkt context olarak göndermeden) 
       devamını ve düzenlemesini ilerde yapıcaz şuanlık basitçe eklemeyi gösterdim
    6- addarticle.html -> formumuzu sitede göstereceğiz bunu login.html sayfasından kopya çekerek ekleyebilirsin(crispy olanı almayı unutma) 

60- VERİTABANINA VERİ,MAKALE KAYDETMEK

    1- article > views.py -> 
       1.messages import ettik
       2.article = form.save(commit=False) yaparak sen formu gönder ben kendim kaydederim dedik
       3.yazarımızı kendimiz belirttik (login yapmış kullanıcı)
       4.işlemleri yaptıktan sonra commit yani kaydetmeyi yap dedik(save)
       5.başarılı işlemi ekrana bastırdık
       6. redirect ile anasayfaya yönlendirdik
       7. zaten is.valid()'e girmediyse return render ile aynı sayfayı renderladık

61- MAKALELERİ DASHBOARD(kontrol paneli) DA GÖSTERMEK(sadece giriş yapan kullanıcının kendi makaleleri)

    1- article > views.py -> adımları orada gösterdim def dashboard içinde
       - kısaca ne yaptık ilk önce modeli dahil ettik 
       - girilen kullanıcı adıyla eklenmiş makaleleri alıp articles objesine atadık
       - articles objesini(liste) context'e atayıp sonra contexti siteye gönderdik
    2-  dashboard.html -> sitemizde göstermek için ekleyeceğiz ama ben güzel görünmesi için bootstrap table kullanacağım 
       - arama motoruna 'bootstrap 4 tables' yazıyoruz çıkan ilk siteden beğendiğin bir tabloyu al benim ki zaten kaynak dosyasında inceleyebilirsin

62- MAKALE SAYFASINI DETAYLANDIRMAK ( dashboard düzenleme )

    1- Öncelikle başlığa link özelliği ekleyip ona tıklandığında o makaleyi görüntüleme sayfasına gitsin istiyorum
       - dashboard.html -> sayfasında article.title kısmına a etiketiyle statik id ekleyip birazdan oluşturacağım sayfaya yönlendiriyorum
    2- article > urls.py -> sayfasına o linke tıklandığında gidiceğimiz sayfanın path'ini veriyoruz 
       - path('article/<int:id>',views.detail,name= 'detail'), bunu yapma amacımız blog_django > urls.py tarafından include edildi unutma
       bu da demek oluyor ki articles/article/<int:id> çağrıldığında views.py dosyasından detail fonksiyonunu çalıştır
    3- article > views.py -> detail fonksiyonunu oluşturuyoruz
       - zaten buraya models.py den Article modelini dahil etmiştik o yüzden tekrar etmiyoruz
       - fonksiyona zaten django id'yi otomatik gönderiyor o yüzden request,id yapmamız yeterli
       - sonra id'si bu numaraya eşit olan makaleyi get ile getiriyoruz ve article objesine atıyoruz
    4- detail.html -> yeni sayfa oluşturuyoruz , extend ve block işlemlerini yapıyoruz
       - sayfanın daha güzel görünmesi için internetten 'start bootstrap blog post' diye aratıp siteye giriyoruz
       girdiğimiz sitenin kaynak kodlarından page content içindeki contentin içindeki row'a ait tüm kodu alıyoruz(container var diye almıyoruz)
       site biraz değişmiş o yüzden ekranın ortasında view source code var ona tıkla sonra githuba gidip dist > index.html içine bak ordan al rowu
       - sayfada gerekli düzenlemeleri yaptık(ana kod templates>includes>posttemplate içinde duruyor inceleyebilirsin)
       
    !! 
    makale sayfasında eğer id numarası ile makale yoksa bu sefer def detail içindeki obje boş dönecek ama yine de siteye gidecek
    siteye gittiği için if articles true olacak çünkü gelen değer boş olsa da var bu yüzden sitede hata mesajı vermek yerine formlarımız boş olarak gözükecek
    bunu nasıl çözeriz ? bunun mantığını get_object_or_404 ile çözüyoruz hemen altta anlatıyorum ve bu 62-63.maddeler birleşik sayıldığı anlamına geliyor

63- GET OBJECT OR 404 (article > views.py ) 

    - erişilen sayfaya ait id  numarasıyla eşleşen makale olmadığında boş form bastırmak yerine 404 eror sayfası bastırmak için kullanacağız
    - Kullanımı : get_object_or_404(model_adı,sorgu)# verilen id ile aranan modelde eşleşen varsa verir,yoksa 404 hatası bastırır


    1- Önce import ediyoruz 'from django.shortcuts import get_object_or_404'
    2- sonra makalemizi bulup article objesine atıyoruz 'article = get_object_or_404(Article,id = id)'
    !! debug=True olduğu için page not found hatası verecektir, normal siteye attığımızda 404 hatası verecektir(olması gereken) 

64- BOOSTRAP DOSYALARINI DÜZENLEME

    1- Statik altında ki style.css dosyasını siliyorum
    2- Statik altına css ve js adında 2 klasör açıyorum (css ve javascript)
    3- layout.html sayfasında kullandığımız bootstrap script dosyalarının isimlerini alıyoruz ve internetten indiriyoruz
       - bootstrap 4 alpha 6 (alpha 6 has landed) yerinden zip dosyasını indirdik
       - indirdiğimiz dosyanın içinden bootstrap.min.css dosyasını alıp oluşturduğumuz css dosyasının içine attık
       - indirdiğimiz dosyanın içinden bootstrap.min.js dosyasını alıp oluşturduğumuz js dosyasının içine attık
       - 'jquery download' yaparak ilk siteye gidip indir dediğimizde attığı metni kopyaladık(https://code.jquery.com/jquery-3.2.1.min.js)
       - js klasörünün içine yeni 'jquery-3.2.1.min.js' adında dosya açıp metni içine yapıştırdık
    4- layout.html üzerinde ki meta içindeki link ve body altındaki scriptleri siliyoruz artık onlara ihtiyacımız kalmadı
    5- indirdiğimiz dosyalar static klasöründe olduğundan layout.html sayfasına statiği load edip yüklüyoruz ( {% load static %} )
    6- meta içine yeni link ekliyoruz ve href'ini eklediğimiz dosyayı belirtiyoruz (<link href:"{static '{% static 'css/bootstrap.min.css' %}'})
    7- body altına script ekleyip src'sini "{% static 'js/bootstrap.min.js' %}" ekliyoruz
    8- body altına script ekleyip src'sini "{% static 'js/jquery-3.2.1.min.js' %}" ekliyoruz
    ! aslında şuan işlemimiz bitti fakat biz djangonun bize önerdiği bütün css ve js dosyalarını bir klasörde birleştirmesini yapıyoruz

    9- django static files yazarak aratıyoruz ve ilk bağlantıya giriyoruz
       1- static url olarak settingse kaydetmiştik  ve layout.htmle {% load static %} yaptık zaten
       2- STATICFILES_DIRS = [BASE_DIR / "static",] de yapmıştık zaten (bu ikisi sayesinde js ve staticleri kullanıyorduk zaten)
       bu uygulamayı bir servera attığımız zaman bizim bir tane daha ayar yapmamız gerekiyor
       !! birazdan oluşturacağımız dosyanın ismi farklı olması gerekiyor aynı yapamazsın (staticfiles yaptım)
       bütün js ve css dosyalarını oluşturacağımız yeri gösteriyoruz
       3- STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles") # ve import os yaptım (settings.py)
       4- son olarak django da ki bir tane komutu çalıştırmamız gerekiyor , terminale giriyoruz ve 'python manage.py collectstatic' yapıp çalıştırıyoruz
       bu işlemin sonunda djangonun kendi oluşturdu js ve css dosyaları dahil tüm dosyaları staticfiles adında yeni klasör açıp içine attı.
       kısaca djangonun istediği düzeni static dosyaları için yaptık ve böylelikle erişim daha kolay olacaktır

65- CK EDİTÖR EKLEMEK (FORMLARI DAHA GÜZEL GÖSTERMEK VE DAHA İŞLEVSEL HALE GETİRMEK)

    - 'django ckeditor' diye arattığımızda çıkan ilk siteye(github) giriyoruz ve  adımları yerine getiriyoruz
    kurulum(Installation):
       1) ilk önce bilgisayarımıza indiriyoruz 'pip install django-ckeditor'
       2) settings.py dosyasında ki INSTALLED_APPS içine  "ckeditor", -> ekliyoruz
       3) ckeditor içersindeki js ve css dosyalarını ana dizine taşımamız gerekiyor yeni terminal -> python manage.py collectstatic yapıyoruz
       !! önceden bu işlemi yaptığımız için staticfiles klasörü mevcut üstüne yazma işlemi için izin isteyecek ona yes diyoruz 
    kullanım(Usage):
       önce oluşturduğumuz model sayfasına gidiyoruz orada işlem yapacağız biz textarea koymuştuk artık onu ckeditor ile değiştirelim
       1) article > models.py -> dosyasına gidip ' from ckeditor.fields import RichTextField ' dahil ediyoruz
       2) content = RichTextField() -> yapıyoruz burası önceden 'content = models.TextField(verbose_name="İçerik")' di
       3) addarticle.html -> formumuzun içine crisp'in üstüne {{form.media}} ekliyoruz (form.as_p eklemiyoruz çünkü bizde zaten crispy var)
       !! aslında şuan bitti ama biz code snippets özelliği ekleceğimiz için ve flasktan hatırlayacağın üzere ckeditor o konuda hata verdiğinden
       şimdi onu düzeltmeyi göstereceğim
       - sitede ctrl+f ile arama yapıp config kısmını bul (allowedContent)
       - settings.py -> alttakileri ekliyoruz
                            CKEDITOR_CONFIGS = {
                                "default": {
                                    "removePlugins": "stylesheetparser",
                                    "allowedContent" : True,
                                    "width" : "100%",
                                }
                            }
        buralarda birkaç sorun vardı çözmeye baya uğraştım ama neler yaptığımı tam hatırlamıyorum devamını o yüzden yazmıyorum

66- FILE UPLOAD (DOSYA YÜKLEME İŞLEMİ)

    !! dokümentasyon paylaşıyorum orada anlatım var ve biz orası üzerinden gidiyoruz
    (https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html)

    1- Formlarımızda gönderdiğimiz dosyalarımız veya resimlerimiz 'request.FILES' içinde bulunuyor (artık postun içersinde değil burada bulunuyor)
       bunları almak içinse bizim formumuza extradan '  enctype="multipart/form-data"  ' eklememiz gerekiyor , eğer eklemezsek dosyayı yüklesek bile
       request.FILES her zaman boş geliyor

       Daha sonra biz bu formu POST şeklinde SUBMIT ettiğimiz zaman django tarafından request.FILES üzerinden bu dosyalarımıza erişebiliyoruz
       -Sonradan modellerimizde artık bir tane FILE alanı olacağı için bunu istersek FileField veya ImageField şeklinde oluşturabiliriz
        FileField: Bütün dosyalarımızı(pdf,video,fotoğraf vb.) upload etmek için kullanılıyor
        ImageField: Sadece fotoğraf yüklemek için kullanılır ayrıca ImageField'ın çalışması için extra bir modüle daha ihtiyacımız oluyor( PILLOW )
        !! Önceki derslerden hakimsen zaten pillow modülünü yapmıştık hatırlıyorsundur ve bilgisayarda yüklüdür (değilse 'pip install pillow')

    2- Dosyalarımızı yüklediğimiz zaman bir yerde birikmesi saklanması gerekiyor bunu da MEDIA klasörü açarak yapacağız
        settings.py -> dosyasına gidip 2 tane tanımlama ekliyoruz (kaynaktan bakabilirsin)
        -MEDIA_URL = '/media/'
        -MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        !! media klasörünü oluşturmaya gerek yok biz herhangi bir dosya upload ettiğimiz zaman django onu otomatik olarak oluşturacaktır
    3- Python dosyalarından media_url ve media_root'a erişmemiz için bu işlemleri yapmamız gerekiyor
        blog_django > urls.py ->

        -from django.conf import settings
        -from django.conf.urls.static import static
        - bunları dahil ettikten sonra en alta şunu ekliyoruz 'urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'

    4- Bizim media_urlmize templates üzerinden erişmemiz için templates değişkenine bunu belirtmemiz gerekiyor
        settings.py -> templates listesine diğerlerinin altına ekliyoruz
        -  'django.template.context_processors.media',
        !! Bu işlem neden önemli ?
        #Çünkü media url'sini dinamik olarak veriyoruz fakat Django sayfalarını statik olarak derlediğinde media url'si null olur.
        Çünkü biz addarticle.html sayfasında formumuzu göndereceğiz(image upload yapacağız) ancak başka bir dosyada bu image göstermemiz gerekiyor
        onun için bu işlemi yapıyoruz

    5- İşlemleri bitirdikten sonra django uygulamasını internetten indiriyoruz. 'Django clean_up' diye aratıyoruz ve pypi sitesine giriyoruz
       !! ne işe yarar? eğer makalemizde resim varsa ve biz makaleyi silersek bu program otomatik olarak ona bağlı medyaları yani resim vb dosyalarını
       da siler bu sayede programda artık kalmaz ve kalıcı silinme işlemini gerçekleştirir.
       * dokümentasyon : https://pypi.org/project/django-cleanup/
       - ' pip install django-cleanup ' yaparak indiriyoruz
       - INSTALLED_APPS listesine ('django_cleanup',) ekliyoruz
       - şuan bunu yaptık ve artık models.py dosyasına media inputu ekleyeceğiz ama bu durum modelimizi değiştirdiğimiz anlamına geliyor
       djangoya bunu belirtmezsek hata verecektir o yüzden şimdi ki adımlar çok önemli dikkatli ol
    
    6- article > models.py -> article_image ekledik ve gerekli parametreleri verdik .
       !! Artık modelimiz değişti bunu djangoya belirtmemiz ve veritabanındaki tablo yapısını değiştirmemiz gerekiyor

    7- terminal -> 
       -'python manage.py makemigrations' yaparak (installed apps) listesini migrate ediyoruz
       -'python manage.py migrate' yaparak da bunu veritabanında işlemiş oluyoruz 
       !! bu iki işlem sayesinde veritabanı ve modeli değiştirdiğimizi belirttik 

    8- önceden oluşturduğumuz modelden alıntılayarak yeni modeli kolay oluşturma işlemi yapmıştık 
       - article > forms.py -> dosyasında addarticle için sadece title ve content eklemiştik onu düzenleyerek artık orada medyayıda görüntülemek istiyoruz
       - fields = ['title', 'content','article_image']
       - işlemlerden sonra kaydettiğini kontrol edip siteye gidip addarticle kısmına bakabilirsin şuanda oraya geldi
    
    9- Artık işlemlerimiz neredeyse bitti , resim eklemek istersek bunu nasıl yapıyoruz
       - article > views.py -> formumuz request.post or none olduğu için files kısmını algılamıyor o yüzden onun yanına ekleme yapıyoruz
       - def addarticle(request): 
            form = ArticleForm(request.POST or None,request.FILES or None)

    10- Normal işleyişte buraya kadar her şey iyi fakat makale eklemeyi denediğimizde resim yüklesek dahi media klasörü oluşmuyor ama hata da vermiyordu
        biraz araştırdım ve sıkıntının çözümü formumuzu encytpe etmek olduğunu buldum . Nasıl yaparız ?
        -addarticle.html -> sayfasına gidip formumuzu şu şekil değiştiriyoruz 
        -                  <form method="POST" enctype="multipart/form-data">
        - şimdi tekrar bir makaleye resim eklemeyi dene ve media klasörü oluştuğunu ve içine resmin geldiğini göreceksin
        - unutma henüz siteye resim görüntülemeyi eklemedik o yüzden makaleyi görüntülerken göremezsin :) (sonraki adımda onu yapacağız)

    11- Eklediğimiz resim dosyasını details sayfasında göstermek
        - Detail sayfasında resmin urlsini almak ve bu sayede sitede göstermek için gerekli izin ve işlemleri önceden yaptık zaten şimdi sadece eklemek kaldı
        - Details.html -> sayfasına gidip image kısmının kaynağına python verisi olarak article_image.url'sini ekliyoruz 
        - bu işlemden sonra makale sayfasına gidip resmi görüntüleyebilirsin işlem başarıyla tamamlandı 

    12- Yaptığımız işlemlere göre eğer resmi olmayan makale görüntülemeye çalışırsak hata alacağız çünkü onun article_image objesi olmadığı için
        - Peki bunu nasıl düzeltiriz ? details.html sayfasında resmi bastırmadan önce koşula sokarak basit bir şekilde çözebiliriz
        - eğer article_image varsa buraya gir ve sonra resmi bastır , yoksa zaten bastırma :)
    
    13- Son olarak eğer ki ben makaleyi silersem media klasöründeki resim dosyası da gidecek mi hemen kontrol ediyoruz 
        - Admin paneline gidip oradan resimli makalemizi siliyoruz(sorduğunu duyar gibiyim kontrol paneline henüz silmeyi eklemedik çünkü)
        - Resimli makaleyi seçip sildikten sonra media klasörünü kontrol et ve django_cleanup sayesinde onun da silindiğini göreceksin
        - evet file upload baya karmaşık görükse de bu kadar basit aslında (hayır değil baya karmaşık ama çaktırma) haydi bakalım devam durmak yok

67- MAKALE SAYFASINDA HTML İÇERİĞİ YORUMLAYICI OLARAK GÖSTERMİYOR , PROBLEMİNİ DÜZELTME

    - sayfaya italic , kalın yazı , ton değişikliği vb. şekilde eklersek ve görüntülediğimizde bunu göstermiyor kodları gösteriyordu hemen onu düzeltelim
    - details.html -> sayfasına gidip flaskda ki yaptığımız safe işlemini yapıyoruz
    - {{article.content | safe}} -> content bastırma işlemini safe olarak belirtiyoruz bu kadar

68- MAKALE GÜNCELLEME SAYFASI EKLEMEK

    !! önceden kontrol paneline eklediğimiz güncelle butonuna işlevsellik katacağız, önceden oluşturduğumuz makeleyi düzenlemeyi yapacağız
    ve veritabanına kaydetmeyi halledeceğiz . 3 adımda güncelleme işlemini yapmak (aynısı gibi silme işlemini de yaptıktan sonra dashboard bitiyor)
    
    1) article > urls.py -> pathimizi ekliyoruz "  path('update/<int:id>/',views.updatearticle,name= 'update'), "
    2) article > views.py -> fonksiyonumuzu oluşturuyoruz return render(request,"update.html")
    !!      (sonradan içeriğini ayarlıcaz şimdi ilk temeli ayarlıyoruz )
    3) update.html template dosyasını oluşturuyoruz (addarticle.html ile aynı olacağından oradan kopyaladık ve düzenledik)
    4) article > views.py -> artık her şey hazır şimdi güncelleme işlemini ve sayfada görünecek formlarımızı yapıyoruz
       -Dahil ettiğimiz ArticleForm üzerinden yeni form oluşturuyoruz(önceki yaptığımız gibi miraz alarak)
       -Diğer adımları fonksiyon içinde yorumlarla anlattım oradan detaylı bakabilirsin (def updatedarticle)
       -İşlemler bittikten sonra kontrol ettiğinde eğer makalede resim varsa ve güncelle kısmından girip resmi temizle yaparsan
        django_cleanup sayesinde ordan kalkan resim media klasöründen de kalkmış olacak 
       -ve kontrol edersen de aynı resmi 2 farklı makaleye yüklersen django resmin adını değiştirecek ve kopya hatası vermeyecektir


69- MAKALE SİLME SAYFASI EKLEMEK

    !! adımlar tıpkı güncellemede ki gibi kolay
    
    1) article > urls.py -> pathimizi ekliyoruz "  path('delete/<int:id>/',views.deletearticle,name= 'delete'),    "
    2) article > views.py -> fonksiyonumuzu oluşturuyoruz 
       - silme işlemi çok basit , id ile eşleşen değeri bulup article objesine atadık ve terminalde yaptığımız gibi article.delete() yaptık
       - bu işlemden sonra bir şey kalmıyor resmi zaten django_cleanup otomatik siliyor biz de sadece return redirect ile yönlendirme yapıyoruz
       - normalde name değişkeni vererek yönlendirebilirsin ama bizim dashboard farklı app içinde olduğundan article:dashboard yaptık 
       - yani article uygulamasında ki dashboard name değişkeniyle eşleşen fonksiyonun url adresine yönlendirdik



70- LOGIN REQUIRED (KULLANICI OTURUM KONTROLÜ)
    !! bazı url adresleri sadece kullanıcılar oturum açtıysa girilebilir olması gerekiyor onu da bu dekoratör sayesinde yapıyoruz


    flasktan hatırlarsın orada yapmıştık ve bu blog uygulamasında da navbarda mevcut zaten giriş yap ve çıkış yap gibi butonlar için
    Bunu nerede kullanacağız? ne için yapıyoruz? 
    Mesela şuan programda giriş yapmasak bile articles/addarticles sayfasına yani makale ekleme sayfasına girebiliyoruz 
    tabii ki makale eklemeye çalışırkan hata verecektir (çünkü django makale eklerken giriş yapan kullanıcının adını otomatik yazar olarak alıyordu)
    biz de bu sayfaya girmeyi bu dekoratör ile engelleyeceğiz baya boş yaptım ama temeli hallettik

    !! dokümentasyon: ' login required django' diye aratıp ilk siteye gir ve ctrl+f ile 'login_required' aratıp modülün nasıl kullanıldığını incele

    1) Django tarafından hazır olarak kullanılan dekoratörü ilk olarak dahil ediyoruz
       - article > views.py -> 'from django.contrib.auth.decorators import login_required'
    2) Kullanmak istediğimiz fonksiyonların hemen üzerine dahil ettiğimiz dekoratörü ekliyoruz 
       - dashboard, addarticle, deletearticle, updatearticle -> @login_required
    
    !! aslında kullanımı bu kadar basit fakat bu kullanımda kullanıcı girişi yapılmadıysa ve belirttiğimiz sitelere girerse 404 hatası verecektir
    biz 404 hatası vermesini değil login(giriş) ekranına gitmesini istersek şöyle yapıyoruz

    3) dekoratörün(login_url değerini = 'app:url_name' ile belirtiyoruz ve belirttiğimiz name değişkeninin bağlı olduğu fonksiyonun urlsine yönlendiriyor)
       - @login_required(login_url="user:loginUser")
       - bu sayede eğer giriş yapılmadıysa login ekranına atacak 

71- TEKNİK AKSAKLIKLARI DÜZELTTİM

    -login yapmış bir kullanıcı tekrar login yapabiliyordu user > views.py kısmına yeni bir dekoratör ekledim bu sayede kullanıcı:
     1) login yaptıysa terkar yapamıyor
     2) login yapmadıysa logout yapamıyor
     3) login yaptıysa register yapamıyor
     4) giriş yapmış fakat ona ait olmayan makaleyi silemiyor ve güncelleyemiyor
     (articles > views.py içinde deletearticle ve updatearticle fonksiyonu düzeltildi)
     !! baya bakındım başka yaptığım değişiklik aklıma gelmedi sen incele açık bulursan düzeltirsin 
     -- eklenen 2 dekoratör var (login_required ve userNotLogged) user olanı ben ekledim hata alma ihtimali olabilir(ama düşük)


72- MAKALELER SAYFASI OLUŞTURMAK (yayınlanmış tüm makaleler olucak yani kişiye özel kontrol paneli değil)
    !! makale sayfasını dersde ki gibi aynen yapmadım kafama göre yaptım (ders-231)

    1) article > urls.py -> yeni path oluşturuyoruz ama boş çünkü kök dizin olsun bu sayede makale urlsi -> /articles olacaktır
     -path('',views.articles,name= 'articles'),
    2) article > views.py -> articles fonksiyonumuzu oluşturuyoruz
     -articles = Article.objects.all() -> yaparak tüm makaleleri bir listeye atadık 
     -{'articles':articles} -> yaparak listemizi sözlük içinde html sayfasına gönderdik
    3) articles.html sayfası oluşturduk 
     - ben dashboard da ki tablolardan kopya çektim , derste details.htmlden kopya çekiyordu
     - olay if koşulu ile makale geliyor mu sorgulamak ve geliyorsa for ile alt alta listelemek gelmiyorsa makale eklenmedi diye bastırmak
     
73- CODE SNIPPETS ÖZELLİĞİ EKLEMEK 
    !! kodlarımızı türlerine göre renklendiriyor , örneğin fonksiyon koşul vb. Zaten flaskta yapmıştık aynısını tekrar burada da yapıyoruz
    Yapma sebebimiz makalelerimizde kod paylaşırsak daha güzel gözükmesi ve anlaşılır olması 

    - 'Google code prettify' diye aratmak ve ilk github sitesine girmek
    - Setup ve usage (kurulum ve kullanım) kısımlarını inceleyerek adımlara devam ediyoruz
    - Sitede verdiği scripti layout.html sayfasına koyarsak eğer her sayfaya koymamıza gerek kalmaz çünkü hepsi layout.htmlden extend ediliyor.
    - Kullanım: Verilen kodu layouta ekliyoruz ve makale eklerken kaynak kısmına girip <pre class> etiketini(sitedeki) kullanarak ekliyoruz
      böylelikle pre içine girdiğimiz kodlar diline göre renklendirilecek ve daha anlaşılır olacak
    - JAVA ve PYTHON KODLARINI RENKLENDİRİR 

    - layout.html -> '<script src="https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js"></script>' 
    - makale ekle -> <pre class="prettyprint">  KODLAR ... </pre>
    
74- DJANGO TEMPLATES FILTRELERİ (jinja 2 templates)

    - 'Django template filter' diye aratıyoruz ve ilk django sitemize giriyoruz (Built-in template tags and filters)
    - Kaynağı inceliyoruz , Etiketlerin ve filtrelerin olduğunu görüyoruz 
    !! Örnek kullandığımız etiketler : load, csrf token, include vb.
    !! Örnek kullandığımız filtre : |safe -> filtresini kullandık mesela articles.html sayfasında content için
    - Peki safe filtresi ne işe yarar ne diye kullandık : html içeriklerini olduğu gibi göstermiyor html sayfası olarak göstermeyi sağlıyor

   -  "truncate words" (kelimeleri kısalt). Bu, belirli bir metin parçasının belirli bir uzunluktan sonra kesilerek kısaltılmasını sağlar. 
    Örneğin, bir web sitesinde uzun başlık veya açıklamaların kısaltılması için kullanılabilir. 
    Bu işlem, metni daha okunaklı hale getirir ve gereksiz bilgiyi keser.
    Normalde programda makaleler kısmında kullanmam gerekiyor fakat ben farklı makaleler sayfası yaptım ve bunu ekleyince güzel durmuyor 
    o yüzden programıma eklemiyorum , sen istersen ekleyebilirsin . Nasıl yapılıyor ?

    - Diğer safe filtresi gibi kullanıyoruz jinja template içine |filtre_ismi yapıyoruz
    ! {{ value|truncatewords:2 }} --> metnin ilk 2 kelimesini göster ve sonrasına ... koy (devamı... gibi) 
    ! {{article.content | safe | truncatewords:3}}


    - Biz sonuna sadece ... koymak değil devamını oku özelliği koyacağız ve tıklandığında makalenin devamı gözükecek
      Bunu nasıl yaparız tabiki yönlendirme yaparak oraya bir a etiketi koyup linkini makalenin id'si yaparız ismini devamını oku yaparız olur
      istersek class'ını btn btn-warning yapıp style içine float: right; da yaparsak sağ tarafta durur tıklayınca devamını oku gibi olur
      aynı bizim başlığa koyduğumuz link gibi (o yüzden yapmama bile gerek yok)
    ! <a href="/articles/article/{{article.id}}" style="float: right;" class="btn btn-info"> devamını oku  </a>


75- ARAMA ÇUBUĞU EKLEMEK (articles.html sayfasına)

    !! şimdi derste bu articles.html için devam ediyor ve yaptıklarının üzerine ekliyor ve ben o şekildeyapmadığım için
    aynı kendi yaptığımın üzerine gördüklerimi ilave edeceğim . Zaten mantık aynı makaleler burada görünecek ve arama sonucu
    aradığımız makaleyi getirecek ben de bu işlemi onun gibi veya ona benzer yapacağım

    - Önce flasktaki arama butonu yani formumuzu çekiyoruz , sen uğraşma diye buraya atıyorum 
        <form action="/search" method="POST" style="float: right;" >
        <input type="text" maxlength="64" name="keyword" placeholder="ara">
        <button type="submit" class="btn btn-primary btn-sm">Ara</button>
        </form> #ben form style float değerini right yaptım sağda dursun diye istersen silebilirsin

    !! CSRF TOKEN EKLEMEYİ SAKIN UNUTMA YOKSA FORMUN DJANGODA ÇALIŞMAZ O YÜZDEN FORMUN İÇİNE EKLİYORUZ -> {% csrf_token %}
    
    - Normalde yaptığımız gibi yukarıda formumuz var post işlemiyle yapıyor falan filan fakat şimdi yeni bir şey öğreneceğiz 
      yapacağımız işlem formumuzun get request ile aynı sayfada işlem yapmasını sağlamak o yüzden formumuzdaki action ve post methodunu kaldırıyoruz
      ki zaten sen articles.html sayfasını incelersen formun son halini görebilirsin ama benim anlatmaya çalıştığım o hale gelirken ki adımlar.

    - Get request kullanırken adres çubuğunda gönderdiğimiz veriler gözükeceği için arama için kullanılabilir fakat şifre veya önemli bilgiler 
      içeren durumlarda get request yapmak mantıksız bir hareteket olacaktır , bu dikkat edilmesi gereken bir unsurdur lütfen unutma

    - Artık hazırız şimdi gönderdiğimiz keyword'ü yani yaptığımız get request sonucu url çubuğuna daha doğrusu arama kutusuna gönderilen değeri
      views.py üzerinden işleme alıyoruz

      adımlar : öncelikle siteye yapılan get modununun get fonksiyonu ile gönderilen değeri alıyoruz ve objeye atıyoruz
      ! eğer ki siteye get yapılmış fakat arama çubuğu ile alakası yoksa bunu da şöyle yapıyoruz
      if keyword : # yani objemiz true mu dönüyor false mi bu koşulla kontrol edebiliriz

      article > views.py ->    
    1)  keyword = request.Get.get("keyword")
        if keyword: pass
    
    2) şimdiyse bu atadığımız veriye göre veri tabanında filtreleme işlemi yapmamız gerekiyor . if koşulu içine
        articles = Article.objects.filter(title__contains = keyword) # FİLTER İÇİNDEKİ İŞLEMLER : 
        # title__contains -> başlıkların içinde geçen anlamında kullanılır ve eşitlediğimiz değeri başlıkların içinde arar

        return render(request,'articles.html',{'articles':articles}) -> yaparak işlemimizi bitiriyoruz

76- URL'LERİMİZİ DİNAMİK HALE GETİRME ( TÜM LİNKLERİ DİNAMİK YAPMAK )

    Birkaç kere dinamik url olarak kullandık fakat çoğunluğu statik tek adresli linkler şimdi ise hepsini dinamik hale nasıl getiririz onu göreceğiz

    -Herhangi bir path içinde url değişikliği yaptığımızda onun bağlı olduğu tüm html sayfalarındaki linki de düzeltmemiz gerekiyor
     tabii bu işlemi  büyük programlarda da yapmak  güç istiyor ancak biz bunu engellemek için pathlerdeki name değişkenlerini kullanabiliriz
     bu sayede path'e bağlı link değişse bile o name sayesinde html sayfası yeni linki kullanacaktır 

    - Kısaca: Html sayfalarında yönlendirmek için link kullanırken artık path içindeki name değişkenini vereceğiz
      bu sayede link değişse bile name aynı olacaktır 

    - Kullanımı: "{% 'name' %}" -> name değişkeni ana uygulama içersindeydi direkt çağrılabilir fakaat
      Kullannım 2 : "{% 'app:name' %}" -> name değişkeni sonradan oluşturduğun uygulama(app) içersindeyse de uygulama_ismi:name_ismi olarak kullanılır


      Örnek: <a class="navbar-brand" href="/">Blog Sayfam</a> -> bu önceki navbarda ki ana sayfaya gönderen butondu şimdi aynısını yapıyoruz
      <a class="navbar-brand" href="{% url 'index' %}">Blog Sayfam</a> --> bu da url tag'i ile dinamik olarak değiştirdiğimiz

      Örnek 2 : şimdi farklı app içersindeki name değişkeninin linkini nasıl dinamikleştiririz onu görelim 
      <a class="nav-link" href="/articles">Makaleler</a> --> linkin önceki hali (include olan link bu unutma)
      <a class="nav-link" href="{% url 'article:articles' %}">Makaleler</a> --> bu da makaleler sayfasının dinamik hale gelmiş urlsi


      Eğer ki önceden oluşturduğumuz dinamik url adresini dinamikleştirmek istersek nasıl yaparız ?
    - Kullanımı : "{% url  'myapp:name' myapp.id %}" -> bu sayede aynı linki veriyor ve id ile dinamikleştiriyoruz

      - "{% url  'article:detail' article.id %}" -> bu tag şu anlama geliyor örnek : /articles/article/{{article.id}}
        bu örnekte detail dememiz kafanı karıştırmasın article > urls.py sayfasında makaleyi görüntüleme pathinin name değişken ismi detail'dir
    



    1) İşlemleri tüm urls.py dosyalarında yapacağız -> article, user ve blog_django > urls.py  sayfalarını aç
    2) Yukarıda gösterdiğim gibi önceden oluşturduğumuz hazır linkleri , önceden oluşturduğumuz pathlerin içindeki name değişkeni olarak belirttiğimiz
    değeri belirt ve bu kadar artık linki değiştirsen dahi sitede otomatik olarak değişcektir

    !! Konuyu örneklendirmek gerekirse : Html siteleri artık anahtara değil eve bağlı. Sen farklı anahtarla da girsen ev aynı ev

77- MAKALELELER İÇİN YORUM KISMI EKLEMEK ( COMMENT MODELİ VE COMMENT FORMU )

    1) article > models.py -> yorumlar için yeni model oluşturuyoruz
    2) article > admin.py -> comment modelimizi dahil ediyor ve sonrasında register ediyoruz
       -from .models import Article,Comment
       -admin.site.register(Comment)
    3) modelde ve admin panelinde değişiklik yaptığımız için djangoya bunu söylüyoruz -> 
       - terminal -> python manage.py makemigrations # - Create model Comment
       - terminal -> python manage.py migrate        # - Applying article.0003_comment... OK

       ! şuanda comment tablomuz oluştu admin paneline giderek kontrol edebilirsin(sitede navbarda admin linki var)

    4) şimdi comment formu oluşturup sitemize ekleyeceğiz ve o formun verilerini veritabanındakilerden çekeceğiz
       - templates > includes > posttemplate.html -> bu sayfadaki sadece COMMENT FORM'u alıyoruz (ben aşağıda veriyorum karışmasın uğraşma)

       <div class="card my-4">
                    <h5 class="card-header">Yorum ekle:</h5>
                     <div class="card-body">
                     <form action="{% url 'article:comment' article.id %} method="POST" > " eski hali -> action="/articles/comment/{{article.id}}"
                        {% csrf_token %}
                        <div class="form-group">
                            <label for="formGroupExampleInput">İsminiz</label>
                            <input type="text" class="form-control" id="formGroupExampleInput">
                          </div>
                        <div class="form-group">
                            <label for="formGroupExampleInput">Yorumunuz</label>
                            <textarea class="form-control" rows="3" ></textarea>   
                        </div>
                    </div> <!-- buton kötü duruyorsa bunu alttaki divden sonra kapat -->
                        <button type="submit" class="btn btn-primary">Gönder</button>
                     </form>   
                    </div>

        - formun actionuna baktığın üzere yeni html sayfası, path ve fonksiyon oluşturuyoruz
        - article > urls.py -> path('comment/<int:id>/',views.addcomment,name= 'comment'),
        - article > views.py -> def addcomment oluşturuyoruz(şimdilik pass ile)
        - detail.html -> isim input'unun name değerini veriyoruz -> <input name="comment_author" type="text" ... >
        - detail.html -> yorum input'unun name değerini de veriyoruz -> <textarea name="comment_content" rows="3" ... >
        !! önceki arama işlemimizde get request ile işlem yapmıştık şimdi formumuz post olduğu için post request ile yapacağız
        - article > vies.py -> addcomment fonksiyonunu oluşturuyoruz, adımları detaylı olarak fonksiyon içinde gösterdim
        !! views.py üzerinde işlem yaparken yorum satırlarına dikkat et (reverse ve comment dahil ettik)

    5) Oluşturulan yorumları details sayfasında göstermek
        1) article > views.py -> def detail içersinde işlem yapıyoruz
          models.py dosyasında (related_name = "comments") olarak belirtmiştik şimdi o ilişki sayesinde erişebiliriz
          basit ama işlemler zaten fonksiyon içinde var inceleyebilirsin (veriyi sözlük olarak siteye gönderdik)
        2) details.html -> gönderdiğimiz comments verisini siteye bastırıyoruz
          - if koşulu açıyoruz ve comments true değilse alert mesajı veriyoruz
          - posttemplate.html sayfasından SINGLE COMMENTS kısmını alıp if içersine koyuyoruz ve düzenliyoruz
          - {% if comments %}
                    {% for comment in comments  %}
                    <div class="media mb-4">
                        <div class="flex-shrink-0">
                            <img class="d-flex mr-3 rounded-circle" src="https://dummyimage.com/50x50/ced4da/6c757d.jpg" alt="..." /></div>
                        <div class="ms-3">
                          <!--   <div class="fw-bold"> {{comment.comment_author}} </div> -->
                          <h5>{{comment.comment_author}}  <small class="text-muted">(Gönderilme tarihi: {{comment.comment_date}})</small></h5>
                        <p> {{comment.comment_content}} </p></div></div>
                    {% endfor %}
                    {% else %}
                        <div class="alert alert-warning"> Bu makaleye henüz yorum yapılmadı.</div>
                    {% endif %}
          - bu kısmı çok anlatamadım o yüzden kodu direkt paylaştım unutmazsam incelerim tekrardan adım adım anlatırım 

78- MAKELELER VE YORUMLARI SIRALAMA (ben created_date ve comment_date'e göre en son ekleneni yaptım)

    !! şuan default olarak en önce eklenenler en başta gözüküyor (yorum ve makale)
    - Bunu yapabilmek için ilk önce modellerimizi değiştirmemiz gerekiyor
    1) article > views.py -> modellerimizin içine alt kısıma meta sınıfı ekliyoruz
    2) ' django ordering ' diye aratıp gittiğimiz ilk siteden sıralama ile alakalı dokümentasyonu inceledik
    3) article > views.py -> 
    class Meta:

       makale için:
       yorum için: ordering = ['-comment_date']
    4) modelimizi değiştirdiğimiz için djangoya söylüyoruz : terminal -> python manage.py makemigrations
    5) değişen modellerimizi veritabanına kaydediyoruz : terminal -> python manage.py migrate


    ŞUANDA PROJE BİTTİ BUNDAN SONRA AKLIMA EKLEYECEĞİM BİR ŞEY GELMİYOR GERİSİ SANA KALMIŞ
    İSTER ARAYÜZÜ GÜNCELLE DEĞİŞTİR KARIŞTIR 
    İSTERSEN DE SIFIRDAN BİR PROJEYE BAŞLA VE İSTEDİĞİN GİBİ OLUŞTUR , TAKILDIĞIN YER OLURSA KAYNAĞI İNCELERSİN
    ŞİMDİ GERİYE KALAN TEK ŞEY PROJEYİ DEPLOY ETMEK FAKAT DJANGOYU DEPLOY ETMEK CAN ALICI KISIM
    O YÜZDEN BUNU PROJEYİ BİTİRDİĞİN GÜN YAPMA MUTLAKA MOLA VER HAYDİ BAKALIM LET'S GO
