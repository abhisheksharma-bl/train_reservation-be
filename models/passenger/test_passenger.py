from train_reservation_be.models.passenger.passenger import Passenger

# Create
p = Passenger("Sachin", 28, "Male")
pid = p.create()
print(f"Created Passenger ID: {pid}")

# # Read
# data = Passenger.get_by_id(pid)
# print(" Fetched:", data)

# # Update
# Passenger.update(pid, age=29)
# print(" Updated age to 29")

# # Delete
# Passenger.delete(pid)
# print(" Deleted Passenger")


#python3 -m train_reservation_be.models.passenger.test_passenger