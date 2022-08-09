
import time

hora = time.strftime('%H') 
minutos = time.strftime('%M') 


if int(hora) >= 18:
	print ("Vamonos a casa") 
else:
	print ("Quedan {} horas y {} minutos para irnos a casa".format(17- int(hora), 57-int(minutos)))