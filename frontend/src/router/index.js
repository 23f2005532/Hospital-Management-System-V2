import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '../store/auth'
import Register from '@/views/auth/Register.vue'
import Dashboard from '@/views/Dashboard.vue'
import Home from '@/views/Home.vue'
import MyAppointments from '@/views/Doctor/MyAppointments.vue'
import PatientLogin from '@/views/auth/PatientLogin.vue'
import DoctorLogin from '@/views/auth/DoctorLogin.vue'
import PatientDashboard from '@/views/Patient/PatientDashboard.vue'
import BookAppointment from '@/views/Patient/BookAppointment.vue'
import PatientAppointments from '@/views/Patient/PatientAppointments.vue'
import PatientProfile from '@/views/Patient/PatientProfile.vue'
import PatientRecords from '@/views/Patient/PatientRecords.vue'
import AdminLogin from '@/views/auth/AdminLogin.vue'
import AdminDashboard from '@/views/Admin/AdminDashboard.vue'
import DoctorsList from '@/views/Admin/doctors/DoctorsList.vue'
import PatientList from '@/views/Admin/patients/PatientList.vue'
import AppointmentsList from '@/views/Admin/appointments/AppointmentsList.vue'
import AddDoctor from '@/views/Admin/doctors/AddDoctor.vue'
import EditDoctor from '@/views/Admin/doctors/EditDoctor.vue'
import PatientEdit from '@/views/Admin/patients/PatientEdit.vue'
import SpecializationList from '@/views/Admin/specializations/SpecializationList.vue'
import SpecializationCreate from '@/views/Admin/specializations/SpecializationCreate.vue'
import SpecializationEdit from '@/views/Admin/specializations/SpecializationEdit.vue'

const routes = [
  // General Routes
  { path: "/", component: Home },
  { path: '/dashboard', component: Dashboard },



  // Auth Routes
  { path: "/register", component: Register },
  { path: "/login/patient", component: PatientLogin},
  {path: "/login/doctor", component: DoctorLogin},
  { path: "/login/admin", component: AdminLogin},
  
  
  
  // Admin Routes
  { path: "/admin/dashboard", component: AdminDashboard },
  { path: "/admin/doctors", component: DoctorsList },
  { path: "/admin/doctors/add", component: AddDoctor },
  { path: "/admin/doctors/edit/:id", component: EditDoctor },
  { path: "/admin/patients", component: PatientList },
  { path: "/admin/patients/:id/edit", component: PatientEdit },
  { path: "/admin/appointments", component: AppointmentsList },
  { path: "/admin/specializations", component: SpecializationList },
  { path: "/admin/specializations/create", component: SpecializationCreate },
  { path: "/admin/specializations/:id/edit", component: SpecializationEdit },





  // Doctor Routes
  {
    path: '/doctor/appointments',
    component: MyAppointments,
    meta: { role: 'doctor' },
  },


  // Patient Routes
  { path: "/patient/dashboard", component: PatientDashboard },
  { path: "/patient/book", component: BookAppointment },
  { path: "/patient/appointments", component: PatientAppointments },
  { path: "/patient/profile", component: PatientProfile },
  { path: "/patient/records", component: PatientRecords },
  

]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const auth = useAuthStore();
  const publicPages = ["/","/login/patient", "/login/doctor", "/login/admin", "/register"];

  // Allow public pages
  if (!auth.token && publicPages.includes(to.path)) {
    return next();
  }

  // Block protected pages
  if (!auth.token && !publicPages.includes(to.path)) {
    return next("/");
  }

  // Role-based protection
  if (to.meta.role && to.meta.role !== auth.role) {
    return next("/dashboard");
  }

  next();
});


export default router
