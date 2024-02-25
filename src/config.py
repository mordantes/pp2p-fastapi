import os 
import dotenv 


dotenv.load_dotenv()

DB_USER = os.environ.get('DB_USER')
DB_PWD = os.environ.get('DB_PWD')
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')