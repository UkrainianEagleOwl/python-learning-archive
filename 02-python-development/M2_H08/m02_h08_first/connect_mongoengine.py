from mongoengine import connect
from configparser import ConfigParser


def get_conect_uri():
    # Load the configuration from config.ini
    config = ConfigParser()
    config.read('config.ini')

    # Extract the database connection information
    db_user = config.get('DB', 'USER')
    db_password = config.get('DB', 'PASSWORD')
    db_name = config.get('DB', 'DB_NAME')
    db_domain = config.get('DB', 'DOMAIN')
    
    # Get the database
    uri = f'mongodb+srv://<username>:<password>@<cluster>/<database>'
    return uri

def do_connect_to_db(db_name):
    uri = get_conect_uri()
    connect(db=db_name, host=uri)
    

# if __name__ == '__main__':
#     do_connect('M2_H08')   
    