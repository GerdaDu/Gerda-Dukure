skaits = int(input('Ievadi pasažieru skaitu!: '))
laiks = int(input('Ievadi pulksteņa laiku veselos skaitļos!: ', (22/23/24/1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21)))

if skaits < 4 :                            #ja pasažieru skaits būs mazāks par 4, tiks izdots nākamais jautājums
    print(laiks)
elif skaits > 0 :                          #ja pasažieru skaits >0, tiks izdots nākamais jautājums
    print(laiks)
else:
    print('Ievadi  pareizus datus! ')
    exit()

if laiks == 22:
    print(0,67)      #uz km
elif laiks == 23:
    print(0,67)      #uz km
elif laiks == 24:
    print(0,67)      #uz km
elif laiks == 1:
    print(0,67)      #uz km
elif laiks == 2:
    print(0,67)      #uz km
elif laiks == 3:
    print(0,67)      #uz km
elif laiks == 4:
    print(0,67)      #uz km
elif laiks == 5:
    print(0,67)      #uz km

elif laiks== 6: 
    print(0,57)      #uz km
elif laiks== 7:
    print(0,57)
elif laiks== 7:
    print(0,57)
elif laiks== 8:
    print(0,57)
elif laiks== 9:
    print(0,57)
elif laiks== 10:
    print(0,57)
elif laiks== 11:
    print(0,57)
elif laiks== 12:
    print(0,57)
elif laiks== 13:
    print(0,57)
elif laiks== 14:
    print(0,57)
elif laiks== 15:
    print(0,57)
elif laiks== 16:
    print(0,57)
elif laiks== 17:
    print(0,57)
elif laiks== 18:
    print(0,57)
elif laiks== 19:
    print(0,57)
elif laiks== 20:
    print(0,57)
elif laiks== 21:
    print(0,57)
else:
    print('Ievadi pareizus datus')

noligsana = input('vai kāds taksometrs ir stāvvietā pie dzelzsceļa stacijas?'('j/n'))    
if noligsana == 'j':
    print(+1,25)
elif noligsana == 'n':
    print(1,25 + 2,20)
else:
    exit()
gaidisana=int(input('Ievadiet gaidīšanas laiku'))
if gaidisana == 1:
    print(+0,13)
elif gaidisana >1:
    print(gaidisana * 0,13)                                                         #Ja gaidīšana ietver sevī vairāk nekā 1 min, tad sareizinās cena 
else:
    exit()
attalums=input('Ievadiet nepieciešamo braukšanas attālumu līdz objektam')
print(attalums*0,57)                                                                #attālumam būtu jāsareizinās ar tarifu par vienu kilometru




