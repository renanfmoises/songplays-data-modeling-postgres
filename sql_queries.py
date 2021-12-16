# DROP TABLES

# Commom string to DROP TABLE
drop_if_exists = """DROP TABLE IF EXISTS {};"""

songplay_table_drop = drop_if_exists.format("songplays")
user_table_drop = drop_if_exists.format("users")
song_table_drop = drop_if_exists.format("songs")
artist_table_drop = drop_if_exists.format("artists")
time_table_drop = drop_if_exists.format("time")

# CREATE TABLES
create_if_not_exists = """CREATE TABLE IF NOT EXISTS {};"""

# Creating the fact table "songplays"
songplay_table_create = create_if_not_exists.format(
    """
                                    songplays (
                                        songplay_id SERIAL PRIMARY KEY,
                                        start_time TIMESTAMP NOT NULL,
                                        user_id INT NOT NULL,
                                        level VARCHAR,
                                        song_id INT NOT NULL,
                                        artist_id INT NOT NULL,
                                        session_id INT NOT NULL,
                                        location VARCHAR,
                                        user_agent VARCHAR
                                    )
                                """
)

# Creating the dimension tables users, songs, artists, time

user_table_create = create_if_not_exists.format(
    """
                                    users (
                                        user_id INT PRIMARY KEY,
                                        first_name VARCHAR,
                                        last_name VARCHAR,
                                        gender VARCHAR,
                                        level VARCHAR
                                    )
                                """
)

song_table_create = create_if_not_exists.format(
    """
                                    songs (
                                        song_id INT PRIMARY KEY,
                                        title VARCHAR,
                                        artist_id INT NOT NULL,
                                        year INT,
                                        duration NUMERIC NOT NULL
                                        )
                                """
)

artist_table_create = create_if_not_exists.format(
    """
                                    artists (
                                        artist_id INT PRIMARY KEY,
                                        name VARCHAR,
                                        location VARCHAR,
                                        latitude NUMERIC,
                                        longitude NUMERIC
                                        )
                                """
)

time_table_create = create_if_not_exists.format(
    """
                                time (
                                    songplay_id INT FOREIGN KEY,
                                    start_time TIMESTAMP,
                                    hour TIMESTAMP,
                                    day INT,
                                    week INT,
                                    month INT,
                                    year INT,
                                    )
                                """
)

# INSERT RECORDS

insert_into = """INSERT INTO {} VALUES {};"""

songplay_table_insert = insert_into.format(
    """songplays (
            start_time,
            user_id,
            level,
            song_id,
            artist_id,
            session_id,
            location,
            user_agent)""",
    "(%s, %s, %s, %s, %s)",
)

user_table_insert = insert_into.format(
    "users (user_id, first_name, last_name, gender, level)", "(%s, %s, %s, %s, %s)"
)

song_table_insert = insert_into.format(
    "songs (song_id, title, artist_id, year, duration)", "(%s, %s, %s, %s, %s)"
)

artist_table_insert = insert_into.format(
    "artists (artist_id, name, location, latitude, longitude) ", "(%s, %s, %s, %s, %s)"
)

time_table_insert = insert_into.format(
    "time (start_time, hour, day, week, month, year, weekday)",
    "(%s, %s, %s, %s, %s, %s, %s)",
)

# FIND SONGS

song_select = """
    SELECT * FROM songplays WHERE songplay_id = %s;
    """

# QUERY LISTS

create_table_queries = [
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
]
