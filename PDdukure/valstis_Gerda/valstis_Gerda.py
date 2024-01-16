valstis = {'valsts nosaukums': [], 'iedzīvotāju skaits':[]}
valstis['valsts_nosaukums'] = ['Latvija','Lietuva','Igaunija','Francija','Polija','Itālija','Somija','Šveice','Īrija','Zviedrija']    
valstis['iedzivotaju_skaits'] = [1875757,2810118,1329460,65821885,38483957,58983000,5374781,8570700,4857000,10402070]

print(valstis)

print('-----------------------------------------------------------')

print('1 - sakārtot valstis pēc to nosaukumiem augošā secībā')
print('2 - sakārtot valstis pēc to nosaukumiem dilstošā secībā')
print('3 - sakārtot valstis pēc to iedzīvotāju skaita augošā secībā')
print('4 - sakārtot valstis pēc to iedzīvotāju skaita dilstošā secībā')
print('5 - pievienot jaunu valsti un iedzīvotāju skaitu')
print('6 - apskatīt visas valstis')
print('0 - iziet, (Jūs varat jebkurā brīdī ievadīt taustiņu 0, tad programma beigsies)')

while True:
    print('-----------------------------------------------------------')
    darbibas = input('Ko jūs vēlaties darīt?: ')         
    print(darbibas)
    atbilde = int(darbibas)

    if atbilde == 1:                            #ja lietotājs uzspiež taustiņu 1, valstis tiek sakārtotas augošā secībā pēc to nosaukumiem
        print('Jūs uzspiedāt taustiņu 1 - sakārtot valstis pēc to nosaukumiem augošā secībā!')
        print(sorted(valstis['valsts_nosaukums'],key=len))

    elif atbilde == 2:                                    #ja lietotājs uzspiež taustiņu 2, valstis tiek sakārtotas dilstošā secībā pēc to nosaukumiem
        print('Jūs uzspiedāt taustiņu 2 - sakārtot valstis pēc to nosaukumiem dilstošā secībā!')       
        print(sorted(valstis['valsts_nosaukums'],reverse=True,key=len))


    elif atbilde == 3:                        #ja lietotājs uzspiež taustiņu 3, valstis tiek sakārtotas augošā secībā pēc to iedzīvotāju skaita
        print('Jūs uzspiedāt taustiņu 3 - sakārtot valstis pēc to iedzīvotāju skaita augošā secībā!')  
        print(sorted(valstis['iedzivotaju_skaits']))

    elif atbilde == 4:                       #ja lietotājs uzspiež taustiņu 4, valstis tiek sakārtotas dilstošā secībā pēc to iedzīvotāju skaita
        print('Jūs uzspiedāt taustiņu 4 - sakārtot valstis pēc to iedzīvotāju skaita dilstošā secībā!')     
        print(sorted(valstis['iedzivotaju_skaits'],reverse=True))

    elif atbilde == 5:                                     #ja lietotājs uzspiež taustiņu 5, viņam ir iespēja pievienot jaunus datus
        print('Jūs uzspiedāt taustiņu 5 - pievienot jaunu valsti un iedzīvotāju skaitu!')
        valsts_nosaukums = input('Ievadiet valsts nosaukumu: ')
        iedzivotaju_skaits = input('Ievadiet šīs valsts iedzīvotāju skaitu: ')
        valstis['valsts_nosaukums'].append(valsts_nosaukums)                  #pevieno valsts nosaukumu
        valstis['iedzivotaju_skaits'].append(iedzivotaju_skaits)               #pievieno iedzīvotāju skaitu
        print(valsts_nosaukums,':', iedzivotaju_skaits)
        print('Jauni dati tika pievienoti!')
        print(valstis)

    elif atbilde == 6:                                  #ja lietotājs uzspiež taustiņu 6, uz ekrāna tiek izprintēti visi dati
        print('Jūs uzspiedāt taustiņu 6 - apskatīt visas valstis')
        print(valstis)

    elif atbilde == 0:                                 #ja lietotājs uzspiež taustiņu 0, programma beidzas
        print('Jūs uzspiedāt taustiņu 0 - iziet')
        print('Visu labu! ;)')
        exit()
