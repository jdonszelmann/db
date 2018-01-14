from . import constants, types
from .logging import *
import time

class query():
	def __init__(self, types, keys, name, order, records=[]):
		self.order = order
		self.records = records
		self.types = types
		self.keys = keys
		self.name = name
		self.selection = records
		self.starttime = time.perf_counter()

	def done(self):
		"""
		esentially returns a copy of the table object which can not be edited by a query
		"""
		from .table import table
		log("query took {} seconds".format(round(time.perf_counter()-self.starttime,8)),importance=1)
		return table(self.types,self.keys,self.name,self.order,self.selection)

	def get(self):
		log("query took {} seconds".format(round(time.perf_counter()-self.starttime,8)),importance=1)
		if len(self.selection) == 1:
			return self.selection[0]
		return self.selection

	def getcol(self,key):
		if not key in self.types: log("invalid key {}".format(key),importance=6)
		log("query took {} seconds".format(round(time.perf_counter()-self.starttime,8)),importance=1)
		ret = []
		for i in self.selection:
			if key in i:
				ret.append(i[key])
			else:
				log("invalid key {}".format(key),importance=6)
		return ret

	def delete(self, match=constants.all):
		if type(match) != list:
			match = [match]
		if match == [constants.all]:
			new_selection = []
			for i in self.records:
				if i not in self.selection:
					new_selection.append(i)
			self.selection = new_selection
			return self
		else:
			new_selection = []
			searcher = []
			for i in self.selection:
				searcher.append({key:item for key,item in i.items() if key in match})
			for i in self.records:
				subdict = {key:item for key,item in i.items() if key in match}
				if subdict not in searcher and i not in new_selection:
					new_selection.append(i)
			self.selection = new_selection
			return self

	def select(self,what):
		if what == constants.all:
			return self
		elif type(what) == list:
			for i in self.selection:
				keys = []
				for key,item in i.items():
					if key not in what:
						keys.append(key)
				for j in keys:
					del i[j]
					if j in self.types:
						del self.types[j]
			return self
		else:
			for i in self.selection:
				keys = []
				for key,item in i.items():
					if key != what:
						keys.append(key)
				for j in keys:
					del i[j]
					if j in self.types:
						del self.types[j]
			return self

	def where(self,a,b,condition):
		edited_selection = []
		for i in self.selection:
			if not a in i: log("invalid rightside in where()",importance=6)
			if condition(i[a],b):
				edited_selection.append(i)
		self.selection = edited_selection
		return self

	def sort(self,by,reverse=False):
		if type(by) == list:
			for i in by:
				if not by in self.types: log("trying to sort by invalid key", importance=6)
			self.selection.sort(key=lambda x: tuple([x[i] if x[i] != Ellipsis else "ellipsis" for i in by]), reverse = reverse)
		else:
			if not by in self.types: log("trying to sort by invalid key", importance=6)
			self.selection.sort(key=lambda x:x[by] if x[by] != Ellipsis else "ellipsis", reverse = reverse)
		return self

	def print(self):
		print(self)
		return self

	def __repr__(self):
		returntext = "_______________\ntable '{}':\n".format(self.name if self.name != None else "<unnamed>")
		for i in self.order:
			for j in self.types:
				if i == j:
					returntext += j.ljust(constants.printcolumnwidth+1)
		returntext += "\n\n"
		for i in self.selection:
			for j in self.order:
				for key,item in i.items():
					if key == j:
						returntext += self.types[key].repr(item)
						returntext += " "
			returntext += "\n"
		returntext += "_______________\n"
		return returntext