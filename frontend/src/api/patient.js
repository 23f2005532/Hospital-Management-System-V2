// src/api/patient.js
import axios from "@/utils/axios";

export default {
  // Dashboard summary (stats + upcoming + recent data)
  dashboard() {
    return axios.get("/patient/dashboard");
  },

  // Get all appointments of the patient
  getAppointments() {
    return axios.get("/patient/appointments");
  },

  // Get single appointment details
  getAppointment(id) {
    return axios.get(`/patient/appointments/${id}`);
  },

  // Book appointment
  bookAppointment(data) {
    return axios.post("/patient/appointments", data);
  },

  // Get all available doctors
  getDoctors() {
    return axios.get("/patient/doctors");
  },

  // Get availability of a doctor (date → time slots)
  getDoctorAvailability(doctorId, date) {
    return axios.get(`/patient/doctors/${doctorId}/availability`, {
      params: { date }
    });
  },

  // Medical records
  getRecords() {
    return axios.get("/patient/records");
  },

  // Single record details
  getRecord(id) {
    return axios.get(`/patient/records/${id}`);
  },

  // Patient profile
  getProfile() {
    return axios.get("/patient/profile");
  },

  updateProfile(data) {
    return axios.put("/patient/profile", data);
  }
};
