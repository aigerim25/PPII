import psycopg2
from config import load_config
import json

def filter_by_group():
    command = """ 
    SELECT c.name, c.email, g.name AS group_name
    FROM contacts c
    JOIN groups g ON c.group_id = g.id
    WHERE g.name = 'Work';
    """
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)

                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
def search_by_email():
    email_part = input("Enter part of email: ")
    command = """
    SELECT name, email FROM contacts
    WHERE email ILIKE %s; 
    """   
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command, ('%' + email_part + '%',))

                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)  
def sort_results():
    print("Sort by:")
    print("1 - name")
    print("2 - birthday")
    choice = input("Choose option: ")
    allowed_sort = {
        "1": "name", 
        "2": "birthday"
    }                  
    sort_column = allowed_sort.get(choice)
    if sort_column is None:
        print("Invalid option")   
        return 
    command = f"""
    SELECT name, email, birthday
    from contacts
    order by {sort_column}
    """    
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)

                rows = cur.fetchall()
                for row in rows:
                    print(row)    
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)    
def paginated_navigation():
    page = 1
    limit = 5
    while True:
        offset = (page - 1) * limit

        command = """
        SELECT name, email, birthday
        from contacts
        order by id
        LIMIT %s OFFSET %s;
        """                
        try:
            config = load_config()
            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cur:
                    cur.execute(command, (limit, offset))
                    rows = cur.fetchall()

                    print(f"\n--- Page {page} ---")    
                    if not rows:
                        print("No contacts on this page")
                    else:
                        for row in rows:
                            print(row)
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)
            return
        action = input("\nType next / prev / quit:").lower() 
        if action == "next":
            page += 1
        if action == "prev":
            if page > 1:
                page -= 1
            else:
                print("You already on the first page")
        elif action == "quit":
            break
        else:
            print("Invalid command")   
def import_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for contact in data:
                    name = contact["name"]
                    email = contact["email"]
                    birthday = contact["birthday"]
                    group_name = contact["group"]  
                    cur.execute(
                        "SELECT id from groups where name = %s",
                        (group_name,)
                    )                
                    group = cur.fetchone()
                    if group is None:
                        cur.execute(
                            "Insert into groups (name) values (%s) RETURNING id",
                            (group_name,)
                        )
                        group_id = cur.fetchone()[0]
                    else:
                        group_id = group[0]    

                    cur.execute(
                        "SELECT id from contacts where name = %s",
                        (name,)
                    )
                    existing = cur.fetchone()
                    if existing:
                        choice = input(f"{name} already exists. skip/overwrite?").lower()
                        if choice == "skip":
                            continue
                        elif choice == "overwrite":
                            cur.execute(
                                """
                                Update contacts 
                                SET email = %s, birthday = %s, group_id = %s
                                WHERE name = %s
                                """,(email, birthday, group_id, name)
                            )  
                    else:
                        cur.execute("""
                        Insert into contacts (name, email, birthday, group_id)
                        values (%s, %s, %s, %s)
                        """, (name, email, birthday, group_id))    
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)                          
if __name__ == '__main__':
    # filter_by_group()   
    # search_by_email()
    # sort_results()
    paginated_navigation()
    # import_from_json("database.json")

      
