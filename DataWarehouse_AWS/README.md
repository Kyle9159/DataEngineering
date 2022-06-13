# Project: Data Warehouse with AWS

## Description
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, you are tasked with building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights into what songs their users are listening to. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Usage

### create_tables.py
This script must be run first. Connects to redshift and drops any existing tables if they exist, then creates `staging_events`, `staging_songs`, `ft_songplay`, `dt_artists`,`dt_songs`, `dt_time`, and `dt_user` tables.

### etl.py
Copy data to staging tables and insert into star schema fact and dimension tables

### sql_queries.py
- Creating and dropping staging and star schema tables
- Copy JSON data from S3 to Redshift staging tables
- Insert data from staging tables to star schema fact and dimension tables

### dwh.cfg
Configure Redshift cluster and data import:

    [CLUSTER]
    HOST=''
    DB_NAME=''
    DB_USER=''
    DB_PASSWORD=''
    DB_PORT=

    [IAM_ROLE]
    ARN=''

    [S3]
    LOG_DATA=''
    LOG_JSONPATH=''
    SONG_DATA=''

## Database Design
The database design schema consists of the following tables:
    
    staging_events - staging table for raw copy of event data
        artist (text)
        auth (text)
        firstName (text)
        gender (char)
        itemInSession (int)
        lastName (text)
        length (float)
        level (text)
        location (text)
        method (text)
        page (text)
        registration (float)
        sessionId (int)
        song (text)
        status (int)
        ts (bigint)
        userAgent (text)
        userId (text)

    staging_songs - staging table for raw copy of song data
        num_songs (int)
        artist_id (text)
        artist_latitude (float)
        artist_longitude (float)
        artist_location (text)
        artist_name (text)
        song_id (text)
        title (text)
        duration (float)
        year (int)

    ft_songplay - contains a consolidated list of song play activity for analysis
        songplay_id (bigint, IDENTITY(0,1) PRIMARY KEY)
        start_time (timestamp, NOT NULL)
        user_id (int, NOT NULL)
        level (text)
        song_id (text)
        artist_id (text)
        session_id (int)
        location (text)
        user_agent (text)

    dt_users - contains data on sparkify users derived from log files in ./data/log_data
        user_id (int, PRIMARY KEY)
        first_name (text)
        last_name (text)
        gender (char)
        level (text)

    dt_songs - contains details on songs from song files in ./data/song_data
        song_id (text, PRIMARY KEY)
        title (text)
        artist_id (text)
        year (int)
        duration (float)

    dt_artists - contains details on artists from song files in ./data/song_data
        artist_id (text, PRIMARY KEY)
        name (text)
        location (text)
        latitude (float)
        longitude (float)

    dt_time - contains a non-duplicate list of timestamps and converted time data
        start_time (timestamp, PRIMARY KEY)
        hour (int)
        day (int)
        week (int)
        month (int)
        year (int)
        weekday (int)


