# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 23:32:35 2019

@author: MSI
"""

# abc = abstract base class
from abc import ABC,abstractmethod

class Button(ABC):

	@abstractmethod #decorator yang memaksa bahwa method ini harus diimplementasikan oleh pewarisnya
	def click(self):
		pass

class PushButton(Button):
	
	def click(self):
		print("push button click")

class RadioButton(Button):

	def click(self):
		print("radio button click")
	

tombol1 = PushButton()
tombol2 = RadioButton()

tombol1.click()
tombol2.click()