import psycopg2
# from db import get_connection
from train_reservation_be.db import get_connection



class Passenger:
    def __init__(self, name=None, age=None, gender=None):
        self.name = name
        self.age = age
        self.gender = gender

    def create(self):
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO passengers (name, age, gender)
                        VALUES (%s, %s, %s)
                        RETURNING id
                        """,
                        (self.name, self.age, self.gender)
                    )
                    passenger_id = cur.fetchone()[0]
                    print(f"Passenger created with ID: {passenger_id}")
                    return passenger_id
        except Exception as e:
            print(f"Error creating passenger: {e}")
            return None

    @staticmethod
    def get_by_id(passenger_id):
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM passengers WHERE id = %s", (passenger_id,))
                    passenger = cur.fetchone()
                    if passenger:
                        print(f"Passenger found: {passenger}")
                        return passenger
                    else:
                        print("Passenger not found.")
                        return None
        except Exception as e:
            print(f"Error fetching passenger: {e}")
            return None

    @staticmethod
    def update(passenger_id, name=None, age=None, gender=None):
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    fields = []
                    values = []

                    if name:
                        fields.append("name = %s")
                        values.append(name)
                    if age:
                        fields.append("age = %s")
                        values.append(age)
                    if gender:
                        fields.append("gender = %s")
                        values.append(gender)

                    if not fields:
                        print("No fields to update.")
                        return

                    values.append(passenger_id)
                    query = f"UPDATE passengers SET {', '.join(fields)} WHERE id = %s"
                    cur.execute(query, tuple(values))
                    print(f"Passenger {passenger_id} updated.")
        except Exception as e:
            print(f"Error updating passenger: {e}")

    @staticmethod
    def delete(passenger_id):
        try:
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("DELETE FROM passengers WHERE id = %s", (passenger_id,))
                    print(f"Passenger {passenger_id} deleted.")
        except Exception as e:
            print(f"Error deleting passenger: {e}")
