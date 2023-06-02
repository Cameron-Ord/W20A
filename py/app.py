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
    
    print(results)

    if(results == None):
        return None
    else:
        return results
get_client()