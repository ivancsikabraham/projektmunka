hanysor = int(input("Hány sor kell? "))

karakter = 1
sor = 1
while sor <= hanysor :
    oszlop = 1
    while oszlop <= karakter :
        print('O ', end='')
        oszlop += 1
    print('')
    if hanysor % 2 == 1 :
        if sor < int(hanysor / 2 + 1 ) :
            karakter += 1
        else:
            karakter -= 1
    elif hanysor % 2 == 0 :
        if sor < int(hanysor / 2 ) :
            karakter += 1
        elif sor == int(hanysor / 2 ) :
            karakter = karakter
        else:
            karakter = karakter - 1
    sor += 1
    