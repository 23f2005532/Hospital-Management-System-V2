<script setup>
defineProps({
  title: String,
  value: [String, Number],
  description: String
});
</script>

<template>
  <div class="card">
    <div class="value">{{ value }}</div>
    <div class="title">{{ title }}</div>
    <div v-if="description" class="desc">{{ description }}</div>
  </div>
</template>

<style scoped>
.card {
  background: white;
  border: 1px solid #e2e8f0;
  padding: 14px;
  border-radius: 10px;
  flex: 1;
  min-width: 180px;
}
.value {
  font-size: 22px;
  font-weight: bold;
  color: #1d3557;
}
.title {
  margin-top: 6px;
  font-size: 14px;
  color: #475569;
}
.desc {
  font-size: 12px;
  color: #64748b;
  margin-top: 4px;
}
</style>
