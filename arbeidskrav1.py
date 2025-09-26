#Program som beregner kostnader for elbil og bensinbil
#Programmert av Dagfinn Kristoffersen (dagfinnk@gmail.com)
#Oppdatert 2025.09.23
#Programmet beregner og sammenligner årlige kostnader for elbil og bensinbil.

#Spør brukeren om antall km. pr år
km_aar = int(input("Hvor mange km. kjører du pr år? "))  #gjør om til heltall

#Sett faste kostnader

trafikkforsikring = 8.38  #kr pr dag
elbil_forsikring  = 5000  #kr pr år
bensin_forsikring = 7500  #kr pr år
el_bomavgift      = 0.1   #kr pr km
bensin_bomavgift  = 0.3   #kr pr km

drivstoff_pr_km = 2         #kr pr km for bensinbil
el_kostnad_pr_km = 2*0.2    #kr pr km

#Beregne årlige kostnader
el_kostnad_aar = (trafikkforsikring*365) + elbil_forsikring + (el_bomavgift*km_aar) + (el_kostnad_pr_km*km_aar)            #Summerer alle kostnader for elbil
bensin_kostnad_aar = (trafikkforsikring*365) + bensin_forsikring + (bensin_bomavgift*km_aar) + (drivstoff_pr_km*km_aar) #Summerer alle kostnader for bensinbil  

#Skriv ut resultatet
print("Årlige kostnader for elbil:    ", el_kostnad_aar, "kr")
print("Årlige kostnader for bensinbil:", bensin_kostnad_aar, "kr")
print("Forskjell i årlige kostnader:  ", round(bensin_kostnad_aar - el_kostnad_aar,2), "kr") #Rund av resultatet til 2 desimaler

