

# Simple Data Modeling and ETL with Postgres and Python

<small>The current repository stores code from Udacity's Data Engineering Nanodegree first hands-on project. </small>

***

## Summary
**This project covers a simple ETL process for storing data from the fictitious company Sparkify, a music streaming application.**

The database is created and populated with `python` scripts running `psycopg2` methods to query and interact via `SQL` with PostgresSQL. After running the script we will end up with a database fully populated with data relevant to the Sparkify operation.

## Installation

### Python version

I have used python 3.8.6 for this project.

Further libraries and its respective versions can be found in `requirements.txt`.


### A step-by-step guide to running the ETL:

1. Download and install PostgresSQL app;
    - Crete and start a new server;

2. Install **psycopg2** library:
   - `pip install psycopg2`;

3. Run `create_tables.py` on your terminal;

4. Run cells on `notebooks/test.ipynb` to test the ETL process.

**If everything works fine, you should see the queries results as outputs in the notebook.**

## The Files

### `sql_queries.py`: The Tables

Queries and code for creating and populating the Database can be found in the `sql_queries.py` file.

The tables created and populated with those scripts are:

- Songplays;
- Users;
- Songs;
- Artists;
- Time

### `create_tables.py`: The Database Set-up

In order for the **ETL** to work properly, the `create_table.py` file must b e run first.

This file will create the database and tables, bring the database up to date with the latest schema, and populate the tables with the data. Queries in this file are imported from `sql_queries.py`.

The `create_table.py` file also works as a restarter for the project. Once such file is run, the database will be dropped and recreated, ensuring that previous data contained in it is dropped such as the database itself and the tables. This will help with inconveniently running into errors of duplicated tables and data.

The code is fully documented, please check it out.

### `notebooks/etl.ipynb`: The ETL Sandbox

This file is a Jupyter Notebook with the process of designing the best flow for the ETL process.

The notebook is divided into sections, each section is a different step of the ETL process.

Sections also are documented and it is worth reading them to have a better understanding of the process automated in the `etl.py` file.

### `etl.py`: The ETL Process

This script will process the data stored in `song_data` and `log_data` json files and is consolidated using the previous scripts and notebooks.

**PLEASE NOTE**: <u>Even though this project was built using fake data, such files are not included in this repo, in accordance with best practices of data governance.</u>

### `notebooks/test.ipynb`: The Checks and Tests

This notebook works as a simple interface for connecting to the database and checking if queries are working as expected.

Really ah hoc, if the code runs fine and the queries return expected results, the data will be shown immediately. This works as a simple test for the ETL process.

***

### Contact & PR

Feel free to hit me up with suggestions of how to make it even simpler if you know some tricks I may have missed. PR are also welcome.








