
# import pytest
# from train_reservation_be.models.train_schedule.train_schedule import TrainSchedule

# @pytest.fixture
# def sample_schedule():
#     return TrainSchedule(
#         train_id=1,
#         source_station="Delhi",
#         destination_station="Mumbai",
#         departure_time="2025-08-01 10:00",
#         arrival_time="2025-08-01 22:00"
#     )

# def test_create_schedule(sample_schedule):
#     schedule_id = sample_schedule.create()
#     assert isinstance(schedule_id, int)

# def test_get_schedule_by_id():
#     result = TrainSchedule.get_by_id("inser_train_id")
#     assert result is not None
#     assert result[2] == "Delhi" 
