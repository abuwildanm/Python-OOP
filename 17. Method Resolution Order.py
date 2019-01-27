# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 22:56:47 2019

@author: MSI
"""

class A:
	
	def show(self):
		print("ini adalah show A")

class B:

	def show(self):
		print("ini adalah show B")

class C(B,A):
	pass
	


objek = C()
objek.show()
help(objek)

"""
Jika ada method yang sama seperti di atas, maka eksekusinya akan mengikuti
method resolution order (bisa dilihat di help())

Pada kasus di atas, method resolution ordernya : C -> B -> A
Hal itu bisa dilihat pada deklarasi class C(B,A)
Sehingga method show() pada class B akan lebih diprioritaskan untuk dieksekusi

Jika deklarasinya adalah C(A,B), maka method resolution ordernya : C -> A -> B
"""