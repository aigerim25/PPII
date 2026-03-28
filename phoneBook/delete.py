import psycopg2
from config import load_config

def delete_username(first_name):
    rows_deleted = 0
    sql = 'DELETE FROM phonebook WHERE first_name = %s'
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (first_name,))
                rows_deleted = cur.rowcount
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return rows_deleted
if __name__ == '__main__':
    deleting_name = input("Enter name: ")

    rows = delete_username(deleting_name)
    print(f"Deleted {rows} row(s)")

