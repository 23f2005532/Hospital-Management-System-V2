<script setup>
import { ref } from "vue";
import specAPI from "@/api/admin/specializations";
import { useRouter } from "vue-router";

const name = ref("");
const description = ref("");

const router = useRouter();

const save = async () => {
  await specAPI.create({
    name: name.value,
    description: description.value
  });

  alert("Specialization created.");
  router.push("/admin/specializations");
};
</script>

<template>
  <div class="page">
    <h1 class="title">Add New Specialization</h1>

    <form class="form">
      <div class="row">
        <label>Name</label>
        <input v-model="name" />
      </div>

      <div class="row">
        <label>Description</label>
        <textarea v-model="description"></textarea>
      </div>

      <button class="save-btn" @click.prevent="save">Create</button>
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
  font-weight: bold;
  display: block;
  margin-bottom: 4px;
}

.row input,
.row textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.save-btn {
  background: #1d3557;
  color: white;
  padding: 10px 18px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
