from train_reservation_be.models.seats.seat import Seat

# Note: Ensure the coach with ID 1 exists before running this test.
# Also ensure passenger with ID 1 exists if you are assigning allocated_to.

# ----------- CREATE Seat -----------
print("Creating seat:")
seat = Seat(seat_number=1, coach_id=5, is_allocated=False, allocated_to=None)
seat_id = seat.create()
print(f"Created seat with ID: {seat_id}")

# ----------- READ Seat -----------
print("\nFetching seat:")
seat_data = Seat.get_by_id(seat_id)
print("Seat Data:", seat_data)

# ----------- UPDATE Seat -----------
print("\nUpdating seat:")
Seat.update(seat_id, is_allocated=True, allocated_to=1)  # Assume passenger with ID 1 exists
updated_seat = Seat.get_by_id(seat_id)
print("Updated Seat Data:", updated_seat)

# ----------- DELETE Seat -----------
print("\nDeleting seat:")
try:
    Seat.delete(seat_id)
    print("Seat deleted successfully.")
except Exception as e:
    print("Error during deletion:", str(e))