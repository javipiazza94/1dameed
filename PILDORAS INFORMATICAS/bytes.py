tipoByte = b"papa"
print(type(tipoByte))

adaptacionByte = bytes("ñ", "utf-8") #lo adaptamos a utf8
print(adaptacionByte)

#modificamos bytearray
ba1=bytearray(b'hola')
ba1[2]=123
print(ba1)

#Podemos también convertir una cadena unicode a bytes utilizando el método encode:
cad="piña"
byte1=cad.encode("utf-8")
print(byte1)

#Para hacer la función inversa, convertir de bytes a unicode utilizamos el método decode:
byte1.decode("utf-8")

