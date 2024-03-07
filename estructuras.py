#Se declaran diccionarios = objetos
clienteUno ={
    "id": "avd658",
    "nombre": "edifUno",
    "Consumo": 200,
    "Ubicacion": "Calle 10"
}
clienteDos={
    "id": "avd679",
    "nombre": "edifDos",
    "Consumo": 500,
    "Ubicacion": "Calle 13"
}

# se declara una lista = arreglo
clientesAsociados=[clienteUno, clienteDos]

#obtener informacion de la lista, recorrer la lista. 
#El rango es el numero de repeticiones dentro del FOR
'''for i in range (10):
    print("El verde es lo mejor")

for i in range (10):
    print(i)

for i in range(3, 10):
    print(i)  ''' 

#interar en el arreglo y escoger el atributo
for i in range(2):
    print(clientesAsociados[i],f"--->",["nombre"])  

#Programar un for each se usa para recorrer arreglos (listas)
# Se recomienda que a variable sea el singular del nombre del arreglo    
    
for cliente in clientesAsociados:
    print(cliente["id"], f"--->",["Consumo"])

for cliente in clientesAsociados:
    print(cliente["id"], '=>', cliente["Consumo"], 'Kv')  
    #otra forma de copiar lo mismo
    print(f"{cliente['id']} =>{cliente['Consumo']} Kv")  
    