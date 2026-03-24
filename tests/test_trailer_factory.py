import pytest
from yardops.factories.trailer_factory import TrailerFactory

def test_dry_trailer():
    trailer = TrailerFactory.create(
        trailer_number = "123",
        trailer_type = "DRY",
        carrier_name = "test carrier"
    )
    assert trailer.trailer_number == "123"
    assert trailer.temp_setting == None

def test_refer_trailer():
    trailer = TrailerFactory.create(
        trailer_number = "456",
        trailer_type = "REEFER",
        carrier_name = "ABC",
    )
    assert trailer.temp_setting == -10

def test_flatbed_trailer():
    trailer = TrailerFactory.create(
        trailer_number = "789",
        trailer_type = "FLATBED",
        carrier_name = "XYZ",
    )
    assert trailer.temp_setting == None

def test_invalid_trailer():
    with pytest.raises(ValueError):
        TrailerFactory.create(
            trailer_number = "123",
            trailer_type = "INVALID",
            carrier_name = "ABC"
        )

def test_flatbed_with_temp():
    with pytest.raises(ValueError):
        TrailerFactory.create(
            trailer_number = "123",
            trailer_type = "FLATBED",
            carrier_name = "ABC",
            temp_setting = 5
        )