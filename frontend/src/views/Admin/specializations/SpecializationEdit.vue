<script setup>
import { ref, onMounted } from "vue";
import specAPI from "@/api/admin/specializations";
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();
const id = route.params.id;

const spec = ref({
  name: "",
  description: ""
});
const loading = ref(true);

const load = async () => {
  const res = await specAPI.getAll();
  spec.value = res.data.find((s) => s.id == id);
  loading.value = false;
};

const save = async () => {
  await specAPI.update(id, spec.value);
  alert("Updated successfully.");
  router.push("/admin/specializations");
};

onMounted(load);
</script>

<template>
  <div class="page">
    <h1 class="title">Edit Specialization</h1>

    <div v-if="loading">Loading...</div>

    <form v-else class="form">
      <div class="row">
        <label>Name</label>
        <input v-model="spec.name" />
      </div>

      <div class="row">
        <label>Description</label>
        <textarea v-model="spec.description"></textarea>
      </div>

      <button class="save-btn" @click.prevent="save">Save</button>
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
  max-width: 450px;
}

.row {
  margin-bottom: 14px;
}

.row label {
  font-weight: 600;
}

.row input,
.row textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.save-btn {
  margin-top: 14px;
  padding: 10px 18px;
  background: #1d3557;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
