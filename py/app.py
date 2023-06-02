import dbcreds
import mariadb

def get_client():

    conn = mariadb.connect(**dbcreds.conn_params)
    cursor = conn.cursor()

    username = input("enter a user:")
    password = input("enter a password:")

    cursor.execute('CALL get_client(?, ?)', [username, password])
    results = cursor.fetchall()

    cursor.close()
    conn.close()
    
    x = len(results)

    if(x < 1):
        results = None
        print("invalid entry")
        return None
    else:
        print(results)
        return results
    
get_client()