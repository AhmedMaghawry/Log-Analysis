#! /usr/bin/env python
import psycopg2

def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("There is an error while connecting")

def execute_query(query):
    db, cursor = connect()
    cursor.execute(query)
    return db, cursor;

db, c = execute_query(
"SELECT title, count(*) as viewers FROM articles,"
"log WHERE articles.slug = substring(log.path, 10) "
"GROUP BY title ORDER BY viewers DESC LIMIT 3;"
);
articles = c.fetchall()

print "What are the most popular three articles of all time? Answer is :\n"
for article in articles:
    print article[0], "-----", article[1], "views"
db.close()

db, c = execute_query(
"SELECT authors.name, count(*) as viewers FROM "
"articles JOIN authors on articles.author = authors.id "
"JOIN log on articles.slug = substring(log.path, 10) "
"WHERE log.status LIKE '200 OK' GROUP BY authors.name "
"ORDER BY viewers DESC;");
articles = c.fetchall()

print "Who are the most popular article authors of all time? Answer is :\n"
for article in articles:
    print " ", article[0], "-", article[1], "views"
db.close()

db, c = execute_query(
"SELECT to_char(errors.date, 'Mon DD, YYYY'), "
"round( cast(errors.percent as numeric), 3) "
"FROM total,errors;");
days = c.fetchall()

print "On which days did more than 1% of requests lead to errors?Answer is :\n"
for day in days:
    print " ", day[0], "-", day[1], "%"
db.close()
