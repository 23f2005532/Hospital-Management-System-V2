from database import db

class Treatment(db.Model):
    __tablename__ = "treatments"

    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey("appointments.id"))

    diagnosis = db.Column(db.Text, nullable=False)
    doctor_notes = db.Column(db.Text)

    appointment = db.relationship("Appointment", back_populates="treatment")

    prescriptions = db.relationship("Prescription", back_populates="treatment", cascade="all, delete-orphan")
