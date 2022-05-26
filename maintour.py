from retoclase.Ciclista import Ciclista

ciclista=Ciclista()
ciclista.nombre="Juan"
ciclista.edad=18
ciclista.pais="Colombia"
ciclista.tiempo=0
print("Nombre: ", ciclista.nombre)
print("Edad: ", ciclista.edad)
print("Pais: ", ciclista.pais)
print("Tiempo: ", ciclista.tiempo)

opcion=-1
ciclistas=[]
while(opcion!=0):
    print("**********")
    print("Digitar 1 para registrar un ciclista")
    print("Digitar 2 para mostrar ciclista con mejor tiempo")
    print("Digitar 0 para cerrar programa")
    print("**********")
    opcion = int(input("Digite una opción: "))
    if(opcion==1):
        ciclista = {}
        ciclista['nombre'] = input("Digita el nombre del ciclista: ")
        ciclista['edad'] = int(input("Digita la edad del ciclista: "))
        ciclista['pais'] = input("Digita el pais del ciclista: ")
        ciclista['tiempo'] = int(input("Digita el tiempo del ciclista: "))
        ciclistas.append(ciclista)
    elif(opcion==2):
        print(ciclistas['tiempo'])
    elif(opcion==0):
        print("Ha cerrado satisfactoriamente el programa")
        break