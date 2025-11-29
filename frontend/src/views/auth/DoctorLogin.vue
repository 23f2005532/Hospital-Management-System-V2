<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import authAPI from "@/api/auth";
import { useAuthStore } from "@/store/auth";

const email = ref("");
const password = ref("");
const error = ref("");
const loading = ref(false);

const auth = useAuthStore();
const router = useRouter();

const login = async () => {
  loading.value = true;
  error.value = "";

  try {
    const res = await authAPI.login({
      email: email.value,
      password: password.value,
      role: "doctor"
    });

    auth.setAuth(res.data.token, "doctor");
    router.push("/doctor/dashboard");

  } catch (err) {
    error.value = "Invalid doctor credentials";
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <div class="page doctor-page">
    <div class="card">
      <img class="icon" src="https://cdn-icons-png.flaticon.com/512/387/387561.png" />

      <h2>Doctor Login</h2>
      <p class="subtitle">Access appointments, patients & records</p>

      <input v-model="email" placeholder="Email" />
      <input v-model="password" type="password" placeholder="Password" />

      <button @click="login" :disabled="loading">
        {{ loading ? 'Logging in...' : 'Login' }}
      </button>

      <p class="error" v-if="error">{{ error }}</p>
    </div>
  </div>
</template>

<style scoped>
.doctor-page {
  background: linear-gradient(145deg, #f0f4f8, #e2e8f0);
  height: calc(100vh - 64px);

  display: flex;
  justify-content: center;
  align-items: center;
}

.card {
  background: white;
  width: 360px;
  padding: 28px;
  border-radius: 14px;
  border: 1px solid #d1d9e6;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
  text-align: center;
}

.icon {
  width: 60px;
  opacity: 0.9;
  margin-bottom: 10px;
}

h2 {
  margin: 0 0 10px;
  color: #1d3557;
}

.subtitle {
  margin-bottom: 20px;
  color: #4a5568;
  font-size: 14px;
}

input {
  width: 100%;
  padding: 10px 12px;
  margin-top: 10px;
  border-radius: 6px;
  border: 1px solid #ccd5df;
}

button {
  margin-top: 16px;
  width: 100%;
  padding: 10px;
  background: #2a4365;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

button:hover {
  background: #1a2f4a;
}

.error {
  margin-top: 12px;
  color: red;
}
</style>
