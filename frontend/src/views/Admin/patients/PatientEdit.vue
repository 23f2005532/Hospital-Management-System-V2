<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import patientAPI from "@/api/admin/patients";

const route = useRoute();
const router = useRouter();
const id = route.params.id;

const patient = ref(null);
const loading = ref(true);

const loadPatient = async () => {
  const res = await patientAPI.getPatient(id);
  patient.value = res.data;
  loading.value = false;
};

const save = async () => {
  await patientAPI.updatePatient(id, patient.value);
  alert("Patient updated.");
  router.push("/admin/patients");
};

onMounted(loadPatient);
</script>

<template>
  <div class="page">
    <h1 class="title">Edit Patient</h1>

    <div v-if="loading">Loading...</div>

    <form v-else class="form">
      <div class="row">
        <label>Name</label>
        <input v-model="patient.name" />
      </div>

      <div class="row">
        <label>Email</label>
        <input v-model="patient.email" />
      </div>

      <div class="row">
        <label>Age</label>
        <input type="number" v-model="patient.age" />
      </div>

      <div class="row">
        <label>Gender</label>
        <select v-model="patient.gender">
          <option>Male</option>
          <option>Female</option>
          <option>Other</option>
        </select>
      </div>

      <div class="row">
        <label>Phone</label>
        <input v-model="patient.phone" />
      </div>

      <div class="row">
        <label>Address</label>
        <textarea v-model="patient.address"></textarea>
      </div>

      <button class="save-btn" @click.prevent="save">Save Changes</button>
    </form>
  </div>
</template>

<style scoped>
.page {
  padding: 24px;
}
.title {
  font-size: 26px;
  margin-bottom: 20px;
}
.form {
  max-width: 500px;
}
.row {
  margin-bottom: 14px;
}
.row label {
  font-weight: 600;
  display: block;
  margin-bottom: 4px;
}
.row input,
.row select,
.row textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.save-btn {
  margin-top: 16px;
  padding: 10px 18px;
  background: #1d3557;
  border: none;
  color: white;
  border-radius: 4px;
  cursor: pointer;
}
</style>
