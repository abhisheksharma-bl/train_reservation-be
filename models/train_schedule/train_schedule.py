import psycopg2
from train_reservation_be.db import get_connection

class TrainSchedule:
    def __init__(self, train_id, start_place, destination_place, departure_time, arrival_time):
        self.train_id = train_id
        self.start_place = start_place
        self.destination_place = destination_place
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def create(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO train_schedules (train_id, start_place, destination_place, departure_time, arrival_time)
            VALUES (%s, %s, %s, %s, %s) RETURNING id
        """, (self.train_id, self.start_place, self.destination_place, self.departure_time, self.arrival_time))
        train_schedule_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return train_schedule_id

    @staticmethod
    def get_by_id(schedule_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM train_schedules WHERE id = %s", (schedule_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def update(schedule_id, **kwargs):
        conn = get_connection()
        cursor = conn.cursor()
        fields = []
        values = []
        for key, value in kwargs.items():
            fields.append(f"{key} = %s")
            values.append(value)
        values.append(schedule_id)
        sql = f"UPDATE train_schedules SET {', '.join(fields)} WHERE id = %s"
        cursor.execute(sql, tuple(values))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete(schedule_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM train_schedules WHERE id = %s", (schedule_id,))
        conn.commit()
        cursor.close()
        conn.close()
