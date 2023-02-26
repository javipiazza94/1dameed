# Aporta informacion al programa. Funciona por niveles (criticidad). Trazan lo que hace el programa (logger)
import logging 

logging.basicConfig(level=logging.INFO) #Igualamos los .info con los warning hacia abajo
logging.debug("Greta tiene razon")
logging.info("El Clima climatico va a acabar con todos nosotros")
logging.warning("EL FIN DEL MUNDO SE ACERCA. VAMOS A MORIR TODOS")
logging.error("Tenemos que volver a la Edad Media para salvar el planeta")
logging.critical("RETURN TO TRADITION")
#Esta es la escala de criticidades
