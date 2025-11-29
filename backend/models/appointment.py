from database import db
import enum

class AppointmentStatus(enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Appointment(db.Model):
    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)

    patient_id = db.Column(db.Integer, db.ForeignKey("patient_profiles.id"))
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctor_profiles.id"))

    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)

    status = db.Column(db.Enum(AppointmentStatus), default=AppointmentStatus.PENDING)

    notes = db.Column(db.Text)

    patient = db.relationship("PatientProfile", back_populates="appointments")
    doctor = db.relationship("DoctorProfile", back_populates="appointments")

    treatment = db.relationship("Treatment", uselist=False, back_populates="appointment")
