import psycopg2
from train_reservation_be.db import get_connection

class Coach:
    def __init__(self, train_id, travel_date, coach_type_id, coach_number, current_occupancy=0):
        self.train_id = train_id
        self.travel_date = travel_date
        self.coach_type_id = coach_type_id
        self.coach_number = coach_number
        self.current_occupancy = current_occupancy

    def create(self):
        conn = get_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO coaches (train_id, travel_date, coach_type_id, coach_number, current_occupancy)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id
        """
        cur.execute(query, (
            self.train_id,
            self.travel_date,
            self.coach_type_id,
            self.coach_number,
            self.current_occupancy
        ))
        coach_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return coach_id

    @staticmethod
    def get_by_id(coach_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM coaches WHERE id = %s", (coach_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def update(coach_id, **kwargs):
        allowed_fields = ['train_id', 'travel_date', 'coach_type_id', 'coach_number', 'current_occupancy']
        updates = []
        values = []

        for field, value in kwargs.items():
            if field in allowed_fields:
                updates.append(f"{field} = %s")
                values.append(value)

        if not updates:
            return False

        values.append(coach_id)
        query = f"UPDATE coaches SET {', '.join(updates)} WHERE id = %s"
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query, tuple(values))
        conn.commit()
        cur.close()
        conn.close()
        return True

    @staticmethod
    def delete(coach_id):
        conn = get_connection()
        cur = conn.cursor()

        # Prevent deletion if referenced elsewhere (e.g. seats/bookings)
        cur.execute("SELECT COUNT(*) FROM seats WHERE coach_id = %s", (coach_id,))
        if cur.fetchone()[0] > 0:
            cur.close()
            conn.close()
            raise Exception("Cannot delete coach — it is referenced in seats.")

        cur.execute("DELETE FROM coaches WHERE id = %s", (coach_id,))
        conn.commit()
        cur.close()
        conn.close()
        return True