# python db


this library is used to generate database structures, to save/load them from disk and to search through the data in the databases.

## usage:

import the library
```python
import db
```
create a setup class
```python
class setup1(db.db):
    #setup entry is required
    setup = {
        "id":db.unique(), #generates a unique id for this field, every time a record is added
        "name":db.short_text(), #shor texts support lengths upto 128 characters
        "adult":db.yesno(), #basically bools
    }
    #order entry is not required
    order = [
        "id",
        "name",
        "adult",
    ]
    #order entry is not required but adviced. a primary key may not be omitted when
    #inserting a record
    primarykey = ["id"]

    #name may be omitted but is usefull
    name = "names"
```

