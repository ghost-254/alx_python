#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to retrieve cities by state, sorted by cities.id
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id"
    )

    # Fetch and print the results
    for row in cursor.fetchall():
        print(row)

    # Close the database connection
    db.close()
