# -*- coding: utf-8 -*-
import binascii

def in_datos():
	print("-----------------------------------------------")
	mensaje = raw_input("Incluya la palabra que quiere cifrar/descifrar: ")
	mensaje = str(mensaje)
	return mensaje

def binarizar(text):
	a = bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in text), 0))
	b = [int(a[0])]
	for i in range(2,len(a)):
		b += [int(a[i])]
	return b

def des_binarizar(text):
	b = str(text[0])
	for i in range(1,len(text)):
		b += str(text[i])
	n = int(b, 2)
	return binascii.unhexlify('%x' % n)

	
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
		#print str(mensaje_v[i]) + " " + str(clave_v[i])
		resultado_v += [mensaje_v[i] ^ clave_v[i]]
	return resultado_v

def mostrar(resultado_v,tam):
	#muestra = str(resultado_v[0])
	#for i in range(1,tam):
	#	muestra += str(resultado_v[i])
	print "Resultado en binario: " + str(resultado_v)
	muestra = des_binarizar(resultado_v)
	print ("El resultado es: "+muestra)

#---------Main

w = 's'
while w == 's':
	mensaje = in_datos() #LEE DATOS1
	mensaje = binarizar(mensaje)
	print "Mensaje en binario: " + str(mensaje)
	tam = len(mensaje)	#TAMAÑO DE DATOS1
	clave = in_clave(tam) #LEE DATOS2
	#mensaje_v = to_vector(mensaje,tam) #PASA A VECTOR
	clave_v = to_vector(clave,tam) #PASA A VECTOR
	resultado_v = vernam(mensaje,clave_v,tam) #EJECUTA ALGORITMO
	print("-----------------------------------------------")
	mostrar(resultado_v,tam) 
	w = raw_input("----¿DESEA REALIZAR OTRA OPERACIÓN?[s/n]----")

#---------FIN MAIN