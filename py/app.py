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
        return 
    


def client_post():

    conn = mariadb.connect(**dbcreds.conn_params)
    cursor = conn.cursor()

    client_id = input("Enter client ID")
    client_id = int(client_id)
    title = input("Enter title")
    content = input("Enter content")

    cursor.execute('CALL insert_post(?,?,?)', [client_id, title, content])
    cursor.close()
    conn.close()

    return



def archive_posts():

    conn = mariadb.connect(**dbcreds.conn_params)
    cursor = conn.cursor()    
    cursor.execute('CALL get_posts()')
    results = cursor.fetchall()

    print(results)

    cursor.close()
    conn.close()
    return 



def login():

    print("LOG IN")

    conn = mariadb.connect(**dbcreds.conn_params)
    cursor = conn.cursor()

    username = input("USERNAME:")
    password = input("PASSWORD")

    cursor.execute('CALL get_client(?, ?)', [username, password])
    results = cursor.fetchall()

    cursor.close()
    conn.close()
    x = len(results)
    
    while(True):
        if(x < 1):
            print("incorrect user/password")
            login()
        else:
            break
        
def choose_function():

    while(True):

        choice = int(input("choose a function"))

        if(choice == 1):

            get_client()

        elif(choice == 2):

            client_post()

        elif(choice == 3):
            archive_posts()

        elif(choice == 4):
            login()

        elif(choice == 5):
            return

        else:
            break

choose_function()


        
