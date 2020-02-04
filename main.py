import mysql.connector

connection = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)
cursor = connection.cursor()
word = input("ENTER A WORD...\n")


query = cursor.execute("SELECT * FROM Dictionary WHERE Expression= '%s'" % word)
results = cursor.fetchall()
if results:
    for item in results:
        print(item[1])
else:
    print("Word not found, please try again!")