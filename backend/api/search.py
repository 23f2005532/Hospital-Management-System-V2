from flask_restful import Resource
from flask import request
from models import DoctorProfile
from database import get_db_session

class SearchDoctors(Resource):
    def get(self):
        specialization = request.args.get("specialization")
        session = get_db_session()

        q = session.query(DoctorProfile)

        if specialization:
            q = q.join(DoctorProfile.specialization).filter_by(name=specialization)

        docs = q.all()

        return [{
            "id": d.id,
            "name": d.user.name,
            "specialization": d.specialization.name
        } for d in docs]
