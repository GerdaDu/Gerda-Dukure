fails = open('ziema.txt','w', encoding = 'UTF-8') # w izveido neeksistējošu failu no jauna
# ieraksta failā datus

saraksts = ['Alūksne\n','Valmiera\n','Balvi\n']

fails.writelines(saraksts) #ieraksta vairākas līnijas
fails.write('Es te braukšu ar telti gulēt') # ieraksta vienu rindiņu
fails.close()

#pārrakstīt kopēta faila saturu
fails = open('ziema_copy.txt','w+', encoding= 'UTF-8')
fails.write('Varētu drīz iet pusdienās!')
fails = open('ziema_copy.txt','w+', encoding = 'UTF-8')
print(fails.read()) #parāda faila saturu uz ekrāna
fails.close

fails = open('ziema_copy.txt','w+', encoding = 'UTF-8')
fails.write('\nCerams pusdienas šodien būs garšīgas!')
fails.close()