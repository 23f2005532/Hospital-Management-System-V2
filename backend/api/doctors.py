from flask_restful import Resource
from flask import request
from models import User, UserRole, DoctorProfile, Specialization
from database import get_db_session
from utils.auth import role_required

class DoctorList(Resource):
    @role_required("admin")
    def post(self):
        data = request.json
        session = get_db_session()

        user = User(
            name=data["name"],
            email=data["email"],
            password=data["password"],
            role=UserRole.DOCTOR
        )
        session.add(user)
        session.flush()

        doc = DoctorProfile(
            user_id=user.id,
            specialization_id=data["specialization_id"],
            experience_years=data.get("experience", 0)
        )
        session.add(doc)
        session.commit()

        return {"message": "Doctor profile created"}, 201

    def get(self):
        session = get_db_session()
        docs = session.query(DoctorProfile).all()

        return [{
            "id": d.id,
            "name": d.user.name,
            "specialization": d.specialization.name
        } for d in docs]
