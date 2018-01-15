from .setup import *
from .types import *
from .constants import *
from .table import load

log("save-on-exit is set to {}".format(save), importance=1)
if debug: log("debug is set to True", importance=1)

def exit_function():
	if save:
		for i in opened_tables:
			log("saving table {}".format(i.name),importance=1)
			try:
				i.save()
			except Exception as e:
				log("could not save table {} ({})".format(i.name, e),importance=2)
				False
	log("closing database",importance=1)

import atexit
atexit.register(exit_function)