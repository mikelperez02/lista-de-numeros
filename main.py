numero = int(input("Digame cuantas palabras tiene la lista:"))
if numero < 1:
  print("¡Imposible!")
else:
  lista = []
  for i in range(numero):
    print("Digame la palabra", str(i + 1) + ":", end="")
    palabra = input()
    lista += [palabra]
    print("La lista creada es:",lista)
    eliminar = input("Palabra que deseo eliminar:")
    for i in range(len(lista)-1, -1, -1):
      if lista[i] == eliminar:
        del(lista[i])
        print("La lista ahora es:", lista)
