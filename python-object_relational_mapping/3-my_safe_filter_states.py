import MySQLdb
import sys

def search_states(username, password, database, state_name):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )

        # Create a cursor object
        cursor = db.cursor()

        # Defining the SQL query with a parameterized query
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

        # Execute the SQL query with the parameter
        cursor.execute(query, (state_name,))

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Display the results in the correct format
        for row in rows:
            state_id, state_name = row
            print("({}, '{}')".format(state_id, state_name))

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
    finally:
        # Close the cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 5:
        print(
            "Usage: python 3-my_safe_filter_states.py <username> <password>" 
            "<database> <state_name>"
            )
        sys.exit(1)

    # Get the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the search_states function with safe parameterized query
    search_states(username, password, database, state_name)
