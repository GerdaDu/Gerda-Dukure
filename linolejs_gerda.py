print('-----Linolejs tiek iegādāts no E-GRIDAS-----')
print('---------Linoleja ražotājs: TARKETT---------')

linoleja_cena = float(input('Ievadi linoleja cenu kvadrātmetrā!: '))
rulla_platums = float(input('Ievadi ruļļa platumu metros!: '))
telpas_platums = float(input('Ievadi telpas platumu!: '))
telpas_garums = float(input('Ievadi telpas garumu!: '))

print('-----------------------------------------')

telpas_platiba = telpas_platums * telpas_garums
print('Telpas platība ir: ', telpas_platiba, 'm2')

linoleja_daudzums = telpas_platiba / rulla_platums           #aprēķina nepieciešamo linoleja daudzumu (m)

apaksklajs = input('Vai jūs vēlaties ieklāt apakšklāju? (ja/ne)')

print('-----------------------------------------')

if apaksklajs == 'ja':                                                     #Ja lietotājs ievada atbildi jā, tad viņam tiek pasniegtas izmaksas par linoleju un apakšklāju
    apaksklajacen = float(input('Ievadiet apakšklāja cenu!: '))

    print('-----------------------------------------')

    apaksklaja_cena = linoleja_daudzums * apaksklajacen                     #aprēķina apakšķlāja cenu
    apaksklaja_daudzums = linoleja_daudzums                                  #apakšklāja daudzums ir vienāds ar apakšklāja cenu
    linoleja_cena2 = linoleja_daudzums * linoleja_cena                       #aprēķina linoleja cenu
    print('Linoleja cena=', round(linoleja_cena2,2))
    print('Apakšklāja cena=', round(apaksklaja_cena,2))
    print('Nepieciešamais linoleja daudzums = ', round(linoleja_daudzums,2) , 'm2')
    print('Nepieciešamais apakšklāja daudzums = ', round(linoleja_daudzums,2) , 'm2')
    izmaksas = linoleja_daudzums * round(linoleja_cena,2) + apaksklaja_cena                            #aprēķina izmaksas par linoleju un apakšklāju (euro)
    print('Izmaksas par linoleju un apakšklāju =', round(izmaksas,2), 'euro') 

    print('-----------------------------------------')

    print('Paldies, ka izmantojāt mūsu pakalpojumus! ;)')

    print('-----------------------------------------')

    print('-----Linolejs tiek iegādāts no E-GRIDAS-----')
    print('---------Linoleja ražotājs: TARKETT---------')

elif apaksklajs == 'ne':                                                     #Ja lietotājs ievada atbildi nē, tad viņam tiek pasniegta tikai cena par linoleju
    print('Nepieciešamais linoleja daudzums = ', round(linoleja_daudzums,2) , 'm2')
    izmaksas = linoleja_daudzums * linoleja_cena                            #aprēķina izmaksas par linoleju (euro)
    print('Izmaksas par linoleju =', round(izmaksas,2), 'euro') 

    print('-----------------------------------------')

    print('Paldies, ka izmantojāt mūsu pakalpojumus! ;)')

    print('-----Linolejs tiek iegādāts no E-GRIDAS-----')
    print('---------Linoleja ražotājs: TARKETT---------')
#dddddddddddddddddddddddddddddddvfbfgvfbhbhbhbhbhbhbhbhbhbhbhbhbhbhbhbhbh


