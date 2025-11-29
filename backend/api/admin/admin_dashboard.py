from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from database import get_db_session
from models import User, UserRole, Appointment, DoctorProfile
from datetime import date

# Utility: Validate admin access based on JWT claims
def require_admin():
    claims = get_jwt()
    role = claims.get("role")  # e.g. "ADMIN" / "DOCTOR" / "PATIENT" or lowercase
    if not role:
        return False
    return role.upper() == "ADMIN"


class AdminDashboard(Resource):
    @jwt_required()
    def get(self):
        # Check that the caller is an admin
        if not require_admin():
            return {"message": "Admin access only"}, 403

        session = get_db_session()

        # Total users by role
        total_doctors = session.query(User).filter_by(role=UserRole.DOCTOR).count()
        total_patients = session.query(User).filter_by(role=UserRole.PATIENT).count()

        # Appointments stats
        total_appointments = session.query(Appointment).count()

        completed = (
            session.query(Appointment)
            .filter(Appointment.status == "COMPLETED")
            .count()
        )

        today_count = (
            session.query(Appointment)
            .filter(Appointment.date == date.today())
            .count()
        )

        # Doctor Verification Pending
        pending_verification = (
            session.query(DoctorProfile)
            .filter(DoctorProfile.is_verified == False)
            .count()
        )

        # Recent 10 appointments (newest first)
        recent = (
            session.query(Appointment)
            .order_by(Appointment.date.desc(), Appointment.time.desc())
            .limit(10)
            .all()
        )

        recent_list = [
            {
                "id": a.id,
                "doctor": a.doctor.user.name if a.doctor and a.doctor.user else "",
                "patient": a.patient.user.name if a.patient and a.patient.user else "",
                "date": str(a.date),
                "time": str(a.time),
                "status": a.status,
            }
            for a in recent
        ]

        return {
            "stats": {
                "doctors": total_doctors,
                "patients": total_patients,
                "appointments": total_appointments,
                "completed": completed,
                "pendingVerifications": pending_verification,
                "today": today_count,
            },
            "recentAppointments": recent_list,
        }, 200
