<script setup>
import { ref, onMounted } from "vue";
import specAPI from "@/api/admin/specializations";
import { useRouter } from "vue-router";

const router = useRouter();
const specializations = ref([]);
const loading = ref(true);

const loadSpecs = async () => {
  loading.value = true;
  const res = await specAPI.getAll();
  specializations.value = res.data;
  loading.value = false;
};

const addNew = () => {
  router.push("/admin/specializations/create");
};

const editSpec = (id) => {
  router.push(`/admin/specializations/${id}/edit`);
};

const deleteSpec = async (id) => {
  if (confirm("Are you sure you want to delete this specialization?")) {
    await specAPI.delete(id);
    loadSpecs();
  }
};

onMounted(loadSpecs);
</script>

<template>
  <div class="page">
    <h1 class="title">Specializations</h1>

    <button class="add-btn" @click="addNew">+ Add Specialization</button>

    <div v-if="loading" class="loading">Loading...</div>

    <table v-else class="data-table">
      <thead>
        <tr>
          <th>Name</th>
          <th>Description</th>
          <th style="text-align:right;">Actions</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="s in specializations" :key="s.id">
          <td>{{ s.name }}</td>
          <td>{{ s.description }}</td>

          <td class="actions">
            <button @click="editSpec(s.id)">Edit</button>
            <button class="delete" @click="deleteSpec(s.id)">Delete</button>
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
  margin-bottom: 20px;
  font-weight: 600;
}

.add-btn {
  background: #1d3557;
  border: none;
  color: white;
  padding: 10px 18px;
  border-radius: 4px;
  margin-bottom: 20px;
  cursor: pointer;
}

.data-table {
  width: 100%;
  background: white;
  border-collapse: collapse;
}

.data-table th {
  background: #1d3557;
  color: white;
  padding: 12px;
}

.data-table td {
  padding: 12px;
  border-bottom: 1px solid #eee;
}

.actions button {
  margin-left: 8px;
  background: #457b9d;
  border: none;
  color: white;
  padding: 6px 12px;
  border-radius: 4px;
  cursor: pointer;
}

.actions button.delete {
  background: #e63946;
}
</style>
