"""Python version of the Real Property data process"""
# IMPORTS

# VARIABLES
    # See ProcessVariables.py
# FUNCTIONS

# CLASSES
    # Record Class
        # Contains all variables and meaningful fields. Does not contain unused data from files
# FUNCTIONS

# FUNCTIONALITY
    # Get the input files (SDAT & MDP) to process
        # using input() OR
        # iterate through all counties using a directory and a collection of the file pairs
    # Create a sql database
    # Prep the SDAT file for joining by creating the Account ID
    # Read the records from the files and store in db
    # Join the files together based on the ID

if __name__ == "__main__":
    print("in main")
