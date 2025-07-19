import psycopg2
# from config import DB_CONFIG
from train_reservation_be.config import DB_CONFIG



def get_connection():
    return psycopg2.connect(**DB_CONFIG)
