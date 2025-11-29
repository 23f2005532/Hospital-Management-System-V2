<script setup>
import { ref } from "vue";
import authAPI from "@/api/auth";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/store/auth";

const email = ref("");
const password = ref("");
const loading = ref(false);
const error = ref("");

const router = useRouter();
const auth = useAuthStore();

const validate = () => {
  error.value = "";

  if (!email.value.trim()) {
    error.value = "Email is required";
    return false;
  }

  if (!password.value.trim()) {
    error.value = "Password is required";
    return false;
  }

  return true;
};

const login = async () => {
  if (!validate()) return;

  loading.value = true;
  error.value = "";

  try {
    const res = await authAPI.login({
      email: email.value,
      password: password.value,
    });

    auth.setAuth(res.data.token, res.data.role);
    router.push("/dashboard");
  } catch (err) {
    error.value = "Invalid email or password";
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <div class="login-page">
    <div class="card">

      <!-- Left Section -->
      <div class="left">
        <h1>Welcome back</h1>
        <p class="subtitle">Login to access your dashboard and manage your health.</p>

        <ul class="highlights">
          <li>✔ Book appointments easily</li>
          <li>✔ Access your medical history</li>
          <li>✔ Manage your patient profile</li>
        </ul>
      </div>

      <!-- Right Section: Form -->
      <div class="right">
        <form @submit.prevent="login" class="form">

          <div class="field">
            <label>Email</label>
            <input v-model="email" type="email" placeholder="you@example.com" />
          </div>

          <div class="field">
            <label>Password</label>
            <input v-model="password" type="password" placeholder="••••••••" />
          </div>

          <p v-if="error" class="error">{{ error }}</p>

          <button class="submit-btn" type="submit" :disabled="loading">
            {{ loading ? "Logging in..." : "Login" }}
          </button>

          <p class="register-link">
            Don't have an account?
            <router-link to="/register">Register here</router-link>
          </p>
        </form>
      </div>

    </div>
  </div>
</template>

<style scoped>
.login-page {
  display: flex;
  justify-content: center;
  padding: 40px 16px;
}

.card {
  display: flex;
  gap: 32px;
  max-width: 900px;
  width: 100%;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
  padding: 32px 32px 36px;
}

/* Left Section */
.left {
  flex: 1;
  border-right: 1px solid #e5e7eb;
  padding-right: 24px;
}

.left h1 {
  font-size: 28px;
  margin-bottom: 10px;
  color: #1d3557;
}

.subtitle {
  font-size: 14px;
  color: #4b5563;
  margin-bottom: 20px;
}

.highlights {
  list-style: none;
  padding: 0;
  color: #374151;
  font-size: 14px;
}

.highlights li {
  margin-bottom: 6px;
}

/* Right Section (Form) */
.right {
  flex: 1.2;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.field {
  display: flex;
  flex-direction: column;
}

label {
  font-size: 13px;
  margin-bottom: 4px;
  color: #374151;
}

input {
  border: 1px solid #d1d5db;
  border-radius: 6px;
  padding: 10px;
  font-size: 14px;
  outline: none;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
}

input:focus {
  border-color: #1d3557;
  box-shadow: 0 0 0 1px rgba(29, 53, 87, 0.2);
}

.error {
  color: #b91c1c;
  font-size: 13px;
  margin-top: -8px;
}

.submit-btn {
  margin-top: 10px;
  padding: 10px 18px;
  background: #1d3557;
  color: white;
  border: none;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  font-size: 15px;
  transition: background 0.15s ease, transform 0.1s ease;
}

.submit-btn:hover:enabled {
  background: #16304a;
  transform: translateY(-1px);
}

.submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.register-link {
  margin-top: 4px;
  text-align: center;
}

.register-link a {
  font-weight: 600;
  color: #1d3557;
  text-decoration: none;
}

.register-link a:hover {
  text-decoration: underline;
}

/* Responsive */
@media (max-width: 850px) {
  .card {
    flex-direction: column;
    padding: 24px 18px;
  }

  .left {
    border-right: none;
    border-bottom: 1px solid #e5e7eb;
    padding-bottom: 16px;
    margin-bottom: 12px;
  }
}
</style>
