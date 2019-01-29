# Databse code for the project log analysis
# Python 2.7

import datetime
import psycopg2
import bleach


DBNAME = "news"


def displayArticles():
    """Return 3 most famous articles from the news DB, max views first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select title as article, count||' views' as views from (select \
    title,count(*) from articlelog group by 1 order by 2 desc limit 3) \
    as general;")
    articles = c.fetchall()
    db.close()
    print "Articles\t\t\t\tViews"
    for article in articles:
        print article[0], '\t', article[1]


def displayAuthors():
    """Return 3 most famous authors from the news DB, max views first."""

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select name,count||' views' as Views from (select name,count(*)\
     from authorlog group by 1 order by 2 desc limit 3) as general;")
    authors = c.fetchall()
    db.close()
    print "Authors\t\t\t\tViews"
    for author in authors:
        print author[0], '\t\t', author[1]


def displayErrorDays():
    """Return the days where more than 1% of the requests resulted in errors"""

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select ROUND(errorcount::decimal*100/totalcount,2) as \
    percentage,DATE(errorlog.date) from totallog,errorlog where totallog.date \
    =errorlog.date and errorcount::decimal*100/totalcount>=1;")
    errors = c.fetchall()
    db.close()
    print "Percentage\tDate"
    for error in errors:
        print error[0], '\t\t', error[1]


if __name__ == '__main__':
    choice = 1
    while(choice != 4):
        print("\n1. Most popular articles \n2. Most popular authors \
        \n3. Error prone days \n4. Exit\n")
        choice = input('Enter your choice : ')
        if choice == 1:
            displayArticles()
        elif choice == 2:
            displayAuthors()
        elif choice == 3:
            displayErrorDays()
        else:
            break
    print("Thank You for the analysis!")
