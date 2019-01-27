# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 20:55:44 2019

@author: MSI
"""

class Hero:

	def __init__(self, name, health, armor):
		self.name = name
		self.__health = health
		self.__armor = armor
		#self.info = "name {} : \n\thealth: {}".format(self.name,self.__health) #kalo pake ini dibanding pake decorator property, maka isi self.info tidak akan terupdate otomatis

    #decorator untuk mengubah method menjadi atribut yang dinamis, bisa mengikuti perubahan self.name dan self.__health
	@property
	def info(self):
		return "name {} : \n\thealth: {}".format(self.name,self.__health)

	@property
	def armor(self):
		pass

    #decorator untuk getter
    #armor disini didapat dari property bukan dari __armor
	@armor.getter
	def armor(self):
		return self.__armor

    #decorator untuk setter
	@armor.setter
	def armor(self, input):
		self.__armor = input

    #decorator untuk delete atribut
	@armor.deleter
	def armor(self):
		print('armor di delet')
		self.__armor = None

sniper = Hero('sniper',100,10)

print('merubah info')
print(sniper.info)
sniper.name = 'dadang'
print(sniper.info)

print('getter dan setter untuk __armor:')
print(sniper.armor)
sniper.armor = 50
print(sniper.armor)

print('delete armor')
del sniper.armor
print(sniper.__dict__)