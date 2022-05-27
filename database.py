import psycopg2

def store_password(email_number_username, password, website):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO accounts (email_number_username, password, website) VALUES (%s, %s, %s)"""
        record_to_insert = (email_number_username, password, website)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)


def connect():
    try:
      connection = psycopg2.connect(user="bozhidar",
                                    password="bojidar0107",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="passwordsmanager")
      return connection
    except (Exception, psycopg2.Error) as error:
      print(error)


def print_all_rows():
  connection = connect()
  cursor = connection.cursor()
  postgres_select_query = """SELECT * from accounts"""
  cursor.execute(postgres_select_query)
  rows  = cursor.fetchall()

  for row in rows:
    print("Email/number/username: ", row[0])
    print("Password: ", row[1])
    print("Website: ", row[2] + '\n')

