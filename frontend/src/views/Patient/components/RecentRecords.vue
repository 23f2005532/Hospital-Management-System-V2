<script setup>
defineProps({
  items: Array,
  loading: Boolean
});
</script>

<template>
  <section class="card">
    <h3>Your Recent Medical Records</h3>

    <div v-if="loading" class="muted">Loading...</div>

    <ul v-else-if="items.length" class="list">
      <li v-for="r in items" :key="r.id">
        <div class="top">
          <span class="doctor">{{ r.doctor_name }}</span>
          <span class="date">{{ r.date }}</span>
        </div>
        <p class="diagnosis">Diagnosis: {{ r.diagnosis }}</p>
      </li>
    </ul>

    <p v-else class="muted">No recent records.</p>
  </section>
</template>

<style scoped>
.card {
  background: white;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  padding: 16px;
}
.list {
  list-style: none;
  margin: 0;
  padding: 0;
}
li {
  padding: 8px 0;
  border-bottom: 1px solid #e2e8f0;
}
.doctor {
  font-weight: bold;
}
.date {
  float: right;
  color: #64748b;
}
.diagnosis {
  margin-top: 4px;
  font-size: 14px;
}
.muted {
  color: #64748b;
  font-size: 14px;
}
</style>
