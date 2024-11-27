import mysql.connector
from app.configuration import UserDbConfiguration

# Database connection
class UserDatabase:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def make_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)

    def my_cursor(self):
        return self.cursor


class UserModel:
    def __init__(self, connection):
        try:
            self.connection = connection
            self.cursor = connection.cursor()
        except Exception as err:
            print('Something went wrong! Internet connection or database connection.')
            print(f'Error: {err}')

    def register_user(self, f_name, s_name, l_name, phone_num, email, password):
        sql = """
                INSERT INTO user(f_name, s_name, l_name, phone_num, email, password)
                VALUES(%s, %s, %s, %s, %s, %s)
                """
        try:
            # Execute ama cabeyn
            self.cursor.execute(
                sql,
                (f_name, s_name, l_name, phone_num, email, password)
            )

            # rid
            self.connection.commit()  #  very, very important


            print('Waa la kaydiyey isticmaalha cusub!')
            return True, f'Waa la kaydiyey tababbarka cusub!'

        except Exception as e:
            print('Lama kaydinin isticmaalaha cusub!')
            print(f'Error: {e}')
            return False, f'Error: {e}.'



# Testing Here


user_configuration = UserDbConfiguration()


# Checking the connection (DB connection) |
def check_user_model_connection():
    try:
        mysql_connect = UserDatabase(
            host=user_configuration.DB_HOSTNAME,
            port=3307,
            user=user_configuration.DB_USERNAME,
            password=user_configuration.DB_PASSWORD,
            database=user_configuration.DB_NAME
        )
        #

        mysql_connect.make_connection()

        user_model = UserModel(mysql_connect.connection)

        return True, user_model
    except Exception as e:
        print(f'')
        return False, f'Error: {e}.'


if __name__ == '__main__':
    # Create an instance of the MySQLConnect class

    # connection to the database

    print('Connecting to the database...')
    # Checking database connectivity
    connection_status, user_model = check_user_model_connection() # True, False
    if connection_status:
        print('You are connected to the database successfully!')

        user_model.register_user('Abdinajib', 'Abdow', 'Abdirahman', '+252615374914', 'najka@gmail.com', '123')


    else:
        print(f'Database Connection {user_model}')
