# Log Analysis Project:
This project requires analysing sql database data from a mock newspaper site.
The database contains newspaper articles, as well as the web server log for the site.
Data is evaluated to answer the following questions:

* What are the most popular three articles of all time?

* Who are the most popular article authors of all time?

* On which days did more that 1% of requests lead to errors?

The implementation requires connecting to the sql database using python and then finding the answers via sql queries.


# Installation and Setup:

A linux based virtual machine is required. See instructions on install [here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)   

To bring the virtual machine online use commands '''vagrant up''' and ''' vagrant ssh'''

## Download the data:

The sql data can be downloaded from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
You will need to unzip this file after downloading it. The file inside is called '''newsdata.sql'''. Put this file into the '''vagrant''' directory, which is shared with your virtual machine.

To load the data, '''cd''' into the '''vagrant''' directory and use the command '''psql -d news -f newsdata.sql'''. 
The database includes three tables:

* The authors table includes information about the authors of articles.
* The articles table includes the articles themselves.cd 
* The log table includes one entry for each time a user has accessed the site.

## Create the following views:

'''Add views info'''
Press '''CTRL-D''' to log out of psql.

## Running the python code:

Copy the python file: '''news_data_analysis.py''' to the same '''vagrant''' directory, which is shared with your virtual machine.
log into the virtual machine if disconnected and '''cd''' into the '''vagrant''' directory.
Type the following command: '''python news_data_analysis.py''' to run the python script and produce the output i.e. the answers to the questions.

**Note**: Python version 3 needs to be installed along with the psycopg2 module for python. Download [python 3](https://www.python.org/downloads/). 
Run command '''pip install psycopg2''' in command shell to install psycoppg2 module.
