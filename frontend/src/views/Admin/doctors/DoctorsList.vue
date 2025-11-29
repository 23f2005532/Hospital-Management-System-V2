<script setup>
import { ref, computed, onMounted } from "vue";
import adminDoctorsAPI from "@/api/admin/doctors";
import { useRouter } from "vue-router";

const router = useRouter();

const loading = ref(true);
const doctors = ref([]);
const search = ref("");

const load = async () => {
  loading.value = true;
  try {
    const res = await adminDoctorsAPI.getAll();
    doctors.value = res.data || [];
  } catch (err) {
    console.error(err);
  }
  loading.value = false;
};

onMounted(load);

const filtered = computed(() => {
  const q = search.value.trim().toLowerCase();
  if (!q) return doctors.value;

  return doctors.value.filter(d => {
    return (
      (d.full_name || "").toLowerCase().includes(q) ||
      (d.email || "").toLowerCase().includes(q) ||
      (d.specialization || "").toLowerCase().includes(q)
    );
  });
});
</script>

<template>
  <div class="page">
    <div class="header">
      <h2>Doctors Management</h2>
      <button class="btn-primary" @click="router.push('/admin/doctors/add')">
        + Add Doctor
      </button>
    </div>

    <input
      v-model="search"
      class="search"
      placeholder="Search doctors..."
    />

    <div v-if="loading" class="loading">Loading...</div>

    <div v-else-if="filtered.length === 0" class="empty">No doctors found.</div>

    <table v-else class="table">
      <thead>
        <tr>
          <th>Name</th>
          <th>Email</th>
          <th>Specialization</th>
          <th>Experience</th>
          <th>Status</th>
          <th>Verified</th>
          <th style="width:130px">Actions</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="d in filtered" :key="d.id">
          <td>{{ d.full_name }}</td>
          <td>{{ d.email }}</td>
          <td>{{ d.specialization }}</td>
          <td>{{ d.experience_years }} yrs</td>

          <td>
            <span :class="d.is_active ? 'tag active' : 'tag inactive'">
              {{ d.is_active ? "Active" : "Inactive" }}
            </span>
          </td>

          <td>
            <span :class="d.is_verified ? 'tag yes' : 'tag no'">
              {{ d.is_verified ? "Verified" : "Pending" }}
            </span>
          </td>

          <td>
            <button class="btn-edit" @click="router.push(`/admin/doctors/edit/${d.id}`)">
              Edit
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.page { padding: 26px; }
.header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 18px;
}
.btn-primary {
  padding: 10px 18px;
  background: #1d3557;
  color: white;
  border-radius: 6px;
}
.search {
  width: 320px;
  padding: 10px;
  border: 1px solid #d0d7e1;
  border-radius: 6px;
  margin-bottom: 18px;
}
.loading, .empty {
  padding: 20px;
  text-align: center;
  color: #6b7280;
}
.table {
  width: 100%;
  border-collapse: collapse;
}
.table th {
  text-align: left;
  background: #f1f5f9;
  padding: 14px;
}
.table td {
  padding: 14px;
  border-bottom: 1px solid #e5e7eb;
}
.table tr:hover {
  background: #f8fafc;
}
.btn-edit {
  background: #457b9d;
  color: white;
  padding: 6px 12px;
  border-radius: 6px;
}
.tag {
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 13px;
}
.tag.active { background: #d1fae5; color: #065f46; }
.tag.inactive { background: #e2e8f0; color: #475569; }
.tag.yes { background: #dcfce7; color: #15803d; }
.tag.no { background: #fee2e2; color: #b91c1c; }
</style>
