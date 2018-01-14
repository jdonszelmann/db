from . import constants
from .logging import *

class dbtype():
	def __init__(self):
		pass

	def get(self, value):
		return value

class unique(dbtype):
	start = -1
	def __init__(self, *args, start=None,**kwargs):
		super().__init__(*args,**kwargs)
		if start != None:
			self.start = start

	def get(self, value):
		if not value == constants.auto: log("value of 'unique' datatype must be db.auto", importance=6)
		self.start+=1
		return self.start

	def repr(self, value):
		return str(value)[:constants.printcolumnwidth-1].ljust(constants.printcolumnwidth)

class short_text(dbtype):
	def get(self, value):
		if value == Ellipsis:
			return value
		if not type(value) == str: log("value of 'short_text' datatype must be a string", importance=6)
		if not len(value) < 128: log("value of 'short_text' datatype must have length < 128 (now {})".format(len(value)), importance=6)
		return value

	def repr(self, value):
		return str(value)[:constants.printcolumnwidth-1].ljust(constants.printcolumnwidth)

class long_text(dbtype):
	def get(self, value):
		if value == Ellipsis:
			return value
		if not type(value) == str: log("value of 'short_text' datatype must be a string", importance=6)
		return value
	
	def repr(self, value):
		return str(value)[:constants.printcolumnwidth-1].ljust(constants.printcolumnwidth)

class number(dbtype):
	def get(self, value):
		if value == Ellipsis:
			return value
		if not type(value) in [int,float]: log("value of 'number' datatype must be a int or float", importance=6)
		return value
	
	def repr(self, value):
		return str(value)[:constants.printcolumnwidth-1].ljust(constants.printcolumnwidth)	

class yesno(dbtype):
	def get(self, value):
		if value == Ellipsis:
			return value
		if not type(value) == bool: log("value of 'yesno' datatype must be a bool",  importance=6)
		return value
	
	def repr(self, value):
		return str(value)[:constants.printcolumnwidth-1].ljust(constants.printcolumnwidth)	
