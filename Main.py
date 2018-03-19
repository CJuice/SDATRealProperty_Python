"""Python version of the Real Property data process"""
# IMPORTS
import ProcessVariables
import RecordClass
import os
# VARIABLES
    # See ProcessVariables.py

# LOCAL FUNCTIONS
def filereader(filepath, func):
    counter = 0
    with open(filepath,'r') as fhand:
            for line in fhand:
                if counter < 2:
                    func(line)
                    counter+=1
                else:
                    break

def split_SDAT_line(line):
    index = 0
    line_parts = []
    for item in ProcessVariables.SDAT_DATA_SPLIT_SPACE_DELIMITED_INDICES:
        old_index = index
        current_index = old_index + item
        line_parts.append(line[old_index:current_index])
        index = current_index
        # print(index)
    print(line_parts)
# CLASSES
    # See RecordClass.py

# FUNCTIONALITY
def mainfunction():
    # Get the input files (SDAT & MDP) to process
        # using input() OR
        # iterate through all counties using a directory and a collection of the file pairings
    testing_root_data_path = r"E:\DoIT_SDATRealProperty_Project\RealPropAllData"
    for pair in ProcessVariables.SDAT_TO_MDP_DATA_FILES_MAPPING:
        print(pair)
        assert os.path.exists(os.path.join(testing_root_data_path,pair[0]))
        assert os.path.exists(os.path.join(testing_root_data_path,pair[1]))

        # Read the SDAT data file
            # load the records into sql database table
            # create RecordClass Objects (while data is going into database table or afterward?)
        filereader(os.path.join(testing_root_data_path,pair[0]), split_SDAT_line)
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
    mainfunction()
