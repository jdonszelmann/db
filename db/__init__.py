from .setup import *
from .types import *
from .constants import *
from .table import load

log("starting database...",importance=1)

import os
path = os.path.dirname(os.path.realpath(__file__))

def exit_function():
	from .constants import _save, _silent
	if _save:
		for i in opened_tables:
			log("saving table {}".format(i.name),importance=1)
			try:
				i.save()
			except Exception as e:
				log("could not save table {} ({})".format(i.name, e),importance=2)
				False
		log("closing database",importance=1)
	else:
		log("closing database (NOT saving)",importance=1)

import atexit
atexit.register(exit_function)