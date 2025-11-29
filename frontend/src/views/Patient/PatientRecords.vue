<script setup>
import { ref, onMounted } from "vue";
import patientAPI from "@/api/patient";

const records = ref([]);
const loading = ref(true);

onMounted(async () => {
  try {
    const res = await patientAPI.getRecords();
    records.value = res.data;
  } catch (err) {
    console.error(err);
  }
  loading.value = false;
});
</script>

<template>
  <div class="page">
    <h2>Medical Records</h2>

    <div class="card">
      <div v-if="loading">Loading records...</div>

      <div
        v-else-if="records.length === 0"
        class="empty"
      >
        No medical records found.
      </div>

      <ul v-else class="list">
        <li v-for="r in records" :key="r.id">
          <div class="top">
            <span class="doctor">{{ r.doctor_name }}</span>
            <span class="date">{{ r.date }}</span>
          </div>
          <p class="diagnosis">Diagnosis: {{ r.diagnosis }}</p>
        </li>
      </ul>
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

.empty {
  color: #64748b;
  font-size: 14px;
}

.list {
  list-style: none;
  padding: 0;
}

li {
  padding: 12px 0;
  border-bottom: 1px solid #e2e8f0;
}

.doctor {
  font-weight: bold;
}

.date {
  float: right;
  color: #64748b;
}
</style>
