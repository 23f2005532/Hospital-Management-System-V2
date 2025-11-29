from database import db

class DoctorProfile(db.Model):
    __tablename__ = "doctor_profiles"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True)

    # Basic doctor info
    full_name = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    age = db.Column(db.Integer)

    # Professional info
    specialization_id = db.Column(db.Integer, db.ForeignKey("specializations.id"), nullable=False)
    experience_years = db.Column(db.Integer, default=0)
    qualification = db.Column(db.String(255))      # MBBS, MD, etc
    bio = db.Column(db.Text)                       # short profile summary
    consultation_fee = db.Column(db.Float, default=0.0)

    # Status flags
    is_active = db.Column(db.Boolean, default=True)       # Approved by admin
    is_verified = db.Column(db.Boolean, default=False)    # Document verification

    # Availability & appointments
    specialization = db.relationship("Specialization", back_populates="doctors")

    availability = db.relationship(
        "DoctorAvailability",
        back_populates="doctor",
        cascade="all, delete-orphan"
    )

    appointments = db.relationship(
        "Appointment",
        back_populates="doctor",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<DoctorProfile {self.full_name} ({self.id})>"
