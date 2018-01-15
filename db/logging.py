from . import constants
from . import colorama
colorama.init(autoreset=True)

def log(message,importance=constants.logging_importance, print_log=True):
	if not constants._silent and importance < 6:
		if print_log:
			if importance == 0 and constants.debug:
				print("log: " + message)
			elif importance == 1 and constants.debug:
				print(colorama.Fore.GREEN + "log (notice): " + message)
			elif importance == 2 and constants.debug:
				print(colorama.Fore.YELLOW + "log (warning): " + message)
			elif importance == 3 and constants.debug:
				print(colorama.Fore.RED + "log (error): " + message)
			elif importance == 4:
				print(colorama.Style.BRIGHT + colorama.Fore.GREEN + "log (critical notice): " + message)
			elif importance == 5:
				print(colorama.Style.BRIGHT + colorama.Fore.YELLOW + "log (critical warning): " + message)
			elif importance == 6:
				print(colorama.Style.BRIGHT + colorama.Fore.RED + "log (fatal error): " + message)
				raise SystemExit()
			elif importance == 7:
				print(colorama.Back.RED + colorama.Fore.GREEN + message)
				raise SystemExit()
			elif importance == 8:
				print(colorama.Back.RED + colorama.Fore.YELLOW + message)
				raise SystemExit()
			elif importance == 9:
				print(colorama.Back.RED + colorama.Fore.RED + message)
				raise SystemExit()
		else:
			if importance == 0:
				return message
			elif importance == 1:
				return colorama.Fore.GREEN + "log (notice): " + message
			elif importance == 2:
				return colorama.Fore.YELLOW + "log (warning): " + message
			elif importance == 3:
				return colorama.Fore.RED + "log (error): " + message
			elif importance == 4:
				return colorama.Style.BRIGHT + colorama.Fore.GREEN + "log (critical notice): " + message
			elif importance == 5:
				return colorama.Style.BRIGHT + colorama.Fore.YELLOW + "log (critical warning): " + message
			elif importance == 6:
				return colorama.Style.BRIGHT + colorama.Fore.RED + "log (fatal error): "+ message
			elif importance == 7:
				return colorama.Back.GREEN + colorama.Fore.GREEN + message
			elif importance == 8:
				return colorama.Back.YELLOW + colorama.Fore.YELLOW + message
			elif importance == 9:
				return colorama.Back.RED + colorama.Fore.RED + message

def abort():
	raise SystemExit(log("",print_log=False,importance=6))

def logging_increment(value=1):
	constants.logging_importance += value

def logging_decrement(value=1):
	constants.logging_importance -= value