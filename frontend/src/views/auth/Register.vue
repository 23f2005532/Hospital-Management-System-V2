<script setup>
import { ref, reactive } from "vue";
import authAPI from "@/api/auth";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/store/auth";

const router = useRouter();
const auth = useAuthStore();

const form = reactive({
  name: "",
  email: "",
  password: "",
  confirmPassword: "",
  age: "",
  gender: "",
  phone: "",
  address: "",
});

const errors = reactive({});
const loading = ref(false);
const apiError = ref("");

const validate = () => {
  apiError.value = "";
  Object.keys(errors).forEach((k) => (errors[k] = ""));

  let valid = true;

  if (!form.name.trim()) {
    errors.name = "Full name is required";
    valid = false;
  }

  if (!form.email.trim()) {
    errors.email = "Email is required";
    valid = false;
  } else if (!/^\S+@\S+\.\S+$/.test(form.email)) {
    errors.email = "Enter a valid email";
    valid = false;
  }

  if (!form.password) {
    errors.password = "Password is required";
    valid = false;
  } else if (form.password.length < 6) {
    errors.password = "Password must be at least 6 characters";
    valid = false;
  }

  if (!form.confirmPassword) {
    errors.confirmPassword = "Please confirm your password";
    valid = false;
  } else if (form.password !== form.confirmPassword) {
    errors.confirmPassword = "Passwords do not match";
    valid = false;
  }

  if (!form.age) {
    errors.age = "Age is required";
    valid = false;
  } else if (isNaN(Number(form.age)) || Number(form.age) <= 0) {
    errors.age = "Enter a valid age";
    valid = false;
  }

  if (!form.gender) {
    errors.gender = "Please select a gender";
    valid = false;
  }

  if (!form.phone.trim()) {
    errors.phone = "Phone number is required";
    valid = false;
  } else if (!/^[0-9+\-\s]{7,15}$/.test(form.phone)) {
    errors.phone = "Enter a valid phone number";
    valid = false;
  }

  if (!form.address.trim()) {
    errors.address = "Address is required";
    valid = false;
  }

  return valid;
};

const register = async () => {
  if (!validate()) return;

  loading.value = true;
  apiError.value = "";

  try {
    // send registration with all details
    await authAPI.register({
      name: form.name,
      email: form.email,
      password: form.password,
      age: form.age,
      gender: form.gender,
      phone: form.phone,
      address: form.address,
    });

    // auto login after registration (based on backend login)
    const res = await authAPI.login({
      email: form.email,
      password: form.password,
    });

    auth.setAuth(res.data.token, res.data.role);
    router.push("/dashboard");
  } catch (err) {
    apiError.value =
      err?.response?.data?.message || "Registration failed. Try a different email.";
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <div class="register-page">
    <div class="card">

      <!-- Left side: Intro -->
      <div class="left">
        <h1>Create your account</h1>
        <p class="subtitle">
          Register as a patient to book appointments, view your medical history,
          and manage your health in one place.
        </p>

        <ul class="highlights">
          <li>✔ Easy appointment booking</li>
          <li>✔ Secure medical records</li>
          <li>✔ Access anywhere, anytime</li>
        </ul>
      </div>

      <!-- Right side: Form -->
      <div class="right">
        <form @submit.prevent="register" class="form">
          <div class="row">
            <div class="field">
              <label>Full Name</label>
              <input v-model="form.name" type="text" placeholder="John Doe" />
              <p v-if="errors.name" class="error">{{ errors.name }}</p>
            </div>

            <div class="field">
              <label>Email</label>
              <input v-model="form.email" type="email" placeholder="you@example.com" />
              <p v-if="errors.email" class="error">{{ errors.email }}</p>
            </div>
          </div>

          <div class="row">
            <div class="field">
              <label>Password</label>
              <input v-model="form.password" type="password" placeholder="••••••••" />
              <p v-if="errors.password" class="error">{{ errors.password }}</p>
            </div>

            <div class="field">
              <label>Confirm Password</label>
              <input
                v-model="form.confirmPassword"
                type="password"
                placeholder="Re-enter password"
              />
              <p v-if="errors.confirmPassword" class="error">
                {{ errors.confirmPassword }}
              </p>
            </div>
          </div>

          <div class="row">
            <div class="field small">
              <label>Age</label>
              <input v-model="form.age" type="number" min="1" placeholder="25" />
              <p v-if="errors.age" class="error">{{ errors.age }}</p>
            </div>

            <div class="field small">
              <label>Gender</label>
              <select v-model="form.gender">
                <option disabled value="">Select</option>
                <option>Male</option>
                <option>Female</option>
                <option>Other</option>
              </select>
              <p v-if="errors.gender" class="error">{{ errors.gender }}</p>
            </div>

            <div class="field">
              <label>Phone</label>
              <input v-model="form.phone" type="text" placeholder="+91 98765 43210" />
              <p v-if="errors.phone" class="error">{{ errors.phone }}</p>
            </div>
          </div>

          <div class="field">
            <label>Address</label>
            <textarea
              v-model="form.address"
              rows="2"
              placeholder="Street, City, State"
            ></textarea>
            <p v-if="errors.address" class="error">{{ errors.address }}</p>
          </div>

          <p v-if="apiError" class="error global">{{ apiError }}</p>

          <button class="submit-btn" type="submit" :disabled="loading">
            {{ loading ? "Creating account..." : "Create account" }}
          </button>

          <p class="login-link">
            Already have an account?
            <router-link to="/login">Login here</router-link>
          </p>
        </form>
      </div>
    </div>
  </div>
</template>

<style scoped>
.register-page {
  display: flex;
  justify-content: center;
  padding: 40px 16px;
}

.card {
  display: flex;
  gap: 32px;
  max-width: 1000px;
  width: 100%;
  background: #ffffff;
  border-radius: 16px;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
  padding: 32px 32px 36px;
}

/* Left side */
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
  margin-bottom: 18px;
}

.highlights {
  list-style: none;
  padding: 0;
  margin: 0;
  color: #374151;
  font-size: 14px;
}

.highlights li {
  margin-bottom: 6px;
}

/* Right side (form) */
.right {
  flex: 1.4;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.row {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
}

.field {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.field.small {
  max-width: 140px;
}

label {
  font-size: 13px;
  color: #374151;
  margin-bottom: 4px;
}

input,
select,
textarea {
  border: 1px solid #d1d5db;
  border-radius: 6px;
  padding: 8px 10px;
  font-size: 14px;
  outline: none;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
}

input:focus,
select:focus,
textarea:focus {
  border-color: #1d3557;
  box-shadow: 0 0 0 1px rgba(29, 53, 87, 0.1);
}

textarea {
  resize: vertical;
}

.error {
  color: #b91c1c;
  font-size: 12px;
  margin-top: 2px;
}

.error.global {
  margin-top: 6px;
  text-align: center;
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

.login-link {
  margin-top: 8px;
  font-size: 14px;
  text-align: center;
}

.login-link a {
  color: #1d3557;
  text-decoration: none;
  font-weight: 600;
}

.login-link a:hover {
  text-decoration: underline;
}

/* Responsive */
@media (max-width: 900px) {
  .card {
    flex-direction: column;
    padding: 24px 18px;
  }

  .left {
    border-right: none;
    border-bottom: 1px solid #e5e7eb;
    padding-right: 0;
    padding-bottom: 16px;
    margin-bottom: 10px;
  }
}
</style>
