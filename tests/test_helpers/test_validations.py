from src.helpers.validations import Validator

def test_valid_password():
    result = Validator.validate_password("Newuser12@")
    assert result

def test_valid_zipcode():
    result = Validator.validate_zipcode("232373")
    assert result

def test_valid_cityname():
    result = Validator.validate_cityname("noida")
    assert result

def test_valid_username():
    result = Validator.validate_username("tanvibansal")
    assert result

def test_invalid_password():
    result = Validator.validate_password("Newuser1")
    assert result

def test_invalid_zipcode():
    result = Validator.validate_zipcode("2392373")
    assert result

def test_invalid_cityname():
    result = Validator.validate_cityname("1")
    assert result

def test_invalid_username():
    result = Validator.validate_username("@")
    assert result

