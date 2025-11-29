<script setup>
import { ref, watch, onMounted } from "vue";
import adminDoctorsAPI from "@/api/admin/doctors";

const props = defineProps({
  modelValue: Object,
  editMode: Boolean
});

const emit = defineEmits(["update:modelValue", "submit"]);

const specializations = ref([]);

const loadSpecs = async () => {
  const res = await adminDoctorsAPI.getSpecializations();
  specializations.value = res.data;
};

onMounted(loadSpecs);

const updateField = (field, value) => {
  emit("update:modelValue", { ...props.modelValue, [field]: value });
};
</script>

<template>
  <div class="form">

    <input
      :value="modelValue.full_name"
      @input="updateField('full_name', $event.target.value)"
      placeholder="Full Name"
    />

    <input
      :value="modelValue.email"
      @input="updateField('email', $event.target.value)"
      placeholder="Email"
      :disabled="editMode"
    />

    <input
      v-if="!editMode"
      :value="modelValue.password"
      @input="updateField('password', $event.target.value)"
      placeholder="Password"
      type="password"
    />

    <input
      :value="modelValue.phone"
      @input="updateField('phone', $event.target.value)"
      placeholder="Phone"
    />

    <input
      :value="modelValue.age"
      @input="updateField('age', $event.target.value)"
      type="number"
      placeholder="Age"
    />

    <select
      :value="modelValue.gender"
      @change="updateField('gender', $event.target.value)"
    >
      <option disabled value="">Gender</option>
      <option>Male</option>
      <option>Female</option>
      <option>Other</option>
    </select>

    <select
      :value="modelValue.specialization_id"
      @change="updateField('specialization_id', $event.target.value)"
    >
      <option disabled value="">Specialization</option>
      <option v-for="s in specializations" :key="s.id" :value="s.id">
        {{ s.name }}
      </option>
    </select>

    <input
      :value="modelValue.qualification"
      @input="updateField('qualification', $event.target.value)"
      placeholder="Qualification"
    />

    <input
      :value="modelValue.experience_years"
      @input="updateField('experience_years', $event.target.value)"
      type="number"
      placeholder="Years of Experience"
    />

    <input
      :value="modelValue.consultation_fee"
      @input="updateField('consultation_fee', $event.target.value)"
      type="number"
      placeholder="Consultation Fee"
    />

    <textarea
      :value="modelValue.bio"
      @input="updateField('bio', $event.target.value)"
      rows="3"
      placeholder="Short Bio"
    ></textarea>

    <button class="submit" @click="emit('submit')">
      {{ editMode ? "Save Changes" : "Create Doctor" }}
    </button>

  </div>
</template>

<style scoped>
.form {
  display: flex;
  flex-direction: column;
  gap: 14px;
}
input, select, textarea {
  padding: 12px;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
}
.submit {
  background: #1d3557;
  color: white;
  padding: 12px;
  border-radius: 6px;
  cursor: pointer;
}
</style>
