<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import adminDoctorsAPI from "@/api/admin/doctors";
import DoctorForm from "./DoctorForm.vue";

const route = useRoute();
const router = useRouter();
const id = route.params.id;

const form = ref(null);

onMounted(async () => {
  const res = await adminDoctorsAPI.getOne(id);
  form.value = res.data;
});

const submit = async () => {
  await adminDoctorsAPI.update(id, form.value);
  router.push("/admin/doctors");
};
</script>

<template>
  <div class="page">
    <h2>Edit Doctor</h2>

    <div v-if="!form" class="loading">Loading...</div>

    <DoctorForm
      v-else
      v-model="form"
      :editMode="true"
      @submit="submit"
    />
  </div>
</template>

<style scoped>
.page { padding: 25px; max-width: 600px; }
.loading { padding: 20px; text-align: center; }
</style>
