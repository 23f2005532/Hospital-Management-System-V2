<script setup>
defineProps({
  appointment: Object,
  loading: Boolean
});
</script>

<template>
  <section class="card">
    <h3>Upcoming Appointment</h3>

    <div v-if="loading" class="loading">Loading...</div>

    <div v-else-if="appointment">
      <p><strong>Doctor:</strong> {{ appointment.doctor_name }}</p>
      <p><strong>Date:</strong> {{ appointment.date }}</p>
      <p><strong>Time:</strong> {{ appointment.time }}</p>
      <p><strong>Status:</strong> {{ appointment.status }}</p>

      <button @click="$router.push('/patient/my-appointments')">
        View All Appointments
      </button>
    </div>

    <div v-else class="empty">
      <p>You have no upcoming appointments.</p>
      <button @click="$router.push('/patient/book')">
        Book Appointment
      </button>
    </div>
  </section>
</template>

<style scoped>
.card {
  background: white;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  padding: 16px;
}
h3 {
  margin-bottom: 10px;
}
.loading {
  color: #64748b;
  font-size: 14px;
}
.empty {
  color: #475569;
  font-size: 14px;
}
button {
  margin-top: 12px;
  background: #1d3557;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
}
button:hover {
  background: #0f2238;
}
</style>
