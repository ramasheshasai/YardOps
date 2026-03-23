from yardops.models.appointment import Appointment
from yardops.models.trailer import Trailer
from yardops.models.yard_spot import YardSpot
from yardops.extensions import db
import uuid
from yardops.errors import(
    TrailerNotFoundError,
    TrailerAlreadyCheckedInError,
    NoAvailableSpotError,
    SpotOccupiedError
)

class AppointmentFactory:

    @staticmethod
    def create_checkin(site_id,trailer_id,preferred_spot_id = None,db_session = None):

        trailer = Trailer.query.get(trailer_id)
        if not trailer:
            raise TrailerNotFoundError("trailer not found")
        
        exists = Appointment.query.filter_by(
            trailer_id = trailer_id,
            status = "CHECKED_IN"
        ).first()

        if exists:
            raise TrailerAlreadyCheckedInError("trailer Already there")
        
            
        if preferred_spot_id:
            spot = YardSpot.query.get(preferred_spot_id)

            if not spot:
                raise NoAvailableSpotError("spot is not available")
            if spot.is_occupied:
                raise SpotOccupiedError("spot is occupied")
        else:
            spot = YardSpot.query.filter_by(
                site_id = site_id,
                is_occupied = False
            ).first()

            if not spot:
                raise NoAvailableSpotError("no available spot")
        
        gate_pass = uuid.uuid4().hex[:8]

        appointment = Appointment(
            trailer_id = trailer_id,
            site_id = site_id,
            yard_spot_id = spot.id,
            gate_pass = gate_pass,
            status = "CHECKED_IN"
        )

        spot.is_occupied = True

        db.session.add(appointment)
        db.session.commit()

        return appointment



        

