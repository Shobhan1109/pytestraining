import pytest

@pytest.fixture
def SetUp():
    print("Setup started")

    yield
    print("Exited!!")


def test_AddItemtoCart(SetUp):
    print("Added successfully.")

def test_RemoveItemfromCart(SetUp):
    print("Removed successfully.")
