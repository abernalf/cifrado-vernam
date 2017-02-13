# -*- coding: utf-8 -*-
import binascii

def des_binarizar(text):
	b = str(text[0])
	for i in range(1,len(text)):
		b += str(text[i])
	n = int(b, 2)
	return binascii.unhexlify('%x' % n)

def binarizar(text):
	a = bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in text), 0))
	b = [int(a[0])]
	for i in range(2,len(a)):
		b += [int(a[i])]
	print b
	return b
	
b = binarizar('Hola')
des_binarizar(b)