#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    username, password, database, state_name = sys.argv[1:5]

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

    # Execute the SQL query to retrieve cities for the given state, sorted by cities.id
    cursor.execute(
        "SELECT cities.name "
        "FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id",
        (state_name,)
    )

    # Fetch and print the results as a comma-separated string
    cities = [row[0] for row in cursor.fetchall()]
    if cities:
        print(", ".join(cities))

    # Close the database connection
    db.close()
