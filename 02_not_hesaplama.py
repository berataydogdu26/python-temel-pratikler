vize1= int(input("İlk vize notunu giriniz: "))
vize2= int(input("İkinci vize notunu giriniz: "))
final = int(input("final notunu giriniz: "))

vizesonuc = (vize1 + vize2) / 2
vizeyuzde =vizesonuc * 60 / 100
finalyuzde = final * 40 / 100
sonuc = vizeyuzde + finalyuzde

if sonuc >= 50:
    print(f"Tebrikler! Sınav notunuz {sonuc}. Bu dersi başarıyla geçtiniz.")
else:
    print(f"Üzgünüm! Sınav notunuz {sonuc}. Dersi geçemediniz.")
