import pytest

@pytest.fixture
def SetUp():
    print("Opened the amazon app.")
    print("Logged in")
    yield
    print("logged out")
    print("Closed amazon app.")

def test_Paymeny(SetUp):
    print("Payment successful.")