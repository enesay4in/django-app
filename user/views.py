from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm

from django.contrib.auth.models import User #Kullanıcı modeli
from django.contrib.auth import login,authenticate,logout #oluşturulan user'i aynı zamanda login yapmak için kullanılan model

from django.contrib import messages

from django.contrib.auth.decorators import login_required
# Create your views here.



# FAZLADAN EKLEDİĞİM DENEME DEKORATÖRÜM
def userNotLogged(func):
    def _func(request, *args, **kwargs):
        # eğer bir kullanıcımız giriş yapmış ise
        if request.user.is_authenticated:
            # Anasayfaya yönlendiriyoruz
            messages.warning(request,f"Hazırda girişiniz bulunuyor ({request.user.username})")
            return redirect('index')
        #giris yapmamışsa fonksiyonu olduğu gibi dönderiyoruz ve sayfaya erişiyor
        return func(request, *args, **kwargs)
    return _func


@userNotLogged
def register(request):

    form = RegisterForm(request.POST or None) #ÇOK KRAL BİR KOD SATIRIDIR ŞU DEMEK : 
    # EĞER REQUEST POST İSE VEYA BOŞ İSE YANİ GET BU DA DEMEK OLUYOR Kİ DJANGO DA REQUEST'İ  IF İLE KONTROL ETMEYE GEREK KALMIYOR
    if form.is_valid():
    #is valid true
        username = form.cleaned_data.get('username')# clean fonksiyonundaki hangi anahtar kelimeyle belirttiysen onu çağırırsın
        password = form.cleaned_data.get('password')

        newUser = User(username = username)#kullanıcı oluşturup kullanıcı_adını formdaki kullanıcı adı yaptık
        newUser.set_password(password)#oluşturduğumuz kullanıcının şifresini atadık ama böyle yaptığımız için şifrelendi -> ****** 

        newUser.save() #oluşturduğumuz kullanıcıyı kaydettik

        login(request,newUser) #bu kod sayesinde oluşturulan kullanıcı aynı zamanda siteye login de oluyor (sadece import et ve burada çağır)

        messages.info(request,"Başarıyla kayıt oldun")

        return redirect("index")
    
    #is valid false veya get request olduğunda ( İŞTE KIRILGAN NOKTA BURASI) EĞER BURAYI ANLARSAN SİSTEMİ ÇÖZERSİN
    context = {
            "form": form
        }

    return render(request,"register.html",context)#girilen parolalar eşleşmezse
    
    #BASİT HALİNİ ANLATIYORUM
    """
    sayfaya post request olduğunda register form dolacak ve bu sayede form.is_valid() kontrol edilecek ve koşula girip girmediğine bakılacak
        eğer valid doğruysa yani parolalar eşleşiyorsa: yeni kullanıcı ve parolası oluşturulacak (**** parola şifrelenmiş olarak)
        ve kullanıcı kaydedilip siteye login edilecek sonrada anasayfaya yönlendirilecek
        eğer valid hatalıysa yani parolalar eşleşmiyorsa:
    sayfa get request olduğunda form boş olucak bu da demek oluyor ki içerik olmadığından form.is_valid() false olacak ve girmeyecek
        girmediği için context oluşturulup sayfa tekrardan render edilecek ve context gönderilecek  
    
    
    """




    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')# clean fonksiyonundaki hangi anahtar kelimeyle belirttiysen onu çağırırsın
            password = form.cleaned_data.get('password')

            newUser = User(username = username)#kullanıcı oluşturup kullanıcı_adını formdaki kullanıcı adı yaptık
            newUser.set_password(password)#oluşturduğumuz kullanıcının şifresini atadık ama böyle yaptığımız için şifrelendi -> ****** 

            newUser.save() #oluşturduğumuz kullanıcıyı kaydettik

            login(request,newUser) #bu kod sayesinde oluşturulan kullanıcı aynı zamanda siteye login de oluyor (sadece import et ve burada çağır)

            return redirect("index")
        #BU ALTTA Kİ KISIM İSE EĞER FORMUMUZ VALID DEĞİLSE YAPILACAK İŞLEMLER
        context = {
            "form": form
        }

        return render(request,"register.html",context)#girilen parolalar eşleşmezse
    else:
        form = RegisterForm() #get request olduğunda form boş olucak o yüzden boş oluşturuyoruz

        context = {
            "form": form
        }

        return render(request,"register.html",context)
    """
    # DEF REGISTER İÇİN ANLATIM
    """
    if request.method == 'POST': -> gelen request 'post' ise içeri gir
        !! POST request olduğunda posttan gelen bilgilerle formu dolduracağımız için form oluştururken verileri atama yapıyoruz
        !! if form.is_valid():  -> bu kısım bizim def clean için çalışması gereken kısımdır , djangoda otomatik değil biz bu koşul ile çağırırız
        unutma sadece is_valid() yapıldığında kontrol yapar aksi halde yapmaz
        if form.is_valid(): True dönerse girilen değerleri döndürür (return values yapar)
        if form.is_valid(): False dönerse raise ile hata fırlatılır (parola ve confirm eşleşmezse)

        artık username ve password alanını alabiliriz bunu da form.cleaned_data.get("username") ile alabiliriz (password de yap)
    else:                         -> gelen request 'get' ise içeri gir
        form oluşturduk, context oluşturup form anahtar kelimesini atadık ve context'i render ile siteye gönderdik(register.html sayfasında kullanılabilir)
    
        
    # User modelinden bir obje oluşturmamız ve sonradan bu objeyi kaydetmemiz gerekiyor
    -from django.contrib.auth.models import User ile modeli dahil ettik
    -Shell kısmında gördüklerini hatırla o işlemleri yapıyoruz(veritabanına kayıt edicez)
        yeni kullanıcı oluştur ve kullanıcı_adını formdaki username olarak ata
        yeni kullanıcıya parola oluştur ama set_password ile parolayı şifreleyerek oluştur -> ******
        oluşturduğun kullanıcıyı veritabanına kaydet(tıpkı commit gibi) data.save()

    #KAYIT EDİLEN KULLANICI AYNI ZAMANDA LOGIN DE OLSUN ISTERSEK django modülü kullanarak nasıl yaparız?
    -from django.contrib.auth import login ile dahil ettik
    - login(request,kullanıcının_ismi) ile çağırdık ve oldu unutma kullanımı basit ama ilk parametre request olmak zorunda!

    #İŞLEMLER BİTTİKTEN SONRA NASIL YÖNLENDİRME YAPARIM?
    -from django.shortcuts import redirect ile 'redirect' methodunu dahil ediyoruz
    - urls.py sayfasında oluşturduğumuz pathlerin name='' parametlerini atamıştık örneğin kök dizin için name='index' yapmıştık
        redirect yaparken de yapcağımız sayfaya bu name değişkenini atarsak o değişkenin bağlı olduğu adrese yönlendirecektir

        
    EN BAŞTAN BASİT BİR ŞEKİLDE ÖZETLEYELİM
    - methodumuzun post olup olmadığını sorguladık
        eğer post ise:
            - formumuzu form.post'dan gelen bilgilerle doldurduk (girilen)
            - form.is_valid() kullanarak parolalar eşleşiyor mu diye kontrol ettik
                eğer doğruysa:
                    yeni kullanıcı oluşturup kullanıcı adı = username ve parola = password ve şifrelenmiş olarak oluşturduk
                    kaydettik ve oluşturduğumuz kullanıcının giriş yapması için otomatik olarak login yaptırdık
                    sonra ana sayfaya gönderdik
                eğer yanlışsa:
                    formumuz eşleşmediği için aynı sayfayı render alıyoruz(post request olsa bile)
                    context oluşturup aynı sayfayı render edip sayfaya aynı bilgiyi verdik bu sayede aynı sayfaya dönüş olduk
        eğer get ise:
            - formumuzu boş oluşturuyoruz
            - formumuzu register.html'e gönderiyoruz

    BU ANLATTIKLARIM YORUM SATIRINA ALINAN KODLAR İÇİN GEÇERLİYDİ (ÖNCEDEN ÖĞRENDİĞİMİZ ŞEKİLDE YAPTIK ÇÜNKÜ)
        
    """



    # SADECE GET REQUEST YAPILINCA BUNU YAZIYORDUK ŞİMDİ ÜSTTE GET VE POST YAPICAZ
    """
    form = RegisterForm()
    context = {
        "form" : form #birden fazlaysa virgül
    }
    return render(request, 'register.html',context) """



@userNotLogged
def loginUser(request):

    form = LoginForm(request.POST or None) # Login formu dahil etmeyi unutma

    context = {
        "form" : form
    }

    if form.is_valid():#eğer form is_valid ise içeri gir değilse bloğa girme
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        #burada clean yapmama sebebimiz zaten forms'un içindeki kendi tanımlandığı gibi çalışır , override etmediğimiz müddettçe

        user = authenticate(username=username, password=password) #username ve password değerlerine göre veritabanında kullanıcı var mı kontol edecek yoksa none döner
    
        if user is None:#eğer user uymuyorsa içeri gir değilse bloğa girme
            messages.info(request,'Kullanıcı adı veya Parola hatalı')
            return render(request,"login.html",context)
        
        #user uyuyorsa devam et
        messages.success(request,f"Başarıyla giriş yapıldı ({user})") # print(f{}) ile veriyi bastırabiliyorduk -> 1.yol
        login(request,user)
        return redirect('index')#işlemler bittikten sonra yönlendirme yaptık



    return render(request, 'login.html',context)


@login_required(login_url='user:loginUser')
def logoutUser(request):
    isim = request.user.username # kullanıcı adını çıkış yaparken bastıracağım -> 2.yol
    messages.info(request,f'Başarıyla çıkış yapıldı ({isim})')
    logout(request)
    
    return redirect ('index')



