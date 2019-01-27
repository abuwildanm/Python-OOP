# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 23:17:49 2019

@author: MSI
"""

class Mangga:

	#magic method
    
    #constructor
	def __init__(self,nama,jumlah):
		self.nama = nama
		self.jumlah = jumlah

    #sama kaya __str__, cuma biasanya buat debugging
	def __repr__(self):
		return "Debug - Mangga: {} dengan jumlah: {}".format(self.nama,self.jumlah)

    #method biar ketika print objek ada isinya, misal print(belanja1)
	def __str__(self):
		return "Mangga: {} dengan jumlah: {}".format(self.nama,self.jumlah)

    #method buat menjumlahkan dua objek
	def __add__(self,objek):
		return self.jumlah + objek.jumlah

	@property
	def __dict__(self):
		return "objek ini mempunyai nama dan jumlah"


belanja1 = Mangga("arumanis",10)
belanja2 = Mangga("mana lagi",30)
print(repr(belanja1))
print(repr(belanja2))
print(belanja1)
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)