def toplam():
    toplam = 0
    i=1
    while i<100:
        f=2**i
        toplam += (1/f)
        i+=1

    return toplam

print (toplam())
