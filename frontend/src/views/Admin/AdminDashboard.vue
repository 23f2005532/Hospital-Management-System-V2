<script setup>
import { ref, onMounted } from "vue";
import StatCard from "./components/StatCard.vue";
import AdminSection from "./components/AdminSection.vue";
import AdminTable from "./components/AdminTable.vue";

import adminAPI from "@/api/admin";

const loading = ref(true);
const stats = ref({
  doctors: 0,
  patients: 0,
  appointments: 0,
  completed: 0,
  pendingVerifications: 0,
  today: 0
});

const recentAppointments = ref([]);

onMounted(async () => {
  try {
    const res = await adminAPI.dashboard();
    stats.value = res.data.stats;
    recentAppointments.value = res.data.recentAppointments;
  } catch (err) {
    console.error(err);
  }
  loading.value = false;
});
</script>

<template>
  <div class="page">
    <h2>Admin Dashboard</h2>

    <!-- KPI Cards -->
    <div class="grid">
      <StatCard title="Doctors" :value="stats.doctors" icon="fa fa-user-md" />
      <StatCard title="Patients" :value="stats.patients" icon="fa fa-users" />
      <StatCard title="Appointments" :value="stats.appointments" icon="fa fa-calendar" />
      <StatCard title="Completed" :value="stats.completed" icon="fa fa-check-circle" />
      <StatCard title="Pending Verifications" :value="stats.pendingVerifications" icon="fa fa-exclamation-circle" />
      <StatCard title="Today’s Appointments" :value="stats.today" icon="fa fa-clock" />
    </div>

    <!-- Recent Appointments -->
    <AdminSection title="Recent Appointments">
      <AdminTable
        :columns="['Date', 'Doctor', 'Patient', 'Status']"
        :rows="recentAppointments"
      />
    </AdminSection>

  </div>
</template>

<style scoped>
.page {
  padding: 20px;
  max-width: 1200px;
  margin: auto;
}
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
  margin-bottom: 24px;
}
</style>
