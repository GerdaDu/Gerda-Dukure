import math
skaits = float(input('Norādiet nepieciešamo pasūtīto podestu skaitu: \n'))
podestaGarums = float(input('Norādiet nepieciešamo podesta garumu(cm): \n'))
podestaPlatums = float(input('Norādiet nepieciešamo podesta platumu(cm): \n'))
podestaAugstums = float(input('Norādiet nepieciešamo podesta augstumu(cm): \n'))
plaksnesBiezums = float(input('Ievadiet nepieciešamo finiera plāksnes biezumu(mm): \n'))
print('\n',skaits,'-podestu skaits \n',podestaGarums,'-podesta garums \n',podestaPlatums,'-podesta platums \n',podestaAugstums,'-podesta augstums \n',plaksnesBiezums,'-plaksnes biezums \n')   #parāda izvadē nepieciešamos ievadītos materiālus

finierisDaudzums =(podestaPlatums*podestaGarums)/(125*250)*6       #aprēķina nepieciešamo finieres daudzumu
if skaits == 2:
    liste = 12
elif skaits == 1:
    liste = 0
else:
    liste = skaits*12
sturis = skaits*8

print('\n',finierisDaudzums,'-finiera plākšņu daudzums \n',liste,'-līstu skaits \n',sturis,'-stūra savienojumu skaits \n')          #parāda izvadē aprēķinātu materiālu daudzumu

if plaksnesBiezums == 4:                   #aprēķina vienas plāksnes cenu 
    plaksnesCena = 45.15
elif plaksnesBiezums == 6.5:
    plaksnesCena = 47.30
elif plaksnesBiezums == 9:
    plaksnesCena = 51.03
elif plaksnesBiezums == 12:
    plaksnesCena = 57.39
elif plaksnesBiezums == 15:
    plaksnesCena = 65.13
elif plaksnesBiezums == 18:
    plaksnesCena = 74.75
elif plaksnesBiezums == 21:
    plaksnesCena = 85.99

cenaFinieris = float(finierisDaudzums*plaksnesCena)          #aprēķina finiera daudzuma kopējo cenu
cenaProfili = liste*0.22                              #līstes cena ir 0.22 euro par vienu
cenaSturis = sturis*4.99                              #stūra cena ir 4.99 euro par vienu

print('\n',round(cenaFinieris,2),'-finiera kopējā cena \n',cenaProfili,'-profilu kopējā cena \n',cenaSturis,'-stūru kopējā cena \n ')  #izvadē parāda materiālu iznākumus
cena = cenaFinieris + cenaProfili + cenaSturis
print('\n Kopējie izdevumi: ',round(cena,2),'euro')       #izvadē parāda kopēko cenu                                  

cenaarpvn = (cena*21)/100+cena
print(round(cenaarpvn,2),'- cena ar pievienotu PVN vērtību')
