import psycopg2

conn = psycopg2.connect(database='homework',
                        user='postgres',host='localhost'
                        ,password='1234',port='5432')

cur = conn.cursor()

class foydalanuvchi:
    def __init__(self,first_name,last_name,username,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password


    def save_user(self):
        save_query = """insert into users (first_name,last_name,username,email,password) 
                        values (%s,%s,%s,%s,%s)"""
        cur.execute(save_query,(self.first_name,self.last_name,self.username,self.email,self.password))
        conn.commit()
        print('User has been successfully saved')

    def delete_user(self):
        delete_query = """delete from users where username = '%s'"""
        cur.execute(delete_query,(self.username))
        conn.commit()
        print('User has been successfully deleted')

    def update_user(self):
        update_query = """update users where username = '%s'"""
        cur.execute(update_query,(self.username))
        conn.commit()
        print('User has been successfully updated')

    def show_users(self):
        show_query = """select * from users"""
        cur.execute(show_query)
        conn.commit()


    def create_table(self):
        create_query = """CREATE TABLE IF NOT EXISTS users (
        id serial PRIMARY KEY,
        firstname VARCHAR(255) NOT NULL,
        lastname VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        )"""
        cur.execute(create_query)
        conn.commit()
        print('User table has been created')
