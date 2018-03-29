# http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
import sqlite3
import os
import shutil

sqlite_file = r"E:\DoIT_SDATRealProperty_Project\SDATRealProperty_PythonProducts\my_test_db_template.sqlite"
sqlite_file_newname = r"E:\DoIT_SDATRealProperty_Project\SDATRealProperty_PythonProducts\my_test_db_production.sqlite"
# SDAT_table = ("SDAT",)
MDP_table = ("MDP",)
accountID_field = ("ACCTID",)
accountID_field_type = ("INTEGER",)
MDP_column_specs_dictionary = {'JURSCODE': 'TEXT', 'ACCTID': 'INTEGER', 'DIGXCORD': 'REAL', 'DIGYCORD': 'REAL',
                               'RESITYP': 'TEXT', 'ADDRESS': 'TEXT', 'STRTUNT': 'TEXT', 'CITY': 'TEXT',
                               'ZIPCODE': 'TEXT', 'LEGAL1': 'TEXT', 'SDATWEBADR': 'TEXT', 'EXISTING': 'TEXT'}


# conn = None

def copy_template_database():
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
    print("Copying {} to {} complete".format(os.path.basename(sqlite_file), os.path.basename(sqlite_file_newname)))


def create_new_database():
    # create new database
    conn = sqlite3.connect((sqlite_file))
    print("{} database created".format(sqlite_file))

    # Create tables
    # conn.execute("CREATE TABLE {table_name} ({new_field} {field_type} PRIMARY KEY)".format(table_name=SDAT_table[0],new_field=accountID_field[0],field_type=accountID_field_type[0]))
    conn.execute("CREATE TABLE {table_name} ({new_field} {field_type} PRIMARY KEY)".format(table_name=MDP_table[0],
                                                                                           new_field=accountID_field[0],
                                                                                           field_type=
                                                                                           accountID_field_type[0]))
    for key,value in MDP_column_specs_dictionary.items():
        if key == "ACCTID":
            pass
        else:
            conn.execute("ALTER TABLE {table_name} ADD COLUMN {new_field} {field_type}".format(table_name=MDP_table[0], new_field=key, field_type=value))

    # If made changes to database then need to commit
    conn.commit()

    # If nothing more than queries, can close without committing
    conn.close()


if __name__ == "__main__":
    create_new_database()
    copy_template_database()
