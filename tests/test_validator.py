from url_checker.validator import validate_urls

def test_validate_urls():
    urls = ['https://www.google.com', 'not_a_url']
    valid, invalid = validate_urls(urls)
    assert valid == ['https://www.google.com']
    assert invalid == ['not_a_url']
