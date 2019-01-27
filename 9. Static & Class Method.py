# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 20:45:05 2019

@author: MSI
"""

class Hero:

	#private class variabel
	__jumlah = 0;

	def __init__(self,name):
		self.__name = name
		Hero.__jumlah += 1

	# method ini hanya berlaku untuk objek
	def getJumlah(self):
		return Hero.__jumlah

	# method ini tidak berlaku untuk objek tapi berlaku untuk class
	def getJumlah1():
		return Hero.__jumlah

	# method static nempel ke objek dan class
	@staticmethod #decorator
	def getJumlah2():
		return Hero.__jumlah

	@classmethod
	def getJumlah3(cls):
		return cls.__jumlah

sniper = Hero('sniper')
print(sniper.getJumlah())
print(Hero.getJumlah1())
rikimaru = Hero('rikimaru')
print(Hero.getJumlah2())
print(sniper.getJumlah2())
drowranger = Hero('drowranger')
print(Hero.getJumlah3())
print(sniper.getJumlah3())