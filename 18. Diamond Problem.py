# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 23:07:07 2019

@author: MSI
"""

class A:
	
	def show(self):
		print("ini adalah show A")

class B(A):
	
	def show(self):
		print("ini adalah show B")

class C(A):
	
	def show(self):
		print("ini adalah show C")

class D(B,C):
	pass

objek = D()
objek.show()
help(objek)