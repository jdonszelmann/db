import db

class setup1(db.db):
	setup = {
		"id":db.unique(),
		"name":db.short_text(),
		"adult":db.yesno(),
	}
	order = [
		"id",
		"name",
		"adult",
	]
	primarykey = ["id"]
	name = "names"

class setup2(db.db):
	setup = {
		"id":db.unique(),
		"name":db.short_text(),
		"adult":db.yesno(),
	}
	order = [
		"id",
		"name",
		"adult",
	]
	primarykey = ["id"]
	name = "names"

table1 = setup1()

table1.new_record({"id":db.auto,"name":"jonathan","adult":False})
table1.new_record({"id":db.auto,"name":"stef","adult":False})
table1.new_record({"id":db.auto,"name":"philip","adult":True})
table1.new_record({"id":db.auto,"name":"romualdo","adult":True})
table1.new_record({"id":db.auto,"name":"noah","adult":True})
table1.new_record({"id":db.auto,"name":"chris","adult":False})

name = table1.save()
table1 = db.load(name)

res1 = table1.query()					\
	.where("adult",True,db.equals)		\
	.delete()							\
	.getcol("name")

name = table1.exportto()
table1 = setup2.importfrom()  

print(res1)