import pymysql
import pymysql.cursors
# pymysql.connect()

connection=pymysql.connect(
    host="10.100.33.60",
    user="aokagejasmin",
    password="220221337",
    database="world",
    cursorclass=pymysql.cursors.DictCursor
)


cursor=connection.cursor()

cursor.execute("SELECT * FROM `country`")


result= cursor.fetchall()

print(type(result))
print(result[3] ['HeadOfState'])
