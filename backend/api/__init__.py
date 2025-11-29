from .auth import Register, Login
from .doctors import DoctorList
from .availability import DoctorAvailabilityAPI
from .appointments import AppointmentAPI
from .treatments import TreatmentAPI
from .search import SearchDoctors
from .reports import MonthlyReport
from .admin.admin_dashboard import AdminDashboard
from .admin.admin_appointments import AdminAppointments, AdminAppointmentDetail
from .admin.admin_doctors import AdminDoctors, AdminDoctorDetail, AdminDoctorVerify, AdminDoctorToggleActive,AdminDoctorAvailability, AdminDoctorAvailabilityDetail
from .admin.admin_specialization import AdminSpecializations, AdminSpecializationDetail
from .admin.admin_patient import AdminPatients, AdminPatientDetail, AdminPatientToggle

def register_routes(api):
    api.add_resource(Register, "/auth/register")
    api.add_resource(Login, "/auth/login")
    # -------------admin-------------------------
    api.add_resource(AdminDashboard, "/admin/dashboard")
    # SPECIALIZATIONS
    api.add_resource(AdminSpecializations, "/admin/specializations")
    api.add_resource(AdminSpecializationDetail, "/admin/specializations/<int:spec_id>")

    # DOCTORS
    api.add_resource(AdminDoctors, "/admin/doctors")
    api.add_resource(AdminDoctorDetail, "/admin/doctors/<int:doc_id>")
    api.add_resource(AdminDoctorVerify, "/admin/doctors/<int:doc_id>/verify")
    api.add_resource(AdminDoctorToggleActive, "/admin/doctors/<int:doc_id>/toggle")

    # Availability
    api.add_resource(AdminDoctorAvailability, "/admin/doctors/<int:doc_id>/availability")
    api.add_resource(AdminDoctorAvailabilityDetail, "/admin/doctors/<int:doc_id>/availability/<int:slot_id>")

    # APPOINTMENTS
    api.add_resource(AdminAppointments, "/admin/appointments")
    api.add_resource(AdminAppointmentDetail, "/admin/appointments/<int:appt_id>")

    # PATIENTS
    api.add_resource(AdminPatients, "/admin/patients")
    api.add_resource(AdminPatientDetail, "/admin/patients/<int:patient_id>")
    api.add_resource(AdminPatientToggle, "/admin/patients/<int:patient_id>/toggle")

    
    api.add_resource(DoctorList, "/doctors")

    api.add_resource(DoctorAvailabilityAPI, "/doctors/availability", "/doctors/<int:doctor_id>/availability")

    api.add_resource(AppointmentAPI, "/appointments")

    api.add_resource(TreatmentAPI, "/treatments", "/treatments/<int:patient_id>")

    api.add_resource(SearchDoctors, "/search/doctors")

    api.add_resource(MonthlyReport, "/reports/monthly")

