
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