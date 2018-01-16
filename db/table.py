from . import constants, types
from .logging import *
import pickle


class table():
	def __init__(self, types, keys, name, order, records=[]):
		self.order = order
		self.records = records
		self.types = types
		self.keys = keys
		self.name = name
	
	def query(self, name=None):
		"""
		esentially returns a copy of the table which can be edited by a query
		"""
		if name == None:
			name = "query"
		from .query import query
		return query(self.types,self.keys,"{} from table '{}'".format(name,self.name),self.order,self.records)

	def new_record(self, record={}, **kwargs):
		"""
		adds a new record to the database

		record must contain keys mapped in the setup object
		"""
		record.update(kwargs)

		record_new = {}
		for i in self.types.keys():
			if i not in record.keys():
				if i in self.keys:
					raise log("primary key ({}) omitted in new_record".format(i), importance=6)
				record[i] = ...

		for key, item in record.items():
			if not key in self.types: log("invalid db key detected in new record ({})".format(key), importance=6)
			record_new.update({key:self.types[key].get(item)})
		self.records.append(record_new)


	def __repr__(self):
		returntext = "_______________\ntable '{}':\n".format(self.name if self.name != None else "<unnamed>")
		for i in self.order:
			for j in self.types:
				if i == j:
					returntext += j.ljust(constants.printcolumnwidth+1)
		returntext += "\n\n"
		for i in self.records:
			for j in self.order:
				for key,item in i.items():
					if key == j:
						returntext += self.types[key].repr(item)
						returntext += " "
			returntext += "\n"
		returntext += "_______________\n"
		return returntext

	def save(self,name=None):
		if name == None:
			name = self.name
		with open("{}.dbfile".format(name),"wb") as f:
			pickle.dump({"name":self.name,"order":self.order,"records":self.records,"types":self.types,"keys":self.keys}, f, pickle.HIGHEST_PROTOCOL)
		return name

	def exportto(self,name=None,type="csv", seperator=","):
		if name == None:
			name = self.name
		with open("{}.csv".format(name),"w") as f:
			header = []
			for i in self.order:
				for j in self.types:
					if i == j:
						header.append(i)
			f.write(seperator.join(header))
			f.write('\n')
			for i in self.records:
				record = []
				for j in self.order:
					for key,item in i.items():
						if key == j:
							record.append(str(item))
				f.write(seperator.join(record))
				f.write('\n')
		return name

def exists(name):
	try:
		f = open("{}.dbfile".format(name),"rb").read()
		return True
	except Exception:
		return False

def load(name):
	with open("{}.dbfile".format(name),"rb") as f:
		res = pickle.load(f)
		return table(res["types"],res["keys"],res["name"],res["order"],res["records"])
