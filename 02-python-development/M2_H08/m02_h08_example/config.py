from configparser import ConfigParser

def get_connection_string():
        
    # Load the configuration from config.ini
    config = ConfigParser()
    config.read('config.ini')

    # Extract the database connection information
    db_user = config.get('DB', 'USER')
    db_password = config.get('DB', 'PASSWORD')
    db_name = config.get('DB', 'DB_NAME')
    db_domain = config.get('DB', 'DOMAIN')
    
    uri = f"mongodb+srv://<username>:<password>@<cluster>/<database>"

    # Construct the connection string
    return uri
    