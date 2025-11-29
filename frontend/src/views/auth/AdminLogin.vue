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
      role: "admin"
    });

    auth.setAuth(res.data.token, "admin");
    router.push("/admin/dashboard");

  } catch (err) {
    error.value = "Invalid admin credentials";
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <div class="page admin-page">
    <div class="card">
      <h2>Admin Login</h2>
      <p class="subtitle">System control panel</p>

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
.admin-page {
  background: linear-gradient(135deg, #1a1a1a, #2c2c2c);
  height: calc(100vh - 64px);
  display: flex;
  align-items: center;
  justify-content: center;
}

.card {
  width: 360px;
  padding: 28px;
  background: #2b2b2b;
  color: white;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.4);
  text-align: center;
}

h2 {
  margin: 0 0 10px;
}

.subtitle {
  margin-bottom: 20px;
  font-size: 14px;
  opacity: 0.7;
}

input {
  width: 100%;
  padding: 10px 12px;
  margin-top: 10px;
  border-radius: 6px;
  border: 1px solid #444;
  background: #1e1e1e;
  color: white;
}

button {
  margin-top: 16px;
  width: 100%;
  padding: 10px;
  background: #e63946;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

button:hover {
  background: #c5303a;
}

.error {
  margin-top: 12px;
  color: #ff8383;
}
</style>
