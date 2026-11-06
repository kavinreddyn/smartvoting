import sqlite3 # Import the tool needed to work with the SQLite database

def add_sample_voters(): # Create a new function called add_sample_voters
    # 1. Connects to election.db using sqlite3
    conn = sqlite3.connect('election.db') # Connect to the database file named 'election.db'
    cursor = conn.cursor() # Create a cursor to let us send commands to the database

    # Sample voters data: (aadhaar, voter_id)
    sample_data = [ # Create a list to hold all the sample voter information
        ("641654244864", "ABC1234567"), # Define the Aadhaar and voter ID for the first person
        ("987654321098", "XYZ7654321"), # Define the Aadhaar and voter ID for the second person
        ("918660313667", "KA11223334"), # Define the Aadhaar and voter ID for the third person
        ("998877665544", "UVW9988776"), # Define the Aadhaar and voter ID for the fourth person
        ("556677889900", "GHI5566778"), # Define the Aadhaar and voter ID for the fifth person
        ("443322110099", "RST4433221"), # Define the Aadhaar and voter ID for the sixth person
        ("102030405060", "JKL1020304"), # Define the Aadhaar and voter ID for the seventh person
        ("605040302010", "OPQ6050403"), # Define the Aadhaar and voter ID for the eighth person
        ("135792468013", "MNO1357924"), # Define the Aadhaar and voter ID for the ninth person
        ("246801357924", "LMN2468013") # Define the Aadhaar and voter ID for the tenth person
    ] # Close the list of sample data

    # 4. Use INSERT OR IGNORE so duplicates do not cause errors.
    cursor.executemany('''
        INSERT OR IGNORE INTO voters (aadhaar, voter_id)
        VALUES (?, ?)
    ''', sample_data) # Give the database a command to insert all of our sample data

    conn.commit() # Save the changes permanently into the database file
    conn.close() # Close the connection to the database since we are done

    # 5. Print "Sample voters added successfully." after inserting.
    print("Sample voters added successfully.") # Display a success message on the screen

if __name__ == "__main__": # Check if this file is being run directly by the user
    add_sample_voters() # Run the previously defined function
