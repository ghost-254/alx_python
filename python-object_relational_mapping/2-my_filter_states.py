import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 5:
        print(
            "Usage: python filter_states.py <username> <password>"
            "<database> <state_name>"
        )
        sys.exit(1)

    # Get the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

    # SQL-query to fetch states where the name matches the provided state_name
    query = (
        "SELECT * FROM states WHERE name = %s OR BINARY name = %s "
        "ORDER BY id ASC"
    )
    cursor.execute(query, (state_name,))

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Display the results in the correct format
    for row in rows:
        state_id, state_name = row
        print("({}, '{}')".format(state_id, state_name))

    # Close the cursor and database connection
    cursor.close()
    db.close()
