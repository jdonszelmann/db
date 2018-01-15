

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

logging_importance = 0

debug = True

def toggle_debug(setter=None):
	global debug
	if type(setter) == bool: log("debug must be bool",importance=6)
	if setter != None:
		debug = setter
	debug = not debug

save = True
def toggle_save(setter=None):
	global debug
	if type(setter) == bool: log("debug must be bool",importance=6)
	if setter != None:
		debug = setter
	debug = not debug