import math
import random

pirmais_teikums = ['Esot vērīgam, tev izdosies tikt vaļā no nepatikšanām.','Pievēršoties mīlestībai, izrādi vairāk jaukuma pasaulei.','Izdarot lielu soli, atsakies no kaut kā sen nevajadzīga.','Izvēloties priekš sevis labāko, pievērsies sev un saviem mērķiem.','Šaudzējot sevi, atsakies no prokrastinācijas']

otrais_teikums = ['Ieteikums tev ir fokusēties uz svarīgākām lietām, bet to, kas ir sekundārs un sajauc galvu, noliec malā.','Ieteikums tev ir aizrakt savu pesimismu un pievērsties kaut kam pozitīvākam.','Ieteikums tev ir atrast vietu dzīvē jaunām lietām un paplašināt savus horizontus.','Ieteikums tev ir padomāt vairāk par sevi, bet neizskar citu cilvēku personīgos rāmjus.','Ieteikums tev ir neatlikt svarīgus darbus un domāt uz priekšu.']

rikojums = ['Paliec pozitīvs un spēsi sasniegt visu!','Uzmanies no negatīviem cilvēkiem, kas var tevi pavilkt līdzi!','Atrodi laiku padomāt par sevi!','Aizmirsti par pagātni, kas tevi sāpina!','Iemācies savienot darbu ar atpūtu!']

zodiaka_zimes = ['Strēlnieks','Skorpions','Svari','Jaunava','Vērsis','Ūdensvīrs','Vēzis','Auns','Zivs','Dvīņi','Mežāzis','Lauva']

def beigt(stop):                         #funkcija beigt() ļauj lietotājam jebkurā brīdī beigt programmas darbību.
    if stop == 'stop':
        print('Paldies par programmas izmantošanu, uzredzēšanos!')
        exit()

def prognozes():                       #funkcija prognozes() izvēlās teikumus no sarakstiem, lai izveidotu netīšus tekstiņus.
    global teksta_izveide
    teksta_izveide = random.choice(pirmais_teikums)
    global teksta_izveide2
    teksta_izveide2 = random.choice(otrais_teikums)
    global teksta_izveide3
    teksta_izveide3 = random.choice(rikojums)
    global zimes
    zimes = (zodiaka_zimes)


for x in zodiaka_zimes:                #izprintē zodiaka zīmju tekstiņus
    prognozes()
    print(x)
    print(teksta_izveide,'\n',teksta_izveide2,'\n',teksta_izveide3,'\n')


while True:
    jautajums = input('Vai jūs vēlaties plašāku astroloģisko prognozi?(j/n):\n')
    beigt(jautajums)
    if jautajums == 'j':                               #ja lietotājs ieraksta 'j' - jā, tad tam piedāvā ierakstīt savu zīmi un, kad tas to ir izdarījis tiek izprintētas paplašinātas astroloģiskās prognozes.
        jautajums2 = input('Ievadiet savu zodiaka zīmi!:\n')
        beigt(jautajums2)
        if jautajums2 == zodiaka_zimes[0]:
            print('Nelaid garām iespēju atgādināt priekšniecībai un dažādiem ierēdņiem viņu solījumus un pienākumus. Uz negaidītiem sarežģījumiem centies reaģēt mierīgi. Aizstāvi savas intereses, cīnies par taisnīgu darbu sadali un godīgu samaksu. Mājās iespējami pārpratumi tur, kur tos nepavisam negaidīji. Lai saprastos ar otru, nāksies ieklausīties partnerī. Aicini taupīt, nevis tērēt!')
            exit()
        elif jautajums2 == zodiaka_zimes[1]:
            print('Piedāvājumu iesaistīties jaunā projektā rūpīgi izvērtē, nepaļaujies uz mutiskiem solījumiem. Uzskati, ka darījums ir noslēgts tikai tad, kad sakārtoti dokumenti, parakstīts līgums. Varbūt to ir vērts atlikt uz jaunā gada ieskaņu. Personīgā dzīve būs mierīga un līdzsvarota, ja vien partnerim neuzspiedīsi savu viedokli, bet vairāk pielāgosies viņa vēlmēm.')
            exit()
        elif jautajums2 == zodiaka_zimes[2]:
            print('Nopietni izturies pret ikvienu iespēju sevi parādīt darbā. Ja ar kādu darbu netiec galā, atliec to, izdari kaut ko citu un tad atgriezies pie atliktā uzdevuma - kad domas un attieksme būs cita, darbs veiksies labāk. Attiecībās meklē zelta vidusceļu. Kam būs bijusi taisnība, nākotne parādīs. Iespējams, tālredzīgi izdarīsi tieši to, kas nepieciešams, lai saglabātu dzīves stabilitāti, ierasto dzīves ritmu un ērtības')
            exit()
        elif jautajums2 == zodiaka_zimes[3]:
            print('Par nepadarītiem darbiem neraizējies, koncentrējies uz svarīgākajiem un nozīmīgākajiem, visu līdz gada noslēgumam tāpat nepaspēsi. Neļauj sevi pierunāt darīt to, kas ir pretrunā ar taviem principiem. Galvenais – neatkāpties grūtību priekšā. Paļaujies ne tikai uz veiksmi, bet arī uz zināšanām un prasmi tās pareizi izmantot. Respektē draugu un tuvinieku noskaņojumu.')
            exit()
        elif jautajums2 == zodiaka_zimes[4]:
            print('Attiecībās izvairies no pavēlnieciska toņa, jo ar piekāpību un diplomātiju panāksi vairāk nekā ar uzstājību. Spēja saprasties palīdzēs neapjukt, bet nerimstoša zinātkāre mudinās nepadoties un virzīties uz priekšu par spīti grūtībām. Uzturi ciešu saiti ar labvēļiem. Risinot sadzīviskas problēmas, drosmīga, izlēmīga rīcība attaisnosies. Nešaubies – uzticies!')
            exit()
        elif jautajums2 == zodiaka_zimes[5]:
            print('Palīdzi tuviniekiem risināt viņu problēmas. Nenosodi, nekritizē, bet gan iedrošini, sniedz emocionālu un praktisku atbalstu. Atvēli laiku sarunām, domu apmaiņai, attīsti iepriekš radušās idejas. Reāls skats uz dzīvi pasargās no vilšanās un slikta garastāvokļa. Tev būs pa spēkam jebkura loma, kuru izvēlēsies. Rūpīgi seko līdzi tam, kur paliek tavs laiks un nauda')
            exit()
        elif jautajums2 == zodiaka_zimes[6]:
            print('Pievērsies lietišķu jautājumu risināšanai, kal nākotnes plānus, domā par to, kā pēc iespējas pilnvērtīgāk izmantot radušās iespējas. Iesākumā šķēršļu, kas traucē veiksmīgi virzīties uz priekšu, būs maz, izmanto to. Gatavojoties gadumijai, atrodi iemeslu priekam. Attiecībās ar mīļoto parādīsies rotaļīgs vieglums, būs patīkami vienam otru iepriecināt, pārsteigt.')
            exit()
        elif jautajums2 == zodiaka_zimes[7]:
            print('Pirms veic lielāku pirkumu, izpēti cenas un piedāvājumu, lai nesanāk pārmaksāt. Dzīvo racionāli, un tev izdosies šo to pat ietaupīt. Gada izskaņā saņemot augstāka amata piedāvājumu, piekrišanu dod tikai tad, kad esi rūpīgi apsvēris visus plusus un mīnusus. Nenoliedzami, ka finansiāli būsi ieguvējs, bet vai tevi apmierinās darba apjoms un atbildība – to rādīs laiks.')
            exit()
        elif jautajums2 == zodiaka_zimes[8]:
            print('Lai nezaudētu stabilitāti, atvirzi emocijas otrajā plānā, neļauj pesimistiskiem prātojumiem ietekmēt darba kvalitāti. Ja sāc šaubīties par sevi, tas nenozīmē, ka no kaut kā jāatsakās. Atliec uz brīdi, pievērsies izklaidei un svētku pasākumu organizēšanai, tas uzlādēs ar pozitīvu enerģiju. Uzkrātais spēks noderēs, kad vajadzēs uzņemties iniciatīvu, lai novērstu trūkumus un nebūšanas.')
            exit()
        elif jautajums2 == zodiaka_zimes[9]:
            print('Sabiedriskā gaisotne, skaļi pasākumi nebūs domāti tev, priekšroku dod aktivitātēm, kur iespējams iedziļināties, izpētīt, būt aci pret aci ar sarunu biedru. Pacenties atturēties no racionāliem spriedumiem. Turpinājumā enerģijas netrūks, ideju būs daudz, turklāt tev izdosies tās pasniegt pietiekami pārliecinoši, lai saņemtu nepieciešamo atbalstu, un no teorētiskiem prātojumiem gada izskaņā pāriet pie praktiskas zināšanu apguves jaunajā gadā.')
            exit()
        elif jautajums2 == zodiaka_zimes[10]:
            print('Liec lietā izdomu, ļaujies azartam, taču vairies no spontānas rīcības, nezaudē kontroli pār sevi un procesiem, kuros esi iesaistīts. Situācijā, kad darbs dzen darbu, atrast brīdi pārdomām būs grūti, bet, ja tas izdosies, tiksi pie vērtīgām atziņām. Tās palīdzēs izdarīt adekvātus secinājumus un ievirzīt notikumus vēlamajā gultnē, lai plūktu kārotos uzvaras laurus.')
            exit()
        elif jautajums2 == zodiaka_zimes[11]:
            print('Neuzņemies riskantas saistības pat tad, ja labi rezultāti šķiet garantēti, jo sakāpinātu emociju, ilūziju un veltīgu cerību ietekmē vari izdarīt aplamu izvēli. Ko par tavu rīcību domā apkārtējie, būs grūti izdibināt, bet, paliekot mājās, neapmierinātība pārvērtīsies nesaskaņās, var sākties rīvēšanās, kašķēšanās. Neļauj sadzīviskām nebūšanām izjaukt cēlus nodomus un svētku noskaņu!')
            exit()
        else:
            print('Ievadiet pareizus datus!')           #ja lietotājs ir ievadījis nepareizus datus, tas tiek paziņots un jautājums tiek izprintēts vēlreiz.
    elif jautajums == 'n':                     #ja lietotājs ievada 'n' - nē, tad programma atvadās un beidz savu darbību.
        print('Paldies par programmas izmantošanu, uzredzēšanos!')
        exit()
    else:
        print('Ievadiet pareizus datus!')           #ja lietotājs ir ievadījis nepareizus datus, tas tiek paziņots un jautājums tiek izprintēts vēlreiz.
        
