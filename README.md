# Log-Analysis
* An internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
* The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. 

**Description**
* Practice interacting with a live database both from the command line and from your code.
* Explore a large database with over a million rows.
* Build and refine complex queries and use them to draw business conclusions from data.

***Report generation***
Building an informative summary from logs is a real task that comes up very often in software engineering. For instance, at Udacity we collect logs to help us measure student progress and the success of our courses. The reporting tools we use to analyze those logs involve hundreds of lines of SQL.

***Database as shared resource***
In this project, we'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

# Assignment

Need To answer the following Questions :

    1.What are the most popular three articles of all time?
    2.Who are the most popular article authors of all time?
    3.On which days did more than 1% of requests lead to errors?

# How to Run
    1.Navigate to ```cd /vagrang```
    2.Enter ```psql```
    3.connect to the database with \c news
    4.Enter any view from which mentioned
    5.Exit by ```psql```
