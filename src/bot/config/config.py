import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BOT_TOKEN = ''
PGUSER = 'cheese'
PGPASSWORD = 'cheese_901'
DATABASE = 'usupport6'
DBHOST = 'localhost'
ADMIN_SECRET_KEY = '22042kur'

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{DBHOST}/{DATABASE}"

# if __name__ == '__main__':
# print(NASTAVNIK_SECRET_KEY)
