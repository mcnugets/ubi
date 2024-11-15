import psycopg2

def create_database(db_name, user, password, host, port):
    """Creates a new database if it doesn't exist."""

    conn_str = f"dbname=postgres user={user} password={password} host={host} port={port}"

    try:
        conn = psycopg2.connect(conn_str)
        conn.autocommit = True
        cursor = conn.cursor()

        cursor.execute(f"CREATE DATABASE {db_name}")
        print(f"Database '{db_name}' created successfully.")

    except psycopg2.DatabaseError as e:
        print(f"Error creating database: {e}")

    finally:
        if conn:
            conn.close()

# Example usage:
db_name = "my_database"
user = "your_user"
password = "your_password"
host = "your_host"
port = "your_port"

create_database(db_name, user, password, host, port)