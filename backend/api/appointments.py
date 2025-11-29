from flask_restful import Resource
from flask import request
from models import Appointment, AppointmentStatus, PatientProfile
from database import get_db_session
from utils.auth import role_required
from datetime import datetime, time

class AppointmentAPI(Resource):

    @role_required("patient")
    def post(self):
        data = request.json
        session = get_db_session()

        appointment = Appointment(
            patient_id=data["patient_id"],
            doctor_id=data["doctor_id"],
            date=datetime.strptime(data["date"], "%Y-%m-%d").date(),
            time=datetime.strptime(data["time"], "%H:%M").time(),
            status=AppointmentStatus.PENDING
        )
        session.add(appointment)
        session.commit()

        return {"message": "Appointment booked"}, 201


    @role_required("doctor", "patient", "admin")
    def get(self):
        session = get_db_session()
        doctor_id = request.args.get("doctor_id")
        patient_id = request.args.get("patient_id")

        q = session.query(Appointment)

        if doctor_id:
            q = q.filter_by(doctor_id=doctor_id)
        if patient_id:
            q = q.filter_by(patient_id=patient_id)

        appointments = q.all()

        return [{
            "id": a.id,
            "date": str(a.date),
            "time": str(a.time),
            "status": a.status.value
        } for a in appointments]
