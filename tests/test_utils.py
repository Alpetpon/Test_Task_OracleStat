from url_checker.utils import is_valid_url

def test_is_valid_url():
    assert is_valid_url('https://www.google.com') == True
    assert is_valid_url('not_a_url') == False
