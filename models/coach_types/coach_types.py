import psycopg2
from train_reservation_be.db import get_connection

class CoachType:
    def __init__(self, name, seat_capacity):
        self.name = name
        self.seat_capacity = seat_capacity

    def create(self):
        conn = get_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO coach_types (name, seat_capacity)
            VALUES (%s, %s)
            RETURNING id
        """
        cur.execute(query, (self.name, self.seat_capacity))
        coach_type_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return coach_type_id

    @staticmethod
    def get_by_id(coach_type_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM coach_types WHERE id = %s", (coach_type_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def update(coach_type_id, **kwargs):
        allowed_fields = ['name', 'seat_capacity']
        updates = []
        values = []

        for field, value in kwargs.items():
            if field in allowed_fields:
                updates.append(f"{field} = %s")
                values.append(value)

        if not updates:
            return False

        values.append(coach_type_id)
        query = f"UPDATE coach_types SET {', '.join(updates)} WHERE id = %s"
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query, tuple(values))
        conn.commit()
        cur.close()
        conn.close()
        return True

    @staticmethod
    def delete(coach_type_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM coach_types WHERE id = %s", (coach_type_id,))
        conn.commit()
        cur.close()
        conn.close()
        return True