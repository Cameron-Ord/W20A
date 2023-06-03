import dbcreds
import mariadb

#just gets the id and username of specific a client in the database

def get_client():

    conn = mariadb.connect(**dbcreds.conn_params)
    cursor = conn.cursor()
    try:
        username = input("enter a user: ")
        password = input("enter a password: ")

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
    except:
        print("user does not exist")
        get_client()

#takes user input and inserts into the data table if inputs are valid

def client_post():
    

    conn = mariadb.connect(**dbcreds.conn_params)
    cursor = conn.cursor()
    try:

        client_id = input("Enter client ID: ")
        client_id = int(client_id)
        title = input("Enter title: ")
        content = input("Enter content: ")

        cursor.execute('CALL insert_post(?,?,?)', [client_id, title, content])
        cursor.close()
        conn.close()

        return

    except TypeError:
        print("invalid entry")
        client_post()


#simply gets all the posts ordered by client id

def archive_posts():
    
    try:
    
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()    
        cursor.execute('CALL get_posts()')
        results = cursor.fetchall()
        
        for i in results:
            print(i)
          


        cursor.close()
        conn.close()
        return 
    
    except:
        print("column does not exist")
        choose_function()

#prompts user to input a username and password. if it matches with a user and pass on the database it will greet them and return them to the menu to make a selection

def login():

    print("LOG IN")

    conn = mariadb.connect(**dbcreds.conn_params)
    cursor = conn.cursor()
    try:
        username = input("USERNAME: ")
        password = input("PASSWORD: ")

        cursor.execute('CALL get_client(?, ?)', [username, password])
        results = cursor.fetchall()

        cursor.close()
        conn.close()
        x = len(results)
        
        
        if(x < 1):
            print("incorrect user/password")
            login()
        elif(x>0):
            print(f'Welcome, {results}')
            return
        else:
            print('oops')
    except TypeError:
        print("invalid entry error")
        choose_function()
    except:
        print("unknown error")
        

#function gets called on script start. Prompts user to make a selection

def choose_function():
    
    try:
        while(True):
            print("1. GET CLIENT")
            print("2. GET CLIENT POST")
            print("3. ARCHIVE POSTS")
            print("4. LOGIN")
            print("5. EXIT")
            choice = int(input("choose a function: "))
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
                print("Please enter a number within parameters")
    except TypeError:
        print("please enter a number")
        choose_function()

    except ValueError:
        print("please enter a number")
        choose_function()
choose_function()


        
