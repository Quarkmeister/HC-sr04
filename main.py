import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

#Defintion der GPIO Pins für trigger und echo
trig = 3
echo = 4

print("Messung startet")
gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)

gpio.output(trig, False)
time.sleep(0.5)

distanzes = list()

timePoint_start = time.time()
while time.time() - timePoint_start < 5:
    #Senden des Ultraschallsignals für 0,00001 Sekunden
    gpio.output(trig, True)
    time.sleep(0.00001)
    gpio.output(trig, False)

    #Solange keine Schallwelle eintrifft bleibt echo auf 0,
    #sobald sie da ist wird echo auf 1 geschaltet
    #time.time() liefert den Unix-Timestamp zum aktuellen Zeitpunkt
    #) →֒Sekunden seit dem 01.01.1970)
    while gpio.input(echo) == 0:
        start = time.time()
    while gpio.input(echo) == 1:
        stop = time.time()

    #Berechnung der Zeitdifferenz und der Distanz
    #Schallgeschwindigkeit trockene Luft, 20°C beträgt 343,20 m/s
    #Runden des Distanzwerts auf 2 Nachkommastellen
    delta_t = stop - start
    distanzes.append(round(delta_t * 34320/2, 2))

distanzes_midd = list()
buffer = 0
for i in range(len(distanzes)):
    if i % 5 != 0:
        buffer += distanzes[i]
    else
        distanzes_midd.append(buffer/5)
        buffer = 0

textfile = open("ultraschall.csv", "w")
for element in distanzes_midd:
    textfile.write(str(element) + "\n")

textfile.close()