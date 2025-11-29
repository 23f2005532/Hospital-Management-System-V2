<script setup>
import { ref } from "vue";
import adminDoctorsAPI from "@/api/admin/doctors";
import { useRouter } from "vue-router";
import DoctorForm from "./DoctorForm.vue";

const router = useRouter();

const form = ref({
  full_name: "",
  email: "",
  phone: "",
  gender: "",
  age: "",
  specialization_id: "",
  qualification: "",
  experience_years: "",
  consultation_fee: "",
  password: "",
  bio: ""
});

const submit = async () => {
  await adminDoctorsAPI.create(form.value);
  router.push("/admin/doctors");
};
</script>

<template>
  <div class="page">
    <h2>Add Doctor</h2>
    <DoctorForm v-model="form" :editMode="false" @submit="submit" />
  </div>
</template>

<style scoped>
.page { padding: 25px; max-width: 600px; }
</style>
