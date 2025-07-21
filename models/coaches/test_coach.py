from train_reservation_be.models.coaches.coach import Coach

# ---------- CREATE ----------
print("Creating coach:")
coach = Coach(train_id=2, travel_date='2025-07-22', coach_type_id=2, coach_number='A1')
coach_id = coach.create()
print(f"Created coach with ID: {coach_id}")

# ---------- READ ----------
print("\nFetching coach:")
coach_data = Coach.get_by_id(coach_id)
print("Coach Data:", coach_data)

# ---------- UPDATE ----------
print("\nUpdating coach:")
Coach.update(coach_id, current_occupancy=5, coach_number='A1-Renamed')
updated_data = Coach.get_by_id(coach_id)
print("Updated Coach Data:", updated_data)

# ---------- DELETE ----------
print("\nDeleting coach:")
try:
    Coach.delete(coach_id)
    print("Coach deleted successfully.")
except Exception as e:
    print("Deletion failed:", str(e))