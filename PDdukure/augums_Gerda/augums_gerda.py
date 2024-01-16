
skolenu_augums = {'skolēna kārtas numurs': [], 'skolēna augums':[]}
skolenu_augums['kartas_numurs'] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
skolenu_augums['augums'] = ['172', '185', '164', '184', '162', '164', '165', '167', '177', '184', '165', '180']
print(skolenu_augums)

while True:
    darbibas = (input('Ko jūs vēlaties darīt? \n 1- pievienot datus \n 2- dzēst noteiktus datus \n 3- iziet \n'))  #Lietotājs var izvēlēties darbību, ko vēlas veikt ar datiem
    atbilde = int(darbibas)

    if atbilde == 1:    #ja lietotājs izvēlas 1, viņš var pievienot datus
        print('Jūs uzspiedāt 1 - pievienot datus!')
        kartas_numurs = input('Ievadi skolēna kārtas numuru: ')
        augums = input('Ievadi skolēna augumu: ')
        skolenu_augums['kartas_numurs'].append(kartas_numurs)
        skolenu_augums['augums'].append(augums)
        print(kartas_numurs,':', augums)
        print('Jauni dati tika pievienoti!')
    
    elif atbilde == 2:   #ja lietotājs izvēlas 2, viņš var izdzēst noteiktus datus
        print('Jūs uzspiedāt 2 - dzēst noteiktus datus!')
        kartas_numurs =(input('Ievadi kārtas numuru: '))
        index = skolenu_augums['kartas_numurs'].index(kartas_numurs)
        skolenu_augums['kartas_numurs'].pop(index) 
        skolenu_augums['augums'].pop(index)
        print('Jūsu izvēlētie dati tika dzēsti')
        print(skolenu_augums['kartas_numurs'], skolenu_augums['augums'])

    elif atbilde == 3:    #Ja lietotājs uzspiež 3, programma beidzas
        print('Jūs uzspiedāt 3, paldies, ka izmantojāt šo programmu! Visu labu!')
        exit()
