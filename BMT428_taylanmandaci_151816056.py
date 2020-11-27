import random


rasgeleSayi=random.randint(1, 100)
def sayiuret():
  return rasgeleSayi

def esitmi(sayi):
    
    if sayi==sayiuret():
        print("Doğru Tahmin Ettiniz")
        return 1
    elif sayi<sayiuret():
        print("YUKARI")
        return 0
    elif sayi>sayiuret():
        print("ASAGI")
        return 0
    else:
        print("esit değil")
        return 0
    

sayiuret() 
sayac=0
tahmin=int(input("Değer gir:"))
kontrol=esitmi(tahmin)
sayac=sayac+1
print(kontrol,tahmin)
if kontrol==1:
    print("doğru tahmin")
while tahmin!=-1:
    tahmin=int(input("Değer gir:"))
    sayac=sayac+1
    kontrol=esitmi(tahmin)
    if kontrol==1:
        break
    else:
        continue
print("Adım Sayısı:",sayac)
    






