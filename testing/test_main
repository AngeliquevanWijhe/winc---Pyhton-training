from main import get_none

def test_get_none(): 
    assert get_none() is None

from main import flatten_dict
def test_flatten_dict():
    assert flatten_dict({'a': 42, 'b': 3.14})
    # [42, 3.14]
    assert flatten_dict({'a': [42, 350], 'b': 3.14})
    # [[42, 350], 3.14]
    assert flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})
    # [{'inner_a': 42, 'inner_b': 350}, 3.14]