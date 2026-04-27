import psycopg2
from config import load_config


def get_connection():
    config = load_config()

    return psycopg2.connect(
        dbname=config["db_name"],
        user=config["db_user"],
        password=config["db_password"],
        host=config["db_host"],
        port=config["db_port"]
    )


def create_tables():
    command = """
    CREATE TABLE IF NOT EXISTS players (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS game_sessions (
        id SERIAL PRIMARY KEY,
        player_id INTEGER REFERENCES players(id),
        score INTEGER NOT NULL,
        level_reached INTEGER NOT NULL,
        played_at TIMESTAMP DEFAULT NOW()
    );
    """

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(command)
    except Exception as error:
        print("Database error:", error)


def get_or_create_player(username):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO players (username)
                    VALUES (%s)
                    ON CONFLICT (username)
                    DO UPDATE SET username = EXCLUDED.username
                    RETURNING id;
                    """,
                    (username,)
                )

                player_id = cur.fetchone()[0]
                return player_id

    except Exception as error:
        print("Player error:", error)
        return None


def save_result(username, score, level):
    try:
        player_id = get_or_create_player(username)

        if player_id is None:
            return

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO game_sessions (player_id, score, level_reached)
                    VALUES (%s, %s, %s);
                    """,
                    (player_id, score, level)
                )

    except Exception as error:
        print("Save result error:", error)


def get_top_scores():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT p.username, g.score, g.level_reached, g.played_at
                    FROM game_sessions g
                    JOIN players p ON g.player_id = p.id
                    ORDER BY g.score DESC
                    LIMIT 10;
                    """
                )

                return cur.fetchall()

    except Exception as error:
        print("Leaderboard error:", error)
        return []


def get_personal_best(username):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT MAX(g.score)
                    FROM game_sessions g
                    JOIN players p ON g.player_id = p.id
                    WHERE p.username = %s;
                    """,
                    (username,)
                )

                result = cur.fetchone()[0]
                return result if result is not None else 0

    except Exception as error:
        print("Personal best error:", error)
        return 0