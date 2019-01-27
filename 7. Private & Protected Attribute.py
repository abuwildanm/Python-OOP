# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 20:12:35 2019

@author: MSI
"""

class Hero:

	# class variabel
	jumlah = 0
	__privateJumlah = 0 # private

	def __init__(self,name,health):
		self.name = name
		self.health = health

		# variabel instance private
		self.__private = "private"
		# variabel instance protected
		self._protected = "protected"



lina = Hero("lina",100)

print(lina.__dict__)
print(Hero.__dict__)
#print(Hero.__privateJumlah)