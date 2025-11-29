<script setup>
import { ref, onMounted } from "vue";
import patientAPI from "@/api/patient";

const profile = ref({
  name: "",
  age: "",
  gender: "",
  phone: "",
  address: ""
});
const message = ref("");

onMounted(async () => {
  try {
    const res = await patientAPI.getProfile();
    profile.value = res.data;
  } catch (err) {
    console.error(err);
  }
});

const save = async () => {
  try {
    await patientAPI.updateProfile(profile.value);
    message.value = "Profile updated successfully.";
  } catch (err) {
    message.value = "Failed to update profile.";
  }
};
</script>

<template>
  <div class="page">
    <h2>My Profile</h2>

    <div class="card">
      <label>Name</label>
      <input v-model="profile.name" />

      <label>Age</label>
      <input v-model="profile.age" type="number" />

      <label>Gender</label>
      <select v-model="profile.gender">
        <option>Male</option>
        <option>Female</option>
      </select>

      <label>Phone</label>
      <input v-model="profile.phone" />

      <label>Address</label>
      <textarea v-model="profile.address"></textarea>

      <button @click="save">Save</button>

      <p class="msg">{{ message }}</p>
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
  padding: 18px;
  border: 1px solid #e2e8f0;

  display: flex;
  flex-direction: column;
  gap: 10px;
}

input,
select,
textarea {
  padding: 10px;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
}

button {
  background: #1d3557;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}

button:hover {
  background: #0f2238;
}

.msg {
  margin-top: 8px;
  font-weight: bold;
}
</style>
