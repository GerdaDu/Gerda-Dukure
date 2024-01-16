import math

print('Faktoriāla aprēķināšana')
zvaigznites = 50
print(('*')*zvaigznites)

while True:
    skaitla_ievade = int(input('Ievadiet pozitīvu veselu skaitli(mazāku par 13): \n'))

    if skaitla_ievade <= 13:             #ja skaitlis ir mazāks par 13, tad tiks aprēķināts faktoriāls
        faktorials = math.factorial(skaitla_ievade)
        print('Faktoriāls:', faktorials)

    elif skaitla_ievade >13:             #ja skaitlis ir lielāks par 13, tad netiks aprēķināts skaitļa faktoriāls
        print('Ievadītais skaitlis ir pārāk liels!')
        
    turpinasana =input('Vai vēlaties turpināt darbu?(j-jā, viti taustiņi-nē) \n')
    if turpinasana == 'j':           #ja lietotājs uzspiedīs taustiņu j, programma turpināsies
        print('\n')
        continue

    else:                            #ja lietotājs uzspiedīs citu taustiņu izņemot j, programma beigsies
        print('Paldies!')
        exit()

