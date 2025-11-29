from database import db

class Prescription(db.Model):
    __tablename__ = "prescriptions"

    id = db.Column(db.Integer, primary_key=True)
    treatment_id = db.Column(db.Integer, db.ForeignKey("treatments.id"))

    medicine_name = db.Column(db.String(120), nullable=False)
    dosage = db.Column(db.String(120), nullable=False)
    duration = db.Column(db.String(120))
    instructions = db.Column(db.Text)

    treatment = db.relationship("Treatment", back_populates="prescriptions")
