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
                                        user_id VARCHAR NOT NULL,
                                        level VARCHAR NOT NULL,
                                        song_id VARCHAR NOT NULL,
                                        artist_id VARCHAR NOT NULL,
                                        session_id VARCHAR NOT NULL,
                                        location VARCHAR NOT NULL,
                                        user_agent VARCHAR NOT NULL
                                        )
                                """
)

# Creating the dimension tables users, songs, artists, time
user_table_create = create_if_not_exists.format(
    """
                                    users (
                                        user_id VARCHAR PRIMARY KEY,
                                        first_name VARCHAR NOT NULL,
                                        last_name VARCHAR NOT NULL,
                                        gender VARCHAR NOT NULL,
                                        level VARCHAR NOT NULL
                                    )
                                """
)

song_table_create = create_if_not_exists.format(
    """
                                    songs (
                                        song_id VARCHAR PRIMARY KEY,
                                        title VARCHAR NOT NULL,
                                        artist_id VARCHAR NOT NULL,
                                        year INT NOT NULL,
                                        duration NUMERIC NOT NULL
                                    )
                                """
)

artist_table_create = create_if_not_exists.format(
    """
                                    artists (
                                        artist_id VARCHAR PRIMARY KEY,
                                        name VARCHAR NOT NULL,
                                        location VARCHAR NOT NULL,
                                        latitude NUMERIC NOT NULL,
                                        longitude NUMERIC NOT NULL
                                    )
                                """
)

time_table_create = create_if_not_exists.format(
    """
                                time (
                                    start_time TIMESTAMP PRIMARY KEY,
                                    hour INT NOT NULL,
                                    day INT NOT NULL,
                                    week INT NOT NULL,
                                    month INT NOT NULL,
                                    year INT NOT NULL,
                                    weekday INT NOT NULL
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
    """(%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (songplay_id) DO NOTHING;""",
)


user_table_insert = insert_into.format(
    "users (user_id, first_name, last_name, gender, level)",
    "(%s, %s, %s, %s, %s) ON CONFLICT (level) DO UPDATE SET level = EXCLUDED.level;",
)

song_table_insert = insert_into.format(
    "songs (song_id, title, artist_id, year, duration)",
    "(%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING;",
)

artist_table_insert = insert_into.format(
    "artists (artist_id, name, location, latitude, longitude) ",
    "(%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING;",
)

time_table_insert = insert_into.format(
    "time (start_time, hour, day, week, month, year, weekday)",
    "(%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING;",
)

# FIND SONGS

song_select = """
    SELECT songs.song_id, artists.artist_id
    FROM songs
    JOIN artists ON songs.artist_id = artists.artist_id
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
