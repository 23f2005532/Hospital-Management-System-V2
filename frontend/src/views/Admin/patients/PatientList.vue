<script setup>
import { ref, onMounted } from "vue";
import patientAPI from "@/api/admin/patients";
import { useRouter } from "vue-router";

const patients = ref([]);
const loading = ref(true);
const router = useRouter();

const loadPatients = async () => {
  loading.value = true;
  const res = await patientAPI.getAllPatients();
  patients.value = res.data;
  loading.value = false;
};

const editPatient = (id) => {
  router.push(`/admin/patients/${id}/edit`);
};

const toggleStatus = async (id) => {
  await patientAPI.togglePatientStatus(id);
  loadPatients();
};

const deletePatient = async (id) => {
  if (confirm("Delete this patient? This cannot be undone.")) {
    await patientAPI.deletePatient(id);
    loadPatients();
  }
};

onMounted(loadPatients);
</script>

<template>
  <div class="page">
    <h1 class="title">Patients Management</h1>

    <div v-if="loading" class="loading">Loading...</div>

    <table v-else class="data-table">
      <thead>
        <tr>
          <th>Name</th>
          <th>Email</th>
          <th>Age</th>
          <th>Gender</th>
          <th>Phone</th>
          <th>Status</th>
          <th style="text-align:right">Actions</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="p in patients" :key="p.id">
          <td>{{ p.name }}</td>
          <td>{{ p.email }}</td>
          <td>{{ p.age }}</td>
          <td>{{ p.gender }}</td>
          <td>{{ p.phone }}</td>

          <td>
            <span :class="p.active ? 'active' : 'inactive'">
              {{ p.active ? "Active" : "Inactive" }}
            </span>
          </td>

          <td class="actions">
            <button @click="editPatient(p.id)">Edit</button>
            <button @click="toggleStatus(p.id)">
              {{ p.active ? "Disable" : "Enable" }}
            </button>
            <button class="delete" @click="deletePatient(p.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.page {
  padding: 24px;
}
.title {
  font-size: 26px;
  font-weight: 600;
  margin-bottom: 24px;
}
.data-table {
  width: 100%;
  border-collapse: collapse;
  background: white;
  border-radius: 6px;
  overflow: hidden;
}
.data-table th {
  background: #1d3557;
  color: white;
  padding: 12px;
  text-align: left;
}
.data-table td {
  padding: 12px;
  border-bottom: 1px solid #eee;
}
.actions button {
  margin-left: 8px;
  padding: 6px 12px;
  border: none;
  cursor: pointer;
  background: #457b9d;
  color: white;
  border-radius: 4px;
}
.actions button.delete {
  background: #e63946;
}
.active {
  color: green;
  font-weight: 600;
}
.inactive {
  color: red;
  font-weight: 600;
}
.loading {
  font-size: 18px;
}
</style>
