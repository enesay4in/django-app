from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from .models import Article,Comment

from django.contrib import messages

from django.contrib.auth.decorators import login_required
# Create your views here.


def articles(request):

    keyword = request.GET.get("keyword")
    # request.hangi_method.fonksiyon_adı("name_değişkeni") -> ilk get yapılan method ve ikinci get onu al yani getir anlamında
    if keyword:
        articles = Article.objects.filter(title__contains = keyword) # FİLTER İÇİNDEKİ İŞLEMLER : 
        # title__contains -> başlıkların içinde geçen anlamında kullanılır ve eşitlediğimiz değeri başlıkların içinde arar
        # yani ille öyle başlamasına gerek yok içinde geçmesi yeterli , güzel arama çeşididir

        return render(request,'articles.html',{'articles':articles}) #if koşula girerse siteyi renderla ve sadece aranılan değeri göster

    articles = Article.objects.all()# if değerine girmezse veritabanındaki tüm değerleri al ve ata
    
    return render(request,'articles.html',{'articles':articles})# atanmış tüm makaleleri ekranda göster (makaleler sitesi aramasız)





def index(request):

    context= {
            "numbers" : [1,2,3,4,5,6,7,8,9],
            }

    return render(request,"index.html")# (,context)


def about(request):

    return render(request,"about.html")

@login_required(login_url="user:loginUser")
def dashboard(request):
    """
    ilk önce models.py dosyasındaki Article sınıfını dahil ediyoruz(makale oluşturma modelimiz)
    bunu dahil etme sebebimiz bu model üzerinden veritabanına eklenen öğelere objects.all veya filter ile erişebiliyoruz
    """
    # shell kısmında yaptığımız gibi veritabanından veri gösterme yapacağız ve filter kullanarak giriş yapan kullanıcıya ait olanları seçeceğiz

    articles = Article.objects.filter(author = request.user) #kullanıcıya ait makaleleri aldık ve articles objesine atadık
    # değerlerimiz liste içinde sözlük yapısıyla objeye atanıyor biz de bu sözlüğe erişerek sitede gösterebiliriz

    #articles'i direkt gönderebiliriz fakat daha güzel görünmesi ve daha kullanışlı olması için sözlüğe atayıp key ile erişmek için böyle gönderiyoruz

    context = {
        "articles": articles
    }

    return render(request, 'dashboard.html',context)


@login_required(login_url="user:loginUser")
def addarticle(request):

    form = ArticleForm(request.POST or None,request.FILES or None)#sayfaya gönderilen post request ise --> if method.request == "POST": 

    if form.is_valid():#şartlandırmalar doğruysa
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        #form.save() sadece yapsaydık author hatası alacaktık(hem kendi verecekti hem otomatik artırımlı olduğundan hata alacaktık)
        #commit=false yaparak formu sen oluştur save işlemini ben yapıcam dedik ve author atadıktan sonra kaydettik

        messages.success(request,'Makale başarıyla eklendi.')
        return redirect("article:dashboard") # return redirect("app:url_name")
        #şu uygulamanın altında ki şu url'ye git dedik (başka uygulamadaki name değeri ile eşleşen fonksiyona yönlendirmek böyle yapılıyor)


    return render(request, 'addarticle.html',{"form":form})




#bu basit işlem gözden kaçabilir o yüzden belirtiyorum 
"""
eğer ki belirteceğin html dosyası ana dizin içersinde ki herhangi bir klasörün içersindeyse 
direkt html dosyasını belirtmeden önce klasörü belirtmeyi unutma
    örnek 1) templates klasörünün içindeki index.html için yönlendirme yapıyorsak
        return render(request,"index.html")
    örnek 2) templates klasörünün içindeki article klasörünün içindeki index.html için yönlendirme yapıyorsak
        return render(request,"article/index.html") 

""" 

def detail(request,id):

    #article = Article.objects.filter(id = id).first() #gelen İLK id ye ait veriyi getiriyor(first yapmazsak filter liste döner)
    #burayı get_object_or_404 ile değiştiriyoruz o yüzden silmiyorum yorum bırakıyorum

    article = get_object_or_404(Article,id = id)
    #bu sayede olmayan makaleyi görüntülemeye çalışınca 404 hatası verecektir (şuanda page not founded veriyor çünkü debug=True,normal sitede bunu vermeyecektir)
    

    comments = article.comments.all()#article'ın ilişkili olduğu(yani related_name="comments" yapmıştık) commentslerin hepsini al

    context = {
        "article": article,
        "comments": comments
    }

    return render(request,"detail.html",context)



@login_required(login_url="user:loginUser")
def updatearticle(request,id):



    article = get_object_or_404(Article,id = id)
    #önceden yaptığımız gibi eşleşen varsa objeye at yoksa 404 hatası ver dedik 

    #posttan gelen bilgiler varsa formu doldur veya boş bırak diyoruz(artık dosyadan gelenler varsa da dahil olucak)

    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    # instance parametresinin içine gönderdiğimiz objemiz buradaki formun içine yazılacak 

    if(article.author!= request.user):
        messages.warning(request,"Sadece kendize ait makaleleri güncelleyebilirsiniz.")
        return redirect('article:dashboard')
    if form.is_valid(): # bu kısım addarticle ile aynı olduğundan oradan kopyalayıp yapıştırdık
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        #form.save() sadece yapsaydık author hatası alacaktık(hem kendi verecekti hem otomatik artırımlı olduğundan hata alacaktık)
        #commit=false yaparak formu sen oluştur save işlemini ben yapıcam dedik ve author atadıktan sonra kaydettik

        messages.success(request,f'{id} Numaralı makale güncellendi.')
        return redirect("article:dashboard") # return redirect("app:url_name")
        #şu uygulamanın altında ki şu url'ye git dedik (başka uygulamadaki name değeri ile eşleşen fonksiyona yönlendirmek böyle yapılıyor)




    """
    bizim instance içine gönderdiğimiz article objesi yukarıdaki oluşturduğumuz ve o da id ile eşleşen veriler demek 
    yaniii form düzenleme işlemi yapacağız o yüzden eski formun aynısını getiriyor ve onun üstünde işlem yapıyoruz 
    biraz karmaşık anlattım şöyle söylim bunu yapmazsak form boş gelir ve ne yazarsak eski formun üzerine o kaydedilirdi 
    sadece 1 harf bile değiştirmek istesen dahi tüm formu tekrar yazman veya düzenlemeden önce kopyalamayla uğraşman gerekiyordu
    """


    # formumuz is_valid ise çalışır değilse siteyi tekrar render eder ve formumuzu göndeririz
    return render(request,"update.html",{"form":form})



@login_required(login_url="user:loginUser")
def deletearticle (request,id):

    article = get_object_or_404(Article,id = id)#Dahil ettiğimiz Article Modelininde belirttiğim id ile eşleşen var mı ara ve article objesine ata


    if article.author.id == request.user.id: #giriş yapan kullanıcı ile makale sahibi kullanıcı id aynı ise
        article.delete() #sil
        messages.success(request,f'{id} Numaralı makale silindi.')
        return redirect("article:dashboard")
    else:#değilse
        messages.warning(request,"Sadece kendinize ait makaleleri silebilirsiniz.")#hata mesajı yayınla ve yönlendir
        return redirect("article:dashboard")




    """
    article.delete()
    
    messages.success(request,f'{id} Numaralı makale silindi.')

    return redirect("article:dashboard") # return redirect("app:url_name")
    #şu uygulamanın altında ki şu url'ye git dedik (başka uygulamadaki name değeri ile eşleşen fonksiyona yönlendirmek böyle yapılıyor)
    """

def addcomment(request,id):
    #öncelikle post değerinden gelen yorumu o article için ekleyeceğimiz için
    article = get_object_or_404(Article,id = id)# posttan gelen değeri aldık yoksa 404 hatasını bastırdık

    if request.method == "POST": #yapılan request post ise içeri gir

        comment_author = request.POST.get("comment_author")#yapılan post requestin içindeki name değeri 'comment_author' olanı al ve objeye ata
        comment_content = request.POST.get("comment_content")#aynı atama işlemini content objesi için de yap
        #comment_date otomatik olarak doldulacak o yüzden onu yazmıyorum

        #article foreign key içinse şöyle yapacağız öncelikle Modelimizi dahil edelim -> from .models import Comment 
        #sonra o sınıf için obje oluşturalım

        newComment = Comment(comment_author = comment_author, comment_content = comment_content)
        newComment.article = article #oluşturduğumuz objenin article değerinide yukarıda aldığımız article değeriyle eşitledik
        """
        bu newComment'in article değerini anlamadıysan models.py içindeki id değerimiz altta veriyorum 
        article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Yorumun Gönderildiği Makale", related_name="comments")
        işte o değeride yukarda aldığımız değere atadık biraz karışık oldu istersen yapay zekaya sor adım adım anlatsın bundan daha iyi oturur
        """ 
        newComment.save()# Comment tablosuna yani modeline commentimizi ekliyoruz
        #bu kısma redirect eklemiyorum çünkü hertürlü bu sayfaya göndereceğimiz için birtane redirect yeterli olacaktır

        messages.success(request,'Yorumunuz gönderildi.')

        
    """
    return redirect("/articles/article/" + str(id))  -> böyle de oluyor fakat daha işlevsel yapmak için şöyle yapabiliriz
    dinamik bir url'yi riderect yani yönlendirme yapacaksak REVERSE fonksiyonunu kullanmamaız gerekiyor ve onu da ilk önce dahil ediyoruz
        1) from django.shortcuts import reverse
        2) reverse yönlendirmesi yapıyoruz ve yönlendir yapacağımız path dinamik url ise kwargs içinde sözlükle onu gönderiyoruz
    """

    return redirect(reverse("article:detail",kwargs={"id":id})) # yukarıdaki yoruma aldığım redirect'in daha işlevsel hali




