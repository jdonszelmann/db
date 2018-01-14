from .table import *
from . import types
from .logging import *

class db():
	def __init__(self):
		pass
	
	@classmethod
	def importfrom(self,name=None,typen="csv",seperator=","):
		order = True
		if not hasattr(self,"setup"): log("no db setup found",importance=6)
		if not hasattr(self,"primarykey"):
			log("no primary key found",importance=2)
			self.primarykey = []
		if not hasattr(self,"order"):
			log("no order found",importance=2)
			self.order = list(self.setup.keys())
			order = False
		if not set(self.order) == set(self.setup.keys()): log("order key mismatch", importance=6)
		for i in self.primarykey:
			if not i in self.setup:
				log("primary key not found in setup", importance=6)
		if hasattr(self,"name") and name == None:
			name = self.name
		elif name != None:
			try:
				f = open("{}.csv".format(name),"r")
			except Exception:
				log("no valid name found for csv file (not in setup nor in function call)", importance=6)
		else:
			log("no name found in setup",importance=2)
			try:
				f = open("None.csv","r")
			except Exception:
				log("no valid name found for csv file (not in setup nor in function call)", importance=6)
		log("opening '{}.csv'".format(name),importance=1)

		with open("{}.csv".format(name),"r") as f:
			file = f.readlines()
			for i in file:
				if not seperator in i: log("seperator not found on line {} of {}.csv".format(file.index(i),name),importance=5)

			if order:
				header = file[0].split(seperator)
				if not len(header) == len(self.order): log("invalid header size", importance=6)
				for index,i in enumerate(header):
					if i.strip() != self.order[index].strip():
						log("invalid header", importance=6)
				t = table(self.setup, list(set(self.primarykey)), name, self.order,[dict(zip([i.strip() for i in header], [j.strip() for j in i.split(seperator)])) for i in file[1:]])
				for key,item in t.types.items():
					if type(item) == types.unique:
						count = 0
						for i in t.records:
							for key1,item1 in i.items():
								if key1 == key:
									count += 1
									i[key] == int(i[key])
						item.start = count
					if type(item) == types.yesno:
						for i in t.records:
							for key1,item1 in i.items():
								if key1 == key:
									i[key] = True if i[key] == "True" else False
					if type(item) == types.number:
						for i in t.records:
							for key1,item1 in i.items():
								if key1 == key:
									i[key] == int(i[key])

				return t


			else:
				header = file[0].split(seperator)
				log("generating order from csv",importance=1)
				if not len(header) == len(self.setup): log("invalid header size", importance=6)
				self.order = [i.strip() for i in header]
				t = table(self.setup, list(set(self.primarykey)), name, self.order,[dict(zip([i.strip() for i in header], [j.strip() for j in i.split(seperator)])) for i in file[1:]])
				for key,item in t.types.items():
					if type(item) == types.unique:
						count = 0
						for i in t.records:
							for key1,item1 in i.items():
								if key1 == key:
									count += 1
									i[key] == int(i[key])
						item.start = count
					if type(item) == types.yesno:
						for i in t.records:
							for key1,item1 in i.items():
								if key1 == key:
									i[key] = True if i[key] == "True" else False
					if type(item) == types.number:
						for i in t.records:
							for key1,item1 in i.items():
								if key1 == key:
									i[key] == int(i[key])
				return t

	def __new__(self):
		if not hasattr(self,"setup"): log("no db setup found",importance=6)
		if not hasattr(self,"primarykey"):
			log("no primary key found",importance=2)
			self.primarykey = []
		if not hasattr(self,"order"):
			log("no order found",importance=2)
			self.order = list(self.setup.keys())
		if not set(self.order) == set(self.setup.keys()): log("order key mismatch", importance=6)
		for i in self.primarykey:
			if not i in self.setup:
				log("primary key not found in setup", importance=6)
		if hasattr(self,"name"):
			name = self.name
		else:
			log("no name found in setup",importance=2)
			name = None
		return table(self.setup, list(set(self.primarykey)), name, self.order)





