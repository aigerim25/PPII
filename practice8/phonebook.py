from connect import connect 
from config import load_config
def search_by_pattern():
    config = load_config()
    conn = connect(config)
    cur = conn.cursor()

    pattern = input("Enter pattern: ")
    cur.execute("SELECT * FROM get_contacts_by_pattern(%s) ORDER BY first_name LIMIT 3 OFFSET 1;", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
if __name__ == '__main__':
    search_by_pattern()        