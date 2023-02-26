#Programacion multihilo --> Se ejecutan multiples funciones en paralelo. Hay concurrencia, suceden multiples eventos a la vez
                            #Permite que los programas sean mucho mas rapidos#
                            
import _thread
import time

def HoraActual(nombre_thread, tiempo_espera):
    count = 0
    while count<3:
        time.sleep(tiempo_espera)# Anadimos los segundos de espera, que estan en formato int
        count+=1
        print(f'hilo: {nombre_thread} - {time.ctime(time.time())}') # Imprimimos el nombre y el tiempo que tarda en la hora actual

_thread.start_new_thread(HoraActual, ("nombre_1", 1))
_thread.start_new_thread(HoraActual, ("nombre_2", 4))

print("Se disparan los hilos")

while True:
    pass
    #time.sleep(0.1) #Se busca dormir el programa para ejecutar los hilos. Esta es la convencion para cargar menos el procesador
    
