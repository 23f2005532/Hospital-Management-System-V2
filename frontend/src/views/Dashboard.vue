<script setup>
import { useAuthStore } from "@/store/auth";
import { useRouter } from "vue-router";

const auth = useAuthStore();
const router = useRouter();

// Cards for each role
const adminLinks = [
  { title: "Manage Doctors", route: "/admin/doctors" },
  { title: "Reports", route: "/admin/reports" },
];

const doctorLinks = [
  { title: "My Appointments", route: "/doctor/appointments" },
  { title: "Set Availability", route: "/doctor/availability" },
  { title: "Treatment Records", route: "/doctor/treatments" },
];

const patientLinks = [
  { title: "Book Appointment", route: "/patient/book" },
  { title: "My Appointments", route: "/patient/appointments" },
  { title: "Medical History", route: "/patient/history" },
];

const navigate = (route) => {
  router.push(route);
};
</script>

<template>
  <div class="dashboard">
    <h2 class="welcome">Welcome, {{ auth.role.toUpperCase() }}</h2>

    <!-- ROLE-BASED SECTIONS -->
    <div class="cards">

      <!-- Admin View -->
      <template v-if="auth.role === 'admin'">
        <div
          v-for="item in adminLinks"
          :key="item.title"
          class="card"
          @click="navigate(item.route)"
        >
          <h3>{{ item.title }}</h3>
        </div>
      </template>

      <!-- Doctor View -->
      <template v-else-if="auth.role === 'doctor'">
        <div
          v-for="item in doctorLinks"
          :key="item.title"
          class="card"
          @click="navigate(item.route)"
        >
          <h3>{{ item.title }}</h3>
        </div>
      </template>

      <!-- Patient View -->
      <template v-else-if="auth.role === 'patient'">
        <div
          v-for="item in patientLinks"
          :key="item.title"
          class="card"
          @click="navigate(item.route)"
        >
          <h3>{{ item.title }}</h3>
        </div>
      </template>

    </div>
  </div>
</template>

<style scoped>
.dashboard {
  padding: 20px;
}

.welcome {
  font-size: 24px;
  margin-bottom: 20px;
}

.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.card {
  width: 220px;
  padding: 20px;
  background: #f1f1f1;
  border-radius: 8px;
  cursor: pointer;
  transition: 0.2s;
  text-align: center;
  border: 1px solid #ccc;
}

.card:hover {
  background: #e8e8e8;
  transform: translateY(-3px);
}

.card h3 {
  margin: 0;
  font-size: 18px;
}
</style>
