import json
import psycopg2
from train_reservation_be.db import get_connection

class Train:
    def __init__(self, train_number, name, start_place, destination_place, stops=None):
        self.train_number = train_number
        self.name = name
        self.start_place = start_place
        self.destination_place = destination_place
        self.stops = stops or {}

    def create(self):
        conn = get_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO trains (train_number, name, start_place, destination_place, stops)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id
        """
        cur.execute(query, (
            self.train_number,
            self.name,
            self.start_place,
            self.destination_place,
            json.dumps(self.stops)
        ))
        train_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return train_id

    @staticmethod
    def get_by_id(train_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM trains WHERE id = %s", (train_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def update(train_id, **kwargs):
        allowed_fields = ['train_number', 'name', 'start_place', 'destination_place', 'stops']
        updates = []
        values = []

        for field, value in kwargs.items():
            if field in allowed_fields:
                updates.append(f"{field} = %s")
                if field == "stops":
                    values.append(json.dumps(value))
                else:
                    values.append(value)

        if not updates:
            return False

        values.append(train_id)
        query = f"UPDATE trains SET {', '.join(updates)} WHERE id = %s"
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query, tuple(values))
        conn.commit()
        cur.close()
        conn.close()
        return True

    @staticmethod
    def delete(train_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM trains WHERE id = %s", (train_id,))
        conn.commit()
        cur.close()
        conn.close()
        return True


