import pytest
from yardops.factories.appointment_factory import AppointmentFactory

def test_success_checkin(sample_site,drytrailer):
    appt = AppointmentFactory.create_appointment(
        site_id = sample_site.id,
        trailer_id = drytrailer.id
    )
    assert appt.status == "CHECKED_IN"
    
def test_prefered_spot_works(sample_site,drytrailer):
    spot = sample_site.yard_spots[0]
    appt = AppointmentFactory.create_appointment(
        site_id = sample_site.id,
        trailer_id = drytrailer.id,
        prefered_id = spot.id
    )
    assert appt.yard_spot_id == spot.id

def test_no_avaialble_spot(sample_site,drytrailer):
    for i in range(4):
        AppointmentFactory.create_appointment(
            site_id = sample_site.id,
            trailer_id = drytrailer.id
        )
    with pytest.raises(ValueError):
        AppointmentFactory.create_checkin(
            site_id = sample_site.id,
            trailer_id = drytrailer.id
        )

