import pytest
from yardops.factories.appointment_factory import AppointmentFactory
from yardops.models.trailer import Trailer
from yardops.extensions import db

def test_success_checkin(app , sample_site,drytrailer):
    appt = AppointmentFactory.create_checkin(
        site_id = sample_site.id,
        trailer_id = drytrailer.id
    )
    assert appt.status == "CHECKED_IN"
    
def test_prefered_spot_works(app , sample_site,drytrailer):
    spot = sample_site.yard_spots[0]
    appt = AppointmentFactory.create_checkin(
        site_id = sample_site.id,
        trailer_id = drytrailer.id,
        preferred_spot_id = spot.id
    )
    assert appt.yard_spot_id == spot.id

# def test_no_avaialble_spot(app, sample_site):
#     trailers = []

#     for i in range(4):
#         trailer = Trailer(
#             trailer_number=str(i),
#             trailer_type="DRY",
#             carrier_name="test"
#         )
#         db.session.add(trailer)
#         db.session.commit()
#         trailers.append(trailer)

#     for trailer in trailers:
#         AppointmentFactory.create_checkin(
#             site_id=sample_site.id,
#             trailer_id=trailer.id
#         )

#     new_trailer = Trailer(
#         trailer_number="999",
#         trailer_type="DRY",
#         carrier_name="test"
#     )
#     db.session.add(new_trailer)
#     db.session.commit()

#     with pytest.raises(ValueError):
#         AppointmentFactory.create_checkin(
#             site_id=sample_site.id,
#             trailer_id=new_trailer.id
#         )
