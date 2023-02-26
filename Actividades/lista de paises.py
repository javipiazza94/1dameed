lista = input("Dame el nombre de varios paises: ")
paises = [pais for pais in lista.split(",")]
print(type(paises))
print(",".join(sorted(list(set(paises)))))