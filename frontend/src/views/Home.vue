<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

const goToLogin = () => router.push("/login");
const goToRegister = () => router.push("/register");
</script>

<template>
  <div class="home">

    <!-- HERO SECTION -->
    <section class="hero">
      <div class="hero-content">
        <h1>Smart Hospital Management System</h1>
        <p>
          Streamlined appointments, digital records, doctor availability, reports,
          and an intelligent workflow — all in one place.
        </p>

        <div class="hero-buttons">
          <button class="btn primary" @click="goToLogin">Login</button>
          <button class="btn secondary" @click="goToRegister">Register</button>
        </div>
      </div>

      <div class="hero-image">
        <img src="https://cdn-icons-png.flaticon.com/512/2966/2966486.png" alt="Hospital" />
      </div>
    </section>

    <!-- FEATURES SECTION -->
    <section class="features">
      <h2>Everything You Need</h2>

      <div class="feature-grid">

        <div class="feature-card">
          <img src="https://cdn-icons-png.flaticon.com/512/2913/2913597.png" />
          <h3>Appointment Booking</h3>
          <p>Patients can easily browse doctors and schedule appointments instantly.</p>
        </div>

        <div class="feature-card">
          <img src="https://cdn-icons-png.flaticon.com/512/2966/2966480.png" />
          <h3>Doctor Portal</h3>
          <p>Doctors manage appointments, availability, and treatment records.</p>
        </div>

        <div class="feature-card">
          <img src="https://cdn-icons-png.flaticon.com/512/3004/3004613.png" />
          <h3>Medical Records</h3>
          <p>Digital treatments, prescriptions, history — always accessible.</p>
        </div>

        <div class="feature-card">
          <img src="https://cdn-icons-png.flaticon.com/512/992/992651.png" />
          <h3>Admin Dashboard</h3>
          <p>Admins manage doctors, oversee reports, and maintain the system.</p>
        </div>

      </div>
    </section>
  </div>
</template>

<style scoped>
.home {
  font-family: "Inter", sans-serif;
  color: #333;
}

/* HERO SECTION */
.hero {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 60px;
  background: #f9fafc;
  border-bottom: 1px solid #ddd;
}

.hero-content {
  max-width: 540px;
}

.hero-content h1 {
  font-size: 40px;
  font-weight: 700;
  margin-bottom: 12px;
  line-height: 1.2;
  color: #1d3557;
}

.hero-content p {
  font-size: 18px;
  line-height: 1.5;
  margin-bottom: 24px;
  color: #4a4a4a;
}

.hero-buttons {
  display: flex;
  gap: 14px;
}

.btn {
  padding: 12px 26px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 15px;
  font-weight: 600;
  transition: 0.2s ease;
}

.btn.primary {
  background: #1d3557;
  color: white;
}

.btn.primary:hover {
  background: #13304a;
}

.btn.secondary {
  background: white;
  border: 2px solid #1d3557;
  color: #1d3557;
}

.btn.secondary:hover {
  background: #1d3557;
  color: white;
}

.hero-image img {
  width: 360px;
  opacity: 0.92;
}

/* FEATURES SECTION */
.features {
  padding: 50px;
  text-align: center;
}

.features h2 {
  font-size: 32px;
  margin-bottom: 40px;
  color: #1d3557;
}

.feature-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 28px;
  justify-content: center;
}

.feature-card {
  width: 260px;
  padding: 24px;
  border-radius: 12px;
  background: #f1f3f6;
  box-shadow: 0 3px 8px rgba(0,0,0,0.08);
  transition: 0.2s ease;
  text-align: center;
}

.feature-card:hover {
  transform: translateY(-5px);
}

.feature-card img {
  width: 70px;
  margin-bottom: 12px;
}

.feature-card h3 {
  font-size: 18px;
  margin-bottom: 8px;
  color: #1d3557;
}

.feature-card p {
  font-size: 14px;
  color: #444;
}

/* FOOTER */
footer {
  margin-top: 40px;
  padding: 20px;
  background: #1d3557;
  color: white;
  text-align: center;
  font-size: 14px;
}
</style>
