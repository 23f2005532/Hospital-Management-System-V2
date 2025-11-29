<script setup></script>

<template>
  <section class="card">
    <h3>Quick Actions</h3>

    <div class="grid">
      <button @click="$router.push('/patient/book')">
        Book Appointment
      </button>
      <button @click="$router.push('/patient/appointments')">
        View Appointments
      </button>
      <button @click="$router.push('/patient/records')">
        Medical Records
      </button>
      <button @click="$router.push('/patient/profile')">
        Edit Profile
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
  margin: 0 0 12px;
  font-size: 15px;
}
.grid {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}
button {
  flex: 1;
  min-width: 150px;
  padding: 10px;
  background: #1d3557;
  color: white;
  border-radius: 8px;
  border: none;
  cursor: pointer;
}
button:hover {
  background: #0f2238;
}
</style>
