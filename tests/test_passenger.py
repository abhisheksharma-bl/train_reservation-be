import pytest
from train_reservation_be.models.passenger.passenger import Passenger

def test_create_passenger():
    p = Passenger("Test User", 25, "Other")
    pid = p.create()
    assert isinstance(pid, int)

    result = Passenger.get_by_id(pid)
    assert result is not None
    assert result[1] == "Test User"

    Passenger.delete(pid)

def test_update_passenger():
    p = Passenger("To Update", 30, "Male")
    pid = p.create()

    Passenger.update(pid, age=35)
    updated = Passenger.get_by_id(pid)
    assert updated[2] == 35

    Passenger.delete(pid)

def test_delete_passenger():
    p = Passenger("To Delete", 22, "Female")
    pid = p.create()

    Passenger.delete(pid)
    assert Passenger.get_by_id(pid) is None
