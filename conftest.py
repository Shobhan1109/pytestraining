import pytest

@pytest.fixture(scope="session",autouse=True)
def SetUp():
    print("Opened the amazon app.")
    print("Logged in")
    yield
    print("logged out")
    print("Closed amazon app.")