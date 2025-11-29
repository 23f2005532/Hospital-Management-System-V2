from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt
from database import get_db_session
from models import Appointment

def require_admin():
    return get_jwt().get("role", "").upper() == "ADMIN"


appt_parser = reqparse.RequestParser()
appt_parser.add_argument("doctor_id", type=int)
appt_parser.add_argument("patient_id", type=int)
appt_parser.add_argument("date")
appt_parser.add_argument("time")
appt_parser.add_argument("status")


class AdminAppointments(Resource):

    @jwt_required()
    def get(self):
        if not require_admin():
            return {"message": "Admin only"}, 403

        session = get_db_session()
        appts = session.query(Appointment).all()

        return [
            {
                "id": a.id,
                "doctor": a.doctor.user.name if a.doctor else "",
                "patient": a.patient.user.name if a.patient else "",
                "date": str(a.date),
                "time": str(a.time),
                "status": a.status,
            }
            for a in appts
        ], 200

    @jwt_required()
    def post(self):
        if not require_admin():
            return {"message": "Admin only"}, 403

        data = appt_parser.parse_args()
        session = get_db_session()

        appt = Appointment(
            doctor_id=data["doctor_id"],
            patient_id=data["patient_id"],
            date=data["date"],
            time=data["time"],
            status=data.get("status", "PENDING")
        )

        session.add(appt)
        session.commit()

        return {"message": "Appointment created", "id": appt.id}, 201


class AdminAppointmentDetail(Resource):

    @jwt_required()
    def put(self, appt_id):
        if not require_admin():
            return {"message": "Admin only"}, 403

        data = appt_parser.parse_args()
        session = get_db_session()

        appt = session.query(Appointment).get(appt_id)
        if not appt:
            return {"message": "Not found"}, 404

        for key, value in data.items():
            if value is not None:
                setattr(appt, key, value)

        session.commit()
        return {"message": "Updated"}, 200

    @jwt_required()
    def delete(self, appt_id):
        if not require_admin():
            return {"message": "Admin only"}, 403

        session = get_db_session()
        appt = session.query(Appointment).get(appt_id)

        if not appt:
            return {"message": "Not found"}, 404

        session.delete(appt)
        session.commit()

        return {"message": "Deleted"}, 200
