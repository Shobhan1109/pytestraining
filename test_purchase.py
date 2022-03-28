import pytest

@pytest.fixture
def SetUp():
    print("User logged in")

    yield
    print("User logged out")


def test_AddItemtoCart(SetUp):
    print("Added successfully.")

def test_RemoveItemfromCart(SetUp):
    print("Removed successfully.")
