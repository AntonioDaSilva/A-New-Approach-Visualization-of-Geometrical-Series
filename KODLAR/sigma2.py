"""07.12.2016
Mert Unsal
Python 3.5 de calistirilmasi gerekmektedir.
2016-2017 Tubitak Projesi icin sigma notasyonlarinin sonuclarinin dogrulugunu
kontrol eden python kodu"""
#Asagidaki fonksiyon r'nin herhangi bir degeri icin (1-r)+(1-r)*r^2+(1-r)*r^4..
#seklinde uzayan sigma notasyonunu hesapliyor.
def sigma2():
    payda=int(input("Oranin paydasini giriniz: "))
    toplam=0
    for sayi in range(1,10000):
        if (1-(-1)**sayi)==0:
            toplam+=0
        else:
            toplam+=((1-(1/payda))*((1/payda)**(sayi-1))*((1-(-1)**sayi)/2))
#sonsuza kadar gidiyorsa uzun uzun basamaklari yazdirmamasi icin gereken kod
    if len(str(toplam))>16:  
        print(str(toplam)[0:16])
    else:
        print(toplam)
while True:
    sigma2()
        
                 
