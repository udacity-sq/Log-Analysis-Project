#! /usr/bin/python
# "Database code" for the DB news.

import psycopg2


DBNAME = "news"


def get_query_results(query):
    # connect to database and return query results
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows


def popular_articles():
    # find the 3 most popular articles - sum up views of the articles
    print("\n")
    print("Query returns the most popular articles of all time:")
    query = """
          select title, total_views, 'views' as views
          from articles join total_views on articles.slug = total_views.slug
          order by total_views DESC limit 3;
          """
    popular_articles = get_query_results(query)
    for title, total_views, unused in popular_articles:
        print(" {} - {} views".format(title, total_views))


def most_popular_authors():
    # find the most popular authors based on views
    print("\n")
    print("Query returns the most popular authors of all time:")
    query = """
          select name, sum(total_views) as author_views, 'views' as views
          from most_popular
          group by name
          order by author_views DESC;
          """
    popular_authors = get_query_results(query)
    for name, author_views, unused in popular_authors:
        print(" {} - {} views".format(name, author_views))


def percent_error():
    # find the days when more than 1% of requests led to errors
    print("\n")
    print("Query returns days when more than 1% of requests led to errors:")
    query = """
           select DISTINCT to_char(time_pst, 'FMMONTH FMDD,YYYY') as day,
           percent_error from daily join percent_error
           on daily.day = percent_error.day
           where percent_error.percent_error >1;
           """
    percent_error = get_query_results(query)
    for day, pct in percent_error:
        print(" {} - {}% errors".format(day, round(pct, 2)))


if __name__ == "__main__":
    popular_articles()
    most_popular_authors()
    percent_error()
