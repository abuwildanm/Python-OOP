# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 15:28:52 2019

@author: MSI
"""

class Hero: #template
	#class variable / static variable
	jumlah = 0

	def __init__(self,inputName,inputHealth,inputPower,inputArmor):
		# instance variable
		self.name = inputName
		self.health = inputHealth
		self.power = inputPower
		self.armor = inputArmor
		Hero.jumlah += 1
		print("membuat Hero dengan nama " + inputName)


hero1 = Hero("sniper",100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("mirana",100, 15, 1)
print(Hero.jumlah)
hero3 = Hero("ucup",1000, 100, 0)
print(Hero.jumlah)