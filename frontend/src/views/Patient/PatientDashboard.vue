<script setup>
import { ref, onMounted } from "vue";
import PatientWelcome from "./components/PatientWelcome.vue";
import PatientStatCard from "./components/PatientStatCard.vue";
import QuickActions from "./components/QuickActions.vue";
import UpcomingAppointmentCard from "./components/UpcomingAppointmentCard.vue";
import RecentAppointments from "./components/RecentAppointments.vue";
import RecentRecords from "./components/RecentRecords.vue";

import patientAPI from "@/api/patient";
import { useAuthStore } from "@/store/auth";

const auth = useAuthStore();

const loading = ref(true);

// Dashboard data
const stats = ref({
  upcoming: 0,
  total: 0,
  completed: 0,
});

const upcomingAppointment = ref(null);
const recentAppointments = ref([]);
const recentRecords = ref([]);

onMounted(async () => {
  loading.value = true;
  try {
    const res = await patientAPI.dashboard();

    stats.value.upcoming = res.data.stats.upcoming;
    stats.value.total = res.data.stats.total;
    stats.value.completed = res.data.stats.completed;

    upcomingAppointment.value = res.data.upcomingAppointment;
    recentAppointments.value = res.data.recentAppointments;
    recentRecords.value = res.data.recentRecords;
  } catch (err) {
    console.error("Dashboard load error", err);
  }
  loading.value = false;
});
</script>

<template>
  <div class="page">

    <!-- Welcome Header -->
    <PatientWelcome :name="auth.user?.name || 'Patient'" />

    <!-- Stats Section -->
    <section class="stats-section">
      <PatientStatCard
        title="Upcoming Appointments"
        :value="stats.upcoming"
        description="Scheduled visits"
      />
      <PatientStatCard
        title="Total Appointments"
        :value="stats.total"
        description="All-time hospital visits"
      />
      <PatientStatCard
        title="Completed"
        :value="stats.completed"
        description="Finished consultations"
      />
    </section>

    <!-- Two-column layout -->
    <section class="grid-2">
      <UpcomingAppointmentCard
        :appointment="upcomingAppointment"
        :loading="loading"
      />

      <QuickActions />
    </section>

    <!-- Recent Appointments -->
    <RecentAppointments
      :items="recentAppointments"
      :loading="loading"
    />

    <!-- Recent Records -->
    <RecentRecords
      :items="recentRecords"
      :loading="loading"
    />

  </div>
</template>

<style scoped>
.page {
  padding: 22px;
  max-width: 1200px;
  margin: auto;
}

/* Stats row */
.stats-section {
  margin-top: 20px;
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

/* Two-column block */
.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin: 20px 0;
}

@media (max-width: 840px) {
  .grid-2 {
    grid-template-columns: 1fr;
  }
}
</style>
