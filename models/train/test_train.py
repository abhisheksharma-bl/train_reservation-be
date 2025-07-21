from train_reservation_be.models.train.train import Train

stops = {
    "Delhi": "08:00",
    "Agra": "10:00",
    "Kanpur": "13:00",
    "Lucknow": "16:00"
}

# Create train
# t = Train("12345", "Shatabdi Express", "Delhi", "Lucknow", stops)
# train_id = t.create()
# print("Created train with ID:", train_id)

# Read train
print("Fetching train:")
print(Train.get_by_id(1))

# # Update train
# print("Updating train:")
# Train.update(train_id, name="Superfast Express", stops={"Delhi": "08:30", "Agra": "10:30"})
# print(Train.get_by_id(train_id))

# # Delete train
# Train.delete(train_id)
# print("Deleted train.")


##python3 -m train_reservation_be.models.train.test_train