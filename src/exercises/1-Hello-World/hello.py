#initialisation
import random as r
import math as m


#main
def main():
	"""Sums up the modules and classes for the programm and executes it in the right order"""
	try:
		test_function()
	except Error as e:
		pass


#modules
def test_function():
	"""Print "Hello World!" and exit"""
	print "Hello World!"


#classes
class ExamlpeClass(object):
	"""docstring for ExamlpeClass"""
	def __init__(self, arg):
		super(ExamlpeClass, self).__init__()
		self.arg = arg
		

#execute
main()