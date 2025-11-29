<script setup>
import { ref, onMounted } from "vue";
import patientAPI from "@/api/patient";

const appointments = ref([]);
const loading = ref(true);

onMounted(async () => {
  try {
    const res = await patientAPI.getAppointments();
    appointments.value = res.data;
  } catch (err) {
    console.error(err);
  }
  loading.value = false;
});
</script>

<template>
  <div class="page">
    <h2>My Appointments</h2>

    <div class="card">
      <div v-if="loading">Loading appointments...</div>

      <table v-else class="table">
        <thead>
          <tr>
            <th>Date</th>
            <th>Time</th>
            <th>Doctor</th>
            <th>Specialization</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="a in appointments" :key="a.id">
            <td>{{ a.date }}</td>
            <td>{{ a.time }}</td>
            <td>{{ a.doctor_name }}</td>
            <td>{{ a.specialization }}</td>
            <td>
              <span class="badge" :class="a.status.toLowerCase()">
                {{ a.status }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
.page {
  padding: 20px;
}

.card {
  background: white;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  padding: 16px;
}

.table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 10px;
  border-bottom: 1px solid #e2e8f0;
  text-align: left;
}

.badge {
  padding: 4px 10px;
  border-radius: 8px;
  color: white;
  font-size: 12px;
}

.completed {
  background: #10b981;
}

.scheduled {
  background: #3b82f6;
}

.canceled {
  background: #ef4444;
}
</style>
