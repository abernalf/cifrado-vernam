# -*- coding: utf-8 -*-
def in_datos():
	print("-----------------------------------------------")
	mensaje = raw_input("Incluya el codigo en binario que quiere cifrar/descifrar: ")
	mensaje = str(mensaje)
	return mensaje
	
def in_clave(tam):
	print("-----------------------------------------------")
	mensaje = raw_input("Incluya la clave con la que va a cifrar/descifrar, recuerde que el tamaño debe ser de "+ str(tam)+ " :")
	mensaje = str(mensaje)
	return mensaje
def to_vector(mensaje,tam):
	mensaje_v = [int(mensaje[0])]
	for i in range(1, tam):
		mensaje_v += [int(mensaje[i])]
	return mensaje_v
def vernam(mensaje_v,clave_v,tam):
	resultado_v= [mensaje_v[0] ^ clave_v[0]]
	for i in range (1,tam):
		resultado_v += [mensaje_v[i] ^ clave_v[i]]
	return resultado_v

def mostrar(resultado_v,tam):
	muestra = str(resultado_v[0])
	for i in range(1,tam):
		muestra += str(resultado_v[i])
	print ("El resultado es: "+muestra)

#---------Main

w = 's'
while w == 's':
	mensaje = in_datos() #LEE DATOS1
	tam = len(mensaje)	#TAMAÑO DE DATOS1
	clave = in_clave(tam) #LEE DATOS2
	mensaje_v = to_vector(mensaje,tam) #PASA A VECTOR
	clave_v = to_vector(clave,tam) #PASA A VECTOR
	resultado_v = vernam(mensaje_v,clave_v,tam) #EJECUTA ALGORITMO
	mostrar(resultado_v,tam) 
	w = raw_input("----¿DESEA REALIZAR OTRA OPERACIÓN?[s/n]----")

#---------FIN MAIN