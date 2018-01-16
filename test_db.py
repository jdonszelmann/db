import db
db.toggle_save(False)

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

table1 = setup1()

table1.new_record({"id":db.auto,"name":"jonathan","adult":False})
table1.new_record({"id":db.auto,"name":"stef","adult":False})
table1.new_record({"id":db.auto,"name":"philip","adult":True})
table1.new_record({"id":db.auto,"name":"romualdo","adult":True})
table1.new_record({"id":db.auto,"name":"noah","adult":True})
table1.new_record({"id":db.auto,"name":"chris","adult":False})
table1.new_record({"id":db.auto,"name":"marco","adult":False})

res1 = table1.query()					\
	.where("adult",True,db.equals)		\
	.delete()							\
	.done()

print(res1)