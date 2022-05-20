# Data Modeling wit PostgresSQL

## Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Running Python Scripts
<ol>
    <li>Open the Terminal</li>
    <li>Type 'python create_tables.py' and press Enter</li>
    <li>Type 'python etl.py' and press Enter</li>
</ol>

## Repository Files
<ol>
    <li><b>create_tables.py</b>: drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.</li>
    <li><b>etl.ipynb</b>: reads and processes a single file from 'song_data' and 'log_data' and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.</li>
    <li><b>etl.py</b>: reads and processes files from 'song_data' and 'log_data' and loads them into your tables. You can fill this out based on your work in the ETL notebook.</li>
    <li><b>README.md</b>: provides discussion on the project.</li>
    <li><b>sql_queries.py</b>:contains all sql queries, and is imported into the last three files above.</li>
    <li><b>test.ipynb</b>: displays the first few rows of each table to let us check on the database.</li>
</ol>

## Database Design

The schema used for this design is the Star Schema. There is one fact table containing all the measures associated with each songplay event, and four dimensional tables that include songs, artists, users and time. Each dimensional table has a primary key that is being referenced in the fact table.

Relational Database rational:

<ul>
    <li>The data types are structured</li>
    <li>The amount of data we need to analyze is not a large dataset</li>
    <li>The relational db strucure enables analysts to aggregate data efficiently</li>
    <li>The need to use JOINS for this scenario</li>
</ul>

### Fact Table
<li><b>songplays</b> - records in log data associated with song plays i.e. records with page NextSong
 <ul><li>songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent</ul></li></li>
 
### Dimension Tables
<ol>
    <li><b>users</b> - users in the app
        <ul><li>user_id, first_name, last_name, gender, level</li></ul></li>
<li><b>songs</b> - songs in music database
    <ul><li>song_id, title, artist_id, year, duration</li></ul></li>
<li><b>artists</b> - artists in music database
    <ul><li>artist_id, name, location, latitude, longitude</li></ul></li>
<li><b>time</b> - timestamps of records in songplays broken down into specific units
    <ul><li>start_time, hour, day, week, month, year, weekday</li></ul></li>    
</ol>