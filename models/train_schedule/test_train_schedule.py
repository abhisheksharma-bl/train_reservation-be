from train_reservation_be.models.train_schedule.train_schedule import TrainSchedule

train_id = 1

# Create
# ts = TrainSchedule(train_id, "Delhi", "Mumbai", "2025-08-01 10:00", "2025-08-01 22:00")
# ts_id = ts.create()
# print("Created:", ts_id)

# Read
result = TrainSchedule.get_by_id(2)
print("Fetched:", result)

# # Update
# TrainSchedule.update(ts_id, departure_time="2025-08-01 11:00")
# print("Updated:", TrainSchedule.get_by_id(ts_id))

# # Delete
# TrainSchedule.delete(ts_id)
# print("Deleted. Fetch should return None:", TrainSchedule.get_by_id(ts_id))





##run ----> python3 -m train_reservation_be.models.train_schedule.test_train_schedule