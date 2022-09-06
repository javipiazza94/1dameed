import time # Importamos el paquete Time

hora_pc = time.strftime('%H') #aplicamos la funcion .strftime que vuelve un string de la hora del dispositivo. Especificamos que nos devuelva la hora
minutos_pc = time.strftime('%M') #Lo mismo pero con los minutos. El dato devuelto aparece en la implementacion del metodo

#Imprimimos la hora actual
print ("Son las", hora_pc,"y", minutos_pc, "minutos")

#Hacemos el if y en else hacemos la resta
if int(hora_pc) >= 19:
	print ("Se acabo lo bueno, para casa") 
else:
	print ("Quedan", format(18- int(hora_pc)), "horas y", format(59-int(minutos_pc)), "minutos para las 20 horas e irnos a casa")
            #restamos la hora anterior con la del PC y lo mismo con los minutos
