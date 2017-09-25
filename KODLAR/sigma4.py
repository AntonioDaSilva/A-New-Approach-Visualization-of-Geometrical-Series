def sigma4():
    us,limit,toplam=2,10000,0
    while us<limit:
        toplam += 1/(2**(us))
        us+=2
    print(toplam)
    
sigma4()



