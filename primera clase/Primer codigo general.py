#Braulio Yahir Gaitan Vargas 6°D
#Fecha de creacion: 09/02/2023
#Primera parte del codigo general
print("Universidad de Colima")
nombre = "Braulio Yahir Gaitan Vargas"
print("hola", nombre)
edad = input("Escribe la edad ")
print(nombre,"tiene la edad de:",edad)
print("operacion 1:",4*5-6)
x=4+7
y=x-2
z=x+y
print("x= ", x)
print("y= ", y)
print("z= ", z)

#Coloque este orden asi para que creara el archivo de texto y despues se leeyera el archivo de texto
#Tercera parte Escritura de Archivo
archivo = open("texto2.txt" , "w")

archivo.write("Esto se escribe en el archivo  \n")
archivo.write("esto tambien\n")
archivo.write("mira, puedo escribir \"comillas\"\n ")
archivo.write("Gracias a la diagonal invertida:  \n")

archivo.close


#Segunda parte Lectura de Archivo
archivo = open("texto2.txt" , "r")

texto=archivo.read()
print(texto)

archivo.close()
