import pytest
from src import utils
JSON = 'operations.json'

def test_load_operations():
    with pytest.raises(NameError):
        utils.load_operations(JSO)
    with pytest.raises(FileNotFoundError):
        utils.load_operations(JSON)
    with pytest.raises(FileNotFoundError):
        utils.load_operations('operations.json')
    with pytest.raises(AttributeError):
        utils.read_data_time(JSON)
    with pytest.raises(NameError):
        utils.read_data_time(JSO)
    with pytest.raises(AttributeError):
        utils.read_data_time('operations.json')

def test_read_data_time():

    with pytest.raises(AttributeError):
        utils.read_data_time(JSON)
    with pytest.raises(NameError):
        utils.read_data_time(JSO)
    with pytest.raises(AttributeError):
        utils.read_data_time('operations.json')
    with pytest.raises(NameError):
        utils.load_operations(JSO)
    with pytest.raises(FileNotFoundError):
        utils.load_operations(JSON)
    with pytest.raises(FileNotFoundError):
        utils.load_operations('operations.json')
    with pytest.raises(NameError):
        utils.load_operations(JSO)
    with pytest.raises(FileNotFoundError):
        utils.load_operations(JSON)
    with pytest.raises(FileNotFoundError):
        utils.load_operations('operations.json')
    with pytest.raises(AttributeError):
        utils.read_data_time(JSON)
    with pytest.raises(NameError):
        utils.read_data_time(JSO)
    with pytest.raises(AttributeError):
        utils.read_data_time('operations.json')



