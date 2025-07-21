import psycopg2
from train_reservation_be.db import get_connection

class Seat:
    def __init__(self, seat_number, coach_id, is_allocated=False, allocated_to=None):
        self.seat_number = seat_number
        self.coach_id = coach_id
        self.is_allocated = is_allocated
        self.allocated_to = allocated_to

    def create(self):
        conn = get_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO seats (seat_number, coach_id, is_allocated, allocated_to)
            VALUES (%s, %s, %s, %s)
            RETURNING id
        """
        cur.execute(query, (self.seat_number, self.coach_id, self.is_allocated, self.allocated_to))
        seat_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return seat_id

    @staticmethod
    def get_by_id(seat_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM seats WHERE id = %s", (seat_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def update(seat_id, **kwargs):
        allowed_fields = ['seat_number', 'coach_id', 'is_allocated', 'allocated_to']
        updates = []
        values = []

        for field, value in kwargs.items():
            if field in allowed_fields:
                updates.append(f"{field} = %s")
                values.append(value)

        if not updates:
            return False

        values.append(seat_id)
        query = f"UPDATE seats SET {', '.join(updates)} WHERE id = %s"
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query, tuple(values))
        conn.commit()
        cur.close()
        conn.close()
        return True

    @staticmethod
    def delete(seat_id):
        # Optional: check if this seat is referenced in bookings before deleting
        conn = get_connection()
        cur = conn.cursor()

        # Check for existing booking reference
        cur.execute("SELECT COUNT(*) FROM bookings WHERE seat_id = %s", (seat_id,))
        if cur.fetchone()[0] > 0:
            cur.close()
            conn.close()
            raise Exception("Cannot delete seat as it is referenced in bookings.")

        cur.execute("DELETE FROM seats WHERE id = %s", (seat_id,))
        conn.commit()
        cur.close()
        conn.close()
        return True