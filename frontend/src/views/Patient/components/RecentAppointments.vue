<script setup>
defineProps({
  items: Array,
  loading: Boolean
});
</script>

<template>
  <section class="card">
    <h3>Recent Appointments</h3>

    <div v-if="loading" class="muted">Loading...</div>

    <table v-else-if="items.length" class="table">
      <thead>
        <tr>
          <th>Date</th>
          <th>Doctor</th>
          <th>Specialization</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="a in items" :key="a.id">
          <td>{{ a.date }}</td>
          <td>{{ a.doctor_name }}</td>
          <td>{{ a.specialization }}</td>
          <td>{{ a.status }}</td>
        </tr>
      </tbody>
    </table>

    <p v-else class="muted">No recent appointments.</p>
  </section>
</template>

<style scoped>
.card {
  background: white;
  border-radius: 12px;
  padding: 16px;
  border: 1px solid #e2e8f0;
}
h3 {
  margin-bottom: 10px;
}
.table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  padding: 6px 8px;
  border-bottom: 1px solid #e2e8f0;
}
.muted {
  color: #64748b;
  font-size: 14px;
}
</style>
