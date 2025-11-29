from flask_restful import Resource
from flask import request
from models import Appointment
from database import get_db_session
from datetime import datetime
from utils.auth import role_required

class MonthlyReport(Resource):
    @role_required("admin", "doctor")
    def get(self):
        doctor_id = request.args.get("doctor_id")
        month = int(request.args.get("month"))
        year = int(request.args.get("year"))

        session = get_db_session()

        appointments = session.query(Appointment).filter(
            Appointment.doctor_id == doctor_id,
            Appointment.date >= datetime(year, month, 1),
            Appointment.date <= datetime(year, month, 28)
        ).all()

        return {
            "total_appointments": len(appointments),
            "completed": len([a for a in appointments if a.status.name == "COMPLETED"]),
            "cancelled": len([a for a in appointments if a.status.name == "CANCELLED"])
        }
