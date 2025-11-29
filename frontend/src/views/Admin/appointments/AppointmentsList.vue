<script setup>
import { ref, computed, onMounted } from "vue";
import adminAPI from "@/api/admin";
import AdminSection from "../components/AdminSection.vue";
import AdminTable from "../components/AdminTable.vue";

const loading = ref(true);
const appointments = ref([]);
const search = ref("");
const statusFilter = ref("ALL");

const loadAppointments = async () => {
  loading.value = true;
  try {
    const res = await adminAPI.getAppointments();
    appointments.value = res.data.appointments;
  } catch (err) {
    console.error(err);
  }
  loading.value = false;
};

onMounted(loadAppointments);

const filtered = computed(() => {
  let data = [...appointments.value];

  if (statusFilter.value !== "ALL") {
    data = data.filter(a => a.status === statusFilter.value);
  }

  if (search.value.trim()) {
    const term = search.value.toLowerCase();
    data = data.filter(a =>
      a.doctor_name.toLowerCase().includes(term) ||
      a.patient_name.toLowerCase().includes(term) ||
      a.date.includes(term)
    );
  }

  return data;
});

const updateStatus = async (id, status) => {
  try {
    await adminAPI.updateAppointmentStatus(id, { status });
    await loadAppointments();
  } catch (err) {
    console.error(err);
  }
};
</script>

<template>
  <div class="page">
    <h2>Manage Appointments</h2>

    <AdminSection title="Appointments List">

      <!-- Filters -->
      <div class="filters">
        <input v-model="search" placeholder="Search by doctor or patient..." />

        <select v-model="statusFilter">
          <option value="ALL">All Status</option>
          <option value="PENDING">Pending</option>
          <option value="CONFIRMED">Confirmed</option>
          <option value="COMPLETED">Completed</option>
          <option value="CANCELLED">Cancelled</option>
        </select>
      </div>

      <!-- Table -->
      <AdminTable
        :columns="['ID', 'Doctor', 'Patient', 'Date', 'Time', 'Status']"
        :rows="filtered"
      />

      <!-- Actions -->
      <div class="actions" v-for="a in filtered" :key="a.id">

        <button
          class="btn confirm"
          v-if="a.status === 'PENDING'"
          @click="updateStatus(a.id, 'CONFIRMED')"
        >
          Confirm
        </button>

        <button
          class="btn complete"
          v-if="a.status === 'CONFIRMED'"
          @click="updateStatus(a.id, 'COMPLETED')"
        >
          Mark Completed
        </button>

        <button
          class="btn cancel"
          v-if="a.status !== 'CANCELLED'"
          @click="updateStatus(a.id, 'CANCELLED')"
        >
          Cancel
        </button>

      </div>

    </AdminSection>
  </div>
</template>

<style scoped>
.page {
  padding: 20px;
}

.filters {
  display: flex;
  gap: 14px;
  margin-bottom: 14px;
}

input, select {
  padding: 10px;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
}

.actions {
  margin-top: 10px;
  display: flex;
  gap: 10px;
}

.btn {
  padding: 6px 12px;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}

.confirm {
  background: #0284c7;
}

.complete {
  background: #16a34a;
}

.cancel {
  background: #dc2626;
}
</style>
