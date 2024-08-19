import pytest

from ..utils.config_reader import Config_Reader


@pytest.fixture
def setup():
    cfg = Config_Reader()

def test_read_default_file_config_ini(setup):
    assert setup. cfg["host"] == 'mediasrv:27017'




@pytest.fixture

def setup_data():
    # Scaffold data
    data = {"key": "value"}
    yield data
    # Teardown code to delete data
    del data
def test_example(setup_data):
    assert setup_data["key"] == "value"