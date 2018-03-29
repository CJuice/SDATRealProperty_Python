import ProcessVariables
import sqlite3
import os
import shutil
import logging
import datetime


def print_and_log(date_time, message, log_level):
    """
    Print and log any provided message based on the indicated logging level.
    :param message:
    :param log_level:
    :return:
    """
    message = str(message).rstrip("\n")
    if log_level is ProcessVariables.INFO_LEVEL:
        logging.info("{} : {}".format(date_time, message))
    elif log_level is ProcessVariables.WARNING_LEVEL:
        logging.warning("{} : {}".format(date_time, message))
    elif log_level is ProcessVariables.ERROR_LEVEL:
        logging.error("{} : {}".format(date_time, message))
    print("{} : {}".format(date_time, message))
    return


def get_datetime_for_logging_and_printing():
    """
    Generate a pre-formatted date and time string for logging and printing purposes.
    :return: String Year/Month/Day Hour:Minute:Second usable in logging, and printing statements if desired
    """
    return '{:%Y/%m/%d %H:%M:%S}'.format(datetime.datetime.now())


# SDAT AND MDP FILE FUNCTIONS
def file_line_reader(filepath):
    with open(filepath, 'r') as fhand:
        for line in fhand:
            line = line.strip()
            yield line


def split_SDAT_line(line, delimeter_list=ProcessVariables.SDAT_DATA_SPLIT_SPACE_DELIMITED_INDICES):
    index = 0
    line_parts = []
    for item in delimeter_list:
        old_index = index
        current_index = old_index + item
        data = line[old_index:current_index]
        line_parts.append(data.strip())
        index = current_index
    return line_parts


# DATABASE RELATED FUNCTIONS
def copy_template_sqldb_and_create_production_sqldb(template_sqldb_path_tuple, production_sqldb_path_tuple):
    # if exists already, delete to avoid error
    try:
        if not os.path.exists(production_sqldb_path_tuple[0]) and os.path.exists(template_sqldb_path_tuple[0]):
            shutil.copyfile(template_sqldb_path_tuple[0], production_sqldb_path_tuple[0])
        elif os.path.exists(production_sqldb_path_tuple[0]) and os.path.exists(template_sqldb_path_tuple[0]):
            os.remove(production_sqldb_path_tuple[0])
            shutil.copyfile(template_sqldb_path_tuple[0], production_sqldb_path_tuple[0])
        elif not os.path.exists(template_sqldb_path_tuple[0]):
            print("the template sqlite3 db doesn't exist")
            exit()
        else:
            print("in copy_template_sqldb_and_create_production_sqldb else clause. what happened?")
    except Exception as e:
        print("in copy_template_sqldb_and_create_production_sqldb except clause. what happened?")
        print(e)
        exit()
    return


def insert_record_into_table(cursor, table_name_tuple, field_names_tuple, field_values_tuple):
    field_names_dict = dict(field_names_tuple)
    field_values_dict = dict(field_values_tuple)
    sql_insert_string = ProcessVariables.SQL_INSERT_STRING_PART_1of3[0].format(table_name=table_name_tuple[0]) + \
                        ProcessVariables.SQL_INSERT_STRING_PART_2of3[0].format(**field_names_dict) + \
                        ProcessVariables.SQL_INSERT_STRING_PART_3of3[0].format(**field_values_dict)
    print(sql_insert_string)
    try:
        cursor.execute(sql_insert_string)
    except sqlite3.IntegrityError:
        print_and_log(date_time=get_datetime_for_logging_and_printing(),
                      message='ERROR: ID already exists in PRIMARY KEY column {}'.format("ACCTID"),
                      log_level=ProcessVariables.ERROR_LEVEL)
    # "INSERT INTO {table_name} ({ACCTID}, {JURSCODE}, {DIGXCORD}, {DIGYCORD}, {RESITYP}, {ADDRESS}, {STRTUNT}, {CITY}, {ZIPCODE}, {LEGAL1}, {SDATWEBADR}, {EXISTING}) VALUES ({acctid}, {jurscode}, {digxcord}, {digycord}, {resityp}, {address}, {strtunt}, {city}, {zipcode}, {legal1}, {sdatwebadr}, {existing})"

# def delete_file(path):
# #if exists already, delete to avoid error
#     if os.path.exists(path):
#         os.remove(path)
#         print("removed")
#     return
# def create_sqlite3_table(database_path):
#     conn = sqlite3.connect((database_path))
#     conn.close()
#     return
#
# def add_table_to_sqlite3_database(database_path, table_name_tuple):
#     conn = sqlite3.connect((database_path))
#     conn.execute("CREATE TABLE {table_name}".format(table_name=table_name_tuple[0]))
#     conn.commit()
#     conn.close()
#     return
#
# def add_field_to_sqlite3_database(database_path, table_name_tuple, field_names_tuple, field_type_tuple, primary_key_boolean):
#     conn = sqlite3.connect((database_path))
#     conn.execute(
#         "ALTER TABLE {table_name} ADD COLUMN '{new_field}' {field_type} {primary_key})".format(
#             table_name=table_name_tuple[0],
#             new_field=field_names_tuple[0],
#             field_type=field_type_tuple[0],
#             primary_key=primary_key_boolean))
#     conn.commit()
#     conn.close()
#     return
