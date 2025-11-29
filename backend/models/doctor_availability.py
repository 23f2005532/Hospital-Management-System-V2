from database import db

class DoctorAvailability(db.Model):
    __tablename__ = "doctor_availability"

    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctor_profiles.id"))

    day_of_week = db.Column(db.String(20), nullable=False)  # Monday, Tuesday etc.
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)

    doctor = db.relationship("DoctorProfile", back_populates="availability")
