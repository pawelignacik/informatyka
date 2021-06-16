from ics import Calendar, Event
import arrow
from datetime import datetime
import pytz
import random


teraz = arrow.get()

with open('plan_zajec.ics', encoding='utf8') as plik_ics:
    kalendarz = Calendar(plik_ics.read())
    
with open('plan_zajec2.ics', encoding='utf8') as plik_ics2:
    kalendarz2 = Calendar(plik_ics2.read())    
    
def wyswietl(y):
    print('PLAN ZAJĘC:' )   
    for wpis in y.events:
        if((poczatek <= wpis.end and koniec >= wpis.begin)
           or (koniec >= wpis.end and poczatek <= wpis.end)
           or (poczatek >= wpis.begin) and (koniec<=wpis.end)):
            print(wpis.name)
            print('Początek: %s' %wpis.begin)
            print('Koniec: %s' %wpis.end)
            print('--------------------------------------------------')
            
    print("")
   
wynik = []

def losuj_godzine():
    godz = random.randint(start,koniec)
    if godz not in wynik:
        wynik.append(godz)
        godzina_spotkania = str(arrow.get(rok, miesiac, dzien, godz, 10))
        
        '''
        #godzina_spotkania = str(godzina_spotkania.split(":"))
        godzina_spotkania = str(godzina_spotkania.split("T"))
        godzina_spotkania = str(godzina_spotkania.split("00+00:00"))
        print(godzina_spotkania[5])
        '''
        godzina_spotkania = godzina_spotkania.replace(":00+00:00",":00+02:00")

        #print("proba: " +str(godzina_spotkania))
        
        sprawdz_godzine(godzina_spotkania)
        
        
    else:
        losuj_godzine()
test = str("2021-05-15T15:10:00+02:00")
    
def sprawdz_godzine(godz):
    #print("wylosowana godzina: "+ str(godz))
    #print("           tab1[0]= " + str(tab1[0])+"\n")
    #print("Sprawdzanie czy o podanej godzinie sa zajecia: " + str(godz))
    #for i in tab1:
    if(godz == str(tab1[0])):
        #print("O tej godzinie są już zajęcia")
        losuj_godzine()
    else:
        print("Możliwe spotkanie o: "+ str(godz) +"\n\n\n")
    
    
    
poczatek = arrow.get(2021, 5, 15, 10,15)
koniec = arrow.get(2021, 5, 25, 16, 00)

wyswietl(kalendarz)
wyswietl(kalendarz2)


tab1=[]
for wpis in kalendarz.events: 
    if((poczatek <= wpis.end and koniec >= wpis.begin)
       or (koniec >= wpis.end and poczatek <= wpis.end)
       or (poczatek >= wpis.begin) and (koniec<=wpis.end)):
            #print(wpis.begin)
            tab1.append(wpis.begin)

            
print(' ')

tab2=[]
for wpis in kalendarz2.events: 
    if((poczatek <= wpis.end and koniec >= wpis.begin)
        or (koniec >= wpis.end and poczatek <= wpis.end)
        or (poczatek >= wpis.begin) and (koniec<=wpis.end)):
            #print(wpis.begin)
            tab2.append(wpis.begin)
            


tab1.sort();
tab2.sort();

print("")



rok = 2021
miesiac = 5
dzien = 15
start = 9
koniec = 16


losuj_godzine()
losuj_godzine()


