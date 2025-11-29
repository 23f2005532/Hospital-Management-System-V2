# models/__init__.py

from database import db

# Import all models so SQLAlchemy + Alembic can detect them
from .user import User, UserRole
from .patient import PatientProfile
from .doctor import DoctorProfile
from .specialization import Specialization
from .doctor_availability import DoctorAvailability
from .appointment import Appointment, AppointmentStatus
from .treatment import Treatment
from .prescription import Prescription

__all__ = [
    "db",
    "User",
    "UserRole",
    "PatientProfile",
    "DoctorProfile",
    "Specialization",
    "DoctorAvailability",
    "Appointment",
    "AppointmentStatus",
    "Treatment",
    "Prescription",
]
