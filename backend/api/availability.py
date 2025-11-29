from flask_restful import Resource
from flask import request
from models import DoctorAvailability
from database import get_db_session
from utils.auth import role_required

class DoctorAvailabilityAPI(Resource):

    @role_required("doctor")
    def post(self):
        data = request.json
        session = get_db_session()

        slot = DoctorAvailability(
            doctor_id=data["doctor_id"],
            day_of_week=data["day"],
            start_time=data["start"],
            end_time=data["end"]
        )
        session.add(slot)
        session.commit()

        return {"message": "Availability added"}, 201


    def get(self, doctor_id):
        session = get_db_session()
        slots = session.query(DoctorAvailability).filter_by(doctor_id=doctor_id).all()

        return [{
            "day": s.day_of_week,
            "from": str(s.start_time),
            "to": str(s.end_time)
        } for s in slots]
