# http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
import sqlite3
import os
import shutil
sqlite_file = r"E:\DoIT_SDATRealProperty_Project\SDATRealProperty_PythonProducts\my_test_db.sqlite"
sqlite_file_newname = r"E:\DoIT_SDATRealProperty_Project\SDATRealProperty_PythonProducts\my_test_db_99.sqlite"
SDAT_table = ("SDAT",)
MDP_table = ("MDP",)
accountID_field = ("ACCTID",)
accountID_field_type = ("INTEGER",)

# conn = None

# if exists already, delete to avoid error
if not os.path.exists(sqlite_file_newname) and os.path.exists(sqlite_file):
    # os.remove(sqlite_file)
    # print("removed")
    shutil.copyfile(sqlite_file, sqlite_file_newname)
elif os.path.exists(sqlite_file_newname) and os.path.exists(sqlite_file):
    os.remove(sqlite_file_newname)
    shutil.copyfile(sqlite_file, sqlite_file_newname)
elif not os.path.exists(sqlite_file):
    print("the template sqlite3 db doesn't exist")
    exit()
else:
    print("in else clause. what happened?")
exit()
# create new database
# conn = sqlite3.connect((sqlite_file))
# print("database created")
conn = sqlite3.connect((sqlite_file_newname))

# Create tables
# conn.execute("CREATE TABLE {table_name} ({new_field} {field_type} PRIMARY KEY)".format(table_name=SDAT_table[0],new_field=accountID_field[0],field_type=accountID_field_type[0]))
# conn.execute("CREATE TABLE {table_name} ({new_field} {field_type} PRIMARY KEY)".format(table_name=MDP_table[0],new_field=accountID_field[0],field_type=accountID_field_type[0]))


# If made changes to database then need to commit
conn.commit()

# If nothing more than queries, can close without committing
conn.close()