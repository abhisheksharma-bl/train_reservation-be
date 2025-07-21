from train_reservation_be.models.coach_types.coach_types import CoachType

# ----------- CREATE Coach Type -----------
print("Creating coach type:")
coach_type = CoachType(name="AC", seat_capacity=72)
coach_type_id = coach_type.create()
print(f"Created coach_type with ID: {coach_type_id}")

# ----------- READ Coach Type -----------
print("\nFetching coach type:")
print(CoachType.get_by_id(coach_type_id))

# ----------- UPDATE Coach Type -----------
print("\nUpdating coach type:")
CoachType.update(coach_type_id, name="AC Updated", seat_capacity=80)
print(CoachType.get_by_id(coach_type_id))

# ----------- DELETE Coach Type -----------
print("\nDeleting coach type:")
CoachType.delete(coach_type_id)
print("Coach type deleted.")