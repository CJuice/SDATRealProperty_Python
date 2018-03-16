"""Python version of the Real Property data process"""
# IMPORTS

# VARIABLES
    # See ProcessVariables.py

# LOCAL FUNCTIONS

# CLASSES
    # See RecordClass

# FUNCTIONALITY
    # Get the input files (SDAT & MDP) to process
        # using input() OR
        # iterate through all counties using a directory and a collection of the file pairings
    # Read the SDAT file
        # load the records into sql database table
        # create RecordClass Objects (while data is going into database table or afterward?)
    # Put both datasources into database tables
        # Option 1:
            # instead of joining the tables, use the AccountID to query the MDP data for the relevant record.
                # QUESTION: Is indexing automatic or do I need to create this
        # Option 2:
            # perform the joining of the two tables like the current FME process
            # Prep the SDAT file for joining by creating the Account ID
    # Build the Account ID's
        # Handle baltimore city special functionality


# DELETIONS & CLEANUP

if __name__ == "__main__":
    print("in main")
