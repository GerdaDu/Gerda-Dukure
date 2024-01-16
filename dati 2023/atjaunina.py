import csv

sakotnejie_dati_fails = 'sakotnejie_dati.csv'
jaunie_dati_fails = 'jaunie_dati.csv'

#mēģina atvērt sākotnējo failu un lasa datus
try:
    with open(sakotnejie_dati_fails, 'r', encoding = 'UTF-8', newline = '') as sakotnejais_fails:
        lasitajs = csv.DictReader(sakotnejais_fails) #pārveido par vārdnīcu
        sakotnejie_dati = list(lasitajs)

        #atjauno datus
        for persona in sakotnejie_dati:
            persona['Vecums'] = int(persona['Vecums'])+1 #palielina vecumu par 1

        #ieraksta jaunus datus jaunā failā
    with open(jaunie_dati_fails, 'w', encoding = 'UTF-8',newline='') as jauns_fails:
        rakstitajs = csv.DictWriter(jauns_fails, fieldnames=['Vards','Uzvards','Vecums'])
        rakstitajs.writeheader()
        rakstitajs.writerows(sakotnejie_dati)
    print(f"Dati ir atjaunināti un saglabāti failā '{jaunie_dati_fails}'.")

except FileNotFoundError:
    print(f"Kļūda: Fails '{sakotnejie_dati_fails}' nav atrasts. ")
except Exception as e:
    print(f'Kļūda: meparedzēta kļūda - {e}')

