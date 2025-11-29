from flask_restful import Resource
from flask import request
from models import Treatment, Prescription
from database import get_db_session
from utils.auth import role_required

class TreatmentAPI(Resource):

    @role_required("doctor")
    def post(self):
        data = request.json
        session = get_db_session()

        treatment = Treatment(
            appointment_id=data["appointment_id"],
            diagnosis=data["diagnosis"],
            doctor_notes=data.get("notes")
        )
        session.add(treatment)
        session.flush()

        for p in data.get("prescriptions", []):
            pres = Prescription(
                treatment_id=treatment.id,
                medicine_name=p["medicine"],
                dosage=p["dosage"],
                duration=p["duration"],
                instructions=p.get("instructions")
            )
            session.add(pres)

        session.commit()
        return {"message": "Treatment saved"}, 201

    @role_required("doctor", "patient")
    def get(self, patient_id):
        session = get_db_session()
        treatments = session.execute("""
            SELECT t.id, t.diagnosis, t.doctor_notes
            FROM treatments t
            JOIN appointments a ON t.appointment_id = a.id
            WHERE a.patient_id = :pid
        """, {"pid": patient_id}).fetchall()

        return [dict(row) for row in treatments]
