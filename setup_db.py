import sqlite3

# Connect to the database
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Insert data into states table
states = [('New York',), ('California',), ('Texas',)]
cursor.executemany("INSERT INTO states (state_name) VALUES (?)", states)

# Insert data into breaches table
breaches = [
    (1, 'Breach A in New York'),
    (1, 'Breach B in New York'),
    (2, 'Breach A in California'),
    (3, 'Breach A in Texas')
]
cursor.executemany("INSERT INTO breaches (state_id, breach_name) VALUES (?, ?)", breaches)

# Insert data into breach_details table
breach_details = [
    (1, 'Details of Breach A in New York'),
    (2, 'Details of Breach B in New York'),
    (3, 'Details of Breach A in California'),
    (4, 'Details of Breach A in Texas')
]
cursor.executemany("INSERT INTO breach_details (breach_id, detail) VALUES (?, ?)", breach_details)

# Commit the changes and close the connection
conn.commit()
conn.close()
