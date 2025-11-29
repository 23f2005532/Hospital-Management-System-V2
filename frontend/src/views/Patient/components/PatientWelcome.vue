<script setup>
defineProps({
  name: { type: String, default: "Patient" }
});
</script>

<template>
  <section class="welcome">
    <div class="content">
      <p class="small">Welcome back,</p>
      <h2>{{ name }}</h2>
      <p class="sub">Here is your health summary for today.</p>
    </div>
    <div class="badge">Patient Portal</div>
  </section>
</template>

<style scoped>
.welcome {
  background: #1d3557;
  color: white;
  padding: 22px;
  border-radius: 14px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.small {
  margin: 0;
  opacity: 0.75;
  font-size: 13px;
}
h2 {
  margin: 4px 0;
  font-size: 24px;
}
.sub {
  margin: 0;
  opacity: 0.85;
  font-size: 14px;
}
.badge {
  padding: 8px 16px;
  border-radius: 20px;
  background: rgba(255,255,255,0.15);
  font-size: 13px;
}
</style>
