<script setup>
import { ref, onMounted } from "vue";
import patientAPI from "@/api/patient";

const doctors = ref([]);
const loadingDoctors = ref(true);

const selectedDoctor = ref(null);
const selectedDate = ref("");
const timeSlots = ref([]);
const loadingSlots = ref(false);

const bookingMessage = ref("");

// Load doctors list
onMounted(async () => {
  try {
    const res = await patientAPI.getDoctors();
    doctors.value = res.data;
  } catch (err) {
    console.error(err);
  }
  loadingDoctors.value = false;
});

// Load availability for selected doctor/date
const loadSlots = async () => {
  if (!selectedDoctor.value || !selectedDate.value) return;

  loadingSlots.value = true;
  try {
    const res = await patientAPI.getDoctorAvailability(
      selectedDoctor.value,
      selectedDate.value
    );
    timeSlots.value = res.data.slots;
  } catch (err) {
    console.error(err);
  }
  loadingSlots.value = false;
};

// Book appointment
const book = async (slot) => {
  try {
    await patientAPI.bookAppointment({
      doctor_id: selectedDoctor.value,
      date: selectedDate.value,
      time: slot
    });

    bookingMessage.value = "Appointment booked successfully!";
  } catch (err) {
    bookingMessage.value = "Failed to book appointment.";
  }
};
</script>

<template>
  <div class="page">

    <h2>Book Appointment</h2>

    <!-- Doctor selection -->
    <section class="card">
      <h3>Select Doctor</h3>

      <div v-if="loadingDoctors">Loading doctors...</div>

      <select v-else v-model="selectedDoctor" @change="loadSlots">
        <option disabled value="">Choose a doctor</option>
        <option
          v-for="d in doctors"
          :key="d.id"
          :value="d.id"
        >
          {{ d.full_name }} — {{ d.specialization }}
        </option>
      </select>
    </section>

    <!-- Date selection -->
    <section class="card">
      <h3>Select Date</h3>

      <input type="date" v-model="selectedDate" @change="loadSlots" />
    </section>

    <!-- Time slots -->
    <section class="card">
      <h3>Available Slots</h3>

      <div v-if="loadingSlots">Loading slots...</div>

      <div v-else-if="timeSlots.length === 0">
        No slots available for selected date.
      </div>

      <div class="slots" v-else>
        <button
          v-for="slot in timeSlots"
          :key="slot"
          @click="book(slot)"
        >
          {{ slot }}
        </button>
      </div>
    </section>

    <!-- Booking message -->
    <p v-if="bookingMessage" class="msg">{{ bookingMessage }}</p>
  </div>
</template>

<style scoped>
.page {
  padding: 20px;
  max-width: 900px;
  margin: auto;
}

h2 {
  margin-bottom: 16px;
}

.card {
  background: white;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  padding: 16px;
  margin-bottom: 18px;
}

select,
input[type="date"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  font-size: 15px;
}

.slots {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

button {
  padding: 8px 14px;
  background: #1d3557;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}

button:hover {
  background: #0f2238;
}

.msg {
  margin-top: 10px;
  font-weight: bold;
  color: #1d4ed8;
}
</style>
