# Sparkify Data Lake Project with Spark
The purpose of this project is to build an ETL pipeline that will be able to extract song and log data from an S3 bucket, process the data with pyspark, then loading the data back into s3 as a set of dimensional tables in parquet files. This helps analysts to continue finding insights on what their users listen to.

## Database Schema Design
The tables created include one fact tablec called `songplays` and four dimensional tables namely `users`, `songs`, `artists` and `time`. This follows the star schema principle which will contain clean data that is suitable for OLAP(Online Analytical Processing) operations which will be what the analysts will need to conduct to find the insights they are looking for.

## Run

1. Set environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.
2. Create an S3 bucket and replace the `output_data` variable in the `main()` function with `s3a://<bucket name>/`, or uncomment the line below to run locally.

**Run ETL pipeline**

```bash
$ python etl.py
```


