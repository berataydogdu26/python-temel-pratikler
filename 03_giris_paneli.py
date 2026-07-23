username =[]
password=[]
while True:
    giris = int(input("""
1-Kayıt ol
2-Giriş yap
3-Çıkış yap
Yapmak istediğiniz işlemi seçiniz: """))

    if giris == 1:
       kullanıcıadı=input("Kullanıcı adını giriniz: ")
       sifre=input("Şifrenizi giriniz: ")
       username.append(kullanıcıadı)
       password.append(sifre)
       print("Kayıt başarıyla oluşturuldu.")
    elif giris == 2:
        klncad = input("Kullanıcı adını giriniz: ")
        sfr = input("Şifrenizi giriniz: ")
        if klncad in username and username.index(klncad) == password.index(sfr):
            print("Giriş başarılı")
        else:
            print("Girdiğiniz bilgiler eşleşmemektedir. Kayıt olunuz veya tekrar deneyiniz.")
    elif giris == 3:
        print("Çıkış yapıldı. İyi günler.")
        break
    else:
        print("Yanlış giriş. Tekrar deneyiniz.")
