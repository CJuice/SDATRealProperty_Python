"""Python version of the Real Property data process"""
# IMPORTS
import ProcessVariables
import ProcessFunctions
import RecordClass
import os
import sqlite3
import timeit
import logging
from collections import OrderedDict

# VARIABLES
# See ProcessVariables.py

# LOCAL FUNCTIONS
# see ProcessFunctions.py

# CLASSES
# See RecordClass.py

# LOGGING
logging.basicConfig(filename=ProcessVariables.LOG_FILENAME, level=logging.INFO)


# FUNCTIONALITY
def mainfunction():
    ProcessFunctions.print_and_log(date_time=ProcessFunctions.get_datetime_for_logging_and_printing(),
                                   message=ProcessVariables.INITIATED_PROCESSING,
                                   log_level=ProcessVariables.INFO_LEVEL)

    # iterate through all counties using a directory and a collection of the file pairings
    for pair_of_files in ProcessVariables.SDAT_TO_MDP_DATA_FILES_TUPLE:
        print(pair_of_files)
        assert os.path.exists(os.path.join(ProcessVariables.testing_root_data_path, pair_of_files[0]))
        assert os.path.exists(os.path.join(ProcessVariables.testing_root_data_path, pair_of_files[1]))

        # Create database for county of focus and establish connection and cursor
        ProcessFunctions.copy_template_sqldb_and_create_production_sqldb(
            template_sqldb_path_tuple=ProcessVariables.SQLITE3_TEMPLATE_DATABASE_PATH,
            production_sqldb_path_tuple=ProcessVariables.SQLITE3_PRODUCTION_DATABASE_PATH)
        connection_to_production_database = sqlite3.connect(ProcessVariables.SQLITE3_PRODUCTION_DATABASE_PATH[0])
        connection_to_production_database_cursor = connection_to_production_database.cursor()

        # MDP data file
        full_path_to_MDP_file = os.path.join(ProcessVariables.testing_root_data_path, pair_of_files[1])
        MDP_line_generator = ProcessFunctions.file_line_reader(full_path_to_MDP_file)
        counter_mdp = 0
        local_MDP_field_index_dictionary = OrderedDict(ProcessVariables.MDP_FIELDS_OF_INTEREST_AND_INDEX_TUPLE)
        for MDP_Gen_Line in MDP_line_generator:
            MDP_line_data_list = MDP_Gen_Line.split(",")

            # Work on Headers
            if counter_mdp > 0:
                pass
            else:
                # Get the index position of the MDP fields of interest, from the headers, in the full MDP dataset
                # Could hardcode this inventory but wanted to build in flexibility if field order changes
                for key in local_MDP_field_index_dictionary.keys():
                    assert key in MDP_line_data_list
                    local_MDP_field_index_dictionary[key] = MDP_line_data_list.index(key)
                # print("Dictionary of MDP index positions for important fields: \n{}".format(local_MDP_field_index_dictionary)) #TESTING
                counter_mdp += 1
                continue
            print("should only show when counter_mdp > 0...counter_mdp={}".format(counter_mdp))

            # Work on Data
            # NOTE: Primary key has a database index by default
            # Build list of field name and field value pairs as tuples in a list
            field_names_tuple = tuple([(key,key) for key in local_MDP_field_index_dictionary.keys()])
            field_values_tuple = tuple([(str(key).lower(),MDP_line_data_list[value]) for key,value in local_MDP_field_index_dictionary.items()])
            ProcessFunctions.insert_record_into_table(cursor=connection_to_production_database_cursor,
                                                      table_name_tuple=ProcessVariables.MDP_TABLE_NAME,
                                                      field_names_tuple=field_names_tuple,
                                                      field_values_tuple=field_values_tuple)
            #STOPPED
            #TODO: Record contained an empty value and the sql fails. need to deal with nulls in data entry
            if counter_mdp > 0 and counter_mdp % 10000 == 0:
                connection_to_production_database.commit()
                ProcessFunctions.print_and_log(
                    date_time=ProcessFunctions.get_datetime_for_logging_and_printing(),
                    message=ProcessVariables.DATABASE_COMMIT_SDAT.format(counter_mdp),
                    log_level=ProcessVariables.INFO_LEVEL)
            counter_mdp += 1
        # commit an remaining records
        connection_to_production_database.commit()
        break

        # SDAT data file. Will not be putting the data into a db.
        counter_SDAT = 0
        full_path_to_SDAT_file = os.path.join(ProcessVariables.testing_root_data_path, pair_of_files[0])
        SDAT_line_generator = ProcessFunctions.file_line_reader(full_path_to_SDAT_file)
        for SDAT_Gen_Line in SDAT_line_generator:
            SDAT_line_data_list = ProcessFunctions.split_SDAT_line(SDAT_Gen_Line)
            SDAT_record_object = RecordClass.RecordClass(SDAT_line_data_list)
            # TODO: Select data from MDP table and pair with SDAT data in object
            # TODO: put record objects into queue. When queue exceeds a size, put objects into database and empty queue.
            # TODO: use multi-thread and have workers
            ProcessFunctions.insert_record_into_table(cursor=connection_to_production_database_cursor,
                                                      table_name_tuple=ProcessVariables.SDAT_TABLE_NAME,
                                                      column_name_tuple=ProcessVariables.ACCOUNTID_FIELD,
                                                      record_value=SDAT_record_object.account_id_from_SDAT_concat_no_leading_zeros)
            if counter_SDAT > 0 and counter_SDAT % 10000 == 0:
                connection_to_production_database.commit()
                ProcessFunctions.print_and_log(
                    date_time=ProcessFunctions.get_datetime_for_logging_and_printing(),
                    message=ProcessVariables.DATABASE_COMMIT_SDAT.format(counter_SDAT),
                    log_level=ProcessVariables.INFO_LEVEL)
                counter_SDAT += 1
        connection_to_production_database.commit()
        ProcessFunctions.print_and_log(
            date_time=ProcessFunctions.get_datetime_for_logging_and_printing(),
            message=ProcessVariables.DATABASE_COMMIT_SDAT.format(counter_SDAT),
            log_level=ProcessVariables.INFO_LEVEL)
        connection_to_production_database.close()

        # TODO: remove break once can process every pair of files
        break

        # Put both datasources into database tables
        # Option 1:
        # Instead of joining the tables, use the AccountID to query the MDP data for the relevant record.
        # QUESTION: Is indexing automatic or do I need to create this?
        # Option 2:
        # perform the joining of the two tables like the current FME process
        # Prep the SDAT file for joining by creating the Account ID
        # Build the Account ID's
        # Handle baltimore city special functionality
        # Reproject lat/lon
        # IMPS string update
        # Make FINDER link
        # handle empty data links
        # Make Google link
        # handle empty data links
        # Map county code to county name string
        # Clean dashes from CurCycleData_LandValue
        # Dwelling Construction Code to string replacement value
        # TypeStyle_Res to string replacement values
        # TypeStyle_Comm to string replacement values
        # CND to string replacement values
        # MH1 to string replacement values
        # Map Dwelling Story code to values
        # Map Dwelling Type code to values
        # Switch owner data for PG County
        # Dwelling Grade to string replacement values
        # Dwelling Condition to string replacement values
        # Map Land Use codes to values
        # Montgomery County data error catching
        # Map Exempt Class codes to values
        # Map Property Factor codes to values
        # Chunks functionality
        #


# DELETIONS & CLEANUP

if __name__ == "__main__":
    print("in main")
    start = timeit.default_timer()
    mainfunction()
    print("Took: {} seconds".format(timeit.default_timer() - start))
