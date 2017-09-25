"""07.12.2016
Python 3.5 de calistirilmasi gerekmektedir.
2016-2017 Tubitak Projesi icin sigma notasyonlarinin sonuclarinin dogrulugunu
kontrol eden python kodu"""
#Asagidaki fonksiyon r nin herhangi bir degeri icin S=(r-r^2)+(r^3-r^4)+.... seklinde
#uzayan sigma notasyonunu hesapliyor.
def sigma1():
    payda=int(input("Oranin paydasini giriniz: "))
    toplam,sayi=0,10000
    while sayi>=1:
        pay1=(-1)**(sayi+1)
        payda1=payda**sayi
        kesir=pay1/payda1
        toplam+=kesir
        sayi-=1
#sonsuza kadar gidiyorsa uzun uzun basamaklari yazdirmamasi icin gereken kod
    if len(str(toplam))>16:  
        print(str(toplam)[0:16])
    else:
        print(toplam)
while True:
    sigma1()
    
