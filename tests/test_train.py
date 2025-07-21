
import pytest
from train_reservation_be.models.train.train import Train

@pytest.fixture
def sample_train():
    return Train(
        train_number="000000",
        name="Express",
        start_place="Delhi",
        destination_place="Mumbai",
        stops={"Kanpur": "10:00", "Bhopal": "14:00"}
    )

def test_create_train(sample_train):
    train_id = sample_train.create()
    assert isinstance(train_id, int)

# def test_get_train_by_id():
#     result = Train.get_by_id("insert train_id")
#     assert result is not None
#     assert result[1] == "000000" 
