import msvcrt                              
import pyodbc


def create_connection_to_server(server_name, db_name, driver_v):
    """Connects to defined server with trusted connection."""
    # Create a pyodbc connection
    conn = pyodbc.connect(
        'Driver={ODBC Driver ' + str(driver_v) + ' for SQL Server};'
        'Server=' + server_name + ';'
        'Database=' + db_name + ';'
        'Trusted_Connection=yes;'
    )
    return conn

def create_connection_to_server_printed(server_name, db_name, driver_v):
    print("\nConnecting to:\n • server:\t\t" + server_name + "\n • db:\t\t\t" + db_name + "\n • ODBC Driver:\t" + str(driver_v) + "\t. . .")
    conn = create_connection_to_server(server_name, db_name, driver_v)
    print("\nconnected")
    return conn

def init_connection(server_name, db_name):
    try:
        return create_connection_to_server_printed(server_name, db_name, 13)
    except Exception as e:   
        try:
            return create_connection_to_server_printed(server_name, db_name, 17)
        except:
            print("\nCouldn't connect to the server.\n" ,e)
            return None
            
def wait():
    msvcrt.getch()


def commit(conn):
       
    try:
        # commit to DB upload actions
        conn.commit()
    except:
        print("waitng for you to connect to VPN ;)\nThen type anything and I'll continue\n")
        wait()
        # commit upload actions
        conn.commit()