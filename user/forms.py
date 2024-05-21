from typing import Any
from django import forms #form oluşturmak için djangonun kendi modülünü import ediyoruz(bu sınıf üzerinden oluşturacağız)



class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label= "Username")#username alanı oluşturuldu ve max length ile uzunluk belirtildi
    password =  forms.CharField(max_length=20, label= "Parola",widget=forms.PasswordInput)

    #burada formu oluşturuyoruz sonra html sayfasına gidip {{form.as_p}} yapıyoruz ama html bunu nasıl anlıyor diye düşünme olay bu ikisinde değil
    # forms-html-views-urls olay böyle dönüyor sen /x sayfasına gidince ona bağlı fonksiyon çalışıyor o fonksiyona ait döküman dönüyor ve formu çekiyor


class RegisterForm(forms.Form): #Kayıt formu açıp forms sınıfdan  türetildi.

    username = forms.CharField(max_length=30, label= "Username")#username alanı oluşturuldu ve max length ile uzunluk belirtildi
    password =  forms.CharField(max_length=20, label= "Parola",widget=forms.PasswordInput)#Parolayı gizli olarak almak için widget kullandık.
    confirm = forms.CharField(max_length=20, label= "Parola Doğrula",widget=forms.PasswordInput)

    #password ve confirm'i eşleştirmek için 'clean' fonksiyonunu kullanacağız . 
    #Djangoda forms içindedir dahil edilince gelir  fakat biz şimdi onu override(geçersiz kılma) edip kendimiz oluşturacağız,düzenleyeceğiz

    def clean(self) :

        # ilk önce oluşturduğumuz inputlara girilen değerleri alıyoruz ve onları objelere atıyoruz

        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get( "password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm: #girilen parola ve doğrulama birbirine eşit değilse demek

            raise  forms.ValidationError("Parolalar uyuşmuyor")# raise ile hata fırlattık
        
        #eğer uyuşuyorsa sözlük olarak belirtip yönlendirme yapmamız gerekiyor yani submit işlemini
        values = {
            "username" : username, #virgül unutma
            "password" : password,
            "confirm":   confirm
            
        }
        return values # bunu yapma sebebimiz user > views.py dosyası üzerinden bu verilere erişim sağlayabilmek
        "https://docs.djangoproject.com/en/5.0/ref/forms/api/" #bu siteden dokümentasyona bakabilirsin