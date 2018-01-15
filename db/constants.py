

class auto:
	def __init__(self):
		log("do NOT initialize this class", print_log=False, importance=5)

class all:
	def __init__(self):
		log("do NOT initialize this class", print_log=False, importance=5)

printcolumnwidth = 20

equals = lambda x,y:x==y
notequals = lambda x,y:x!=y
contains = lambda x,y:x in y

logging_importance = 1

debug = True
_silent = False

def toggle_debug(setter=None):
	global debug
	if type(setter) == bool: log("debug must be bool",importance=6)
	if setter != None:
		debug = setter
	debug = not debug

def silent(setter=None):
	global _silent
	if type(setter) == bool: log("debug must be bool",importance=6)
	if setter != None:
		_silent = setter
	_silent = not debug

save = True
def toggle_save(setter=None):
	global debug
	if type(setter) == bool: log("debug must be bool",importance=6)
	if setter != None:
		debug = setter
	debug = not debug