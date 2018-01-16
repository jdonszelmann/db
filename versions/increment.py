import db
db.silent(True)

if not db.exists("./version"):
	class setup1(db.db):
		setup = {
			"major":db.number(),
			"middle":db.number(),
			"minor":db.number(),
		}
		name = "version"
	table1 = setup1()
	table1.new_record(major=0,middle=0,minor=0)
	table1.save("version")

table1 = db.load("version")

version = table1.query().get()
print(version)
print("version {}.{}.{}".format(version["major"],version["middle"],version["minor"]))
print("update major [0]")
print("update middle [1]")
print("update minor [2]")
print("reset [3]")
while True:
	i = int(input(">>>"))
	if i in [0,1,2]:
		if i == 0:
			version["major"] += 1
		elif i == 1:
			version["middle"] += 1		
		elif i == 2:
			version["minor"] += 1
		elif i == 3:
			version["middle"] = 0		
			version["minor"] = 0
			version["major"] = 0
		break
print("version {}.{}.{}".format(version["major"],version["middle"],version["minor"]))
table1 = table1.query().delete().done()
table1.new_record(version)
table1.save("version")
db.silent(False)
