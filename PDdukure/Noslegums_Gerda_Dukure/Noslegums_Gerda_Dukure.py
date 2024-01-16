from datetime import datetime

now = datetime.now()
time = now.strftime("%H:%M:%S")
date_time = date_time = now.strftime("%m/%d/%Y, %H:%M:%S")      # uzraksta šobrīdējo datumu un laiku.


def iegut_datus():             # funkcija noskaidro eksperimenta nosaukumu, vārdu un eksperimenta veikšanas vietu.
    global eksperimenta_nosaukums       #globalizē mainīgo programmā, kas ļauj tam strādāt ārpus šī def.
    global laiks
    global vards
    global vieta
    eksperimenta_nosaukums = input("Ievadiet eksperimenta nosaukumu!\n")
    laiks = datetime.now()
    vards = input('Ievadiet savu vārdu!\n')
    vieta = input('Ievadiet eksperimenta veikšanas vietu!: \n')
    print('\n')
    print(f'Eksperimenta nosaukums: {eksperimenta_nosaukums}')
    print(f'Eksperimenta veiksanas laiks: {date_time}')
    print(f'Jūsu vārds: {vards}')
    print(f'Eksperimenta veikšanas vieta: {vieta}',)


dati = ['eksperimenta_nosaukums', 'laiks', 'vards', 'vieta']

try:
    def saglabat_datus():                               #pievieno un saglabā jaunus datus.
        
        with open('eksperimenta_dati.txt', 'a', encoding = 'UTF = 8', newline= '') as f:
            f.writelines(f'Eksperimenta nosaukums: {eksperimenta_nosaukums}, ')
            f.writelines(f'Eksperimenta veiksanas laiks: {date_time}, ')
            f.writelines(f'Jūsu vārds: {vards}, ')
            f.writelines(f'Eksperimenta veikšanas vieta: {vieta}, ')
            f.close()
except FileNotFoundError:
    print(f"Kļūda: Fails '{'eksperimenta_dati.txt'}' nav atrasts. ")
except Exception as e:
    print(f'Kļūda: meparedzēta kļūda - {e}')


def galvena():                   #izprintē sasveicināšanos un izsauc def iegut_datus() un saglabat_datus()
    print('---PROGRAMMA EKSPERIMENTU PIERAKSTIEM!---','\n', '---Sveicināti mūsu programmā!---' )
    iegut_datus()
    saglabat_datus()
galvena()

#palaižot programmu vēlreiz, nedzēšot ārā txt failu, jaunie dati pievienosies klāt esošajiem.


