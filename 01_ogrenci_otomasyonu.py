ogrenciler = {}


while True:
    print("\n----------------------------------")
    islem = input("""1- Yeni Öğrenci Kaydı
2- Öğrenci Bilgisi Sorgulama
3- Çıkış
Yapmak istediğiniz işlemi seçiniz (1/2/3): """)

    if islem == "1":
        yeninumara = input("Yeni Öğrencinin Numarasını Giriniz: ")
        yeniisim = input("Yeni Öğrencinin Adını Giriniz: ")
        yenisoyad = input("Yeni Öğrencinin Soyadını Giriniz: ")
        yenitelefon = input("Yeni Öğrencinin Telefon Numarasını Giriniz: ")


        ogrenciler[yeninumara] = {
            "Ad": yeniisim,
            "Soyad": yenisoyad,
            "Telefon": yenitelefon
        }
        print(f"\n✅ {yeniisim} {yenisoyad} adlı öğrenci başarıyla eklendi!")


    elif islem == "2":
        ogrencinum = input("Bilgilerini Sorgulamak İstediğiniz Öğrencinin Numarasını Giriniz: ")

        if ogrencinum in ogrenciler:
            print("\n--- Öğrenci Bilgileri ---")
            print(f"Adı: {ogrenciler[ogrencinum]['Ad']}")
            print(f"Soyadı: {ogrenciler[ogrencinum]['Soyad']}")
            print(f"Telefon: {ogrenciler[ogrencinum]['Telefon']}")
        else:
            print("\n❌ Bu Numaraya Kayıtlı Öğrenci Bulunamadı!")

    elif islem == "3":
        print("\nProgramdan çıkılıyor. İyi günler!")
        break  # Döngüyü kırar ve programı sonlandırır.

    else:
        print("\n⚠️ Geçersiz bir seçim yaptınız, lütfen 1, 2 veya 3 giriniz.")
