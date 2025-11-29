<script setup>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import SubHeader from "./components/SubHeader.vue";
</script>

<template>
  <Header />
  <SubHeader />

  <main class="main-content">
    <router-view />
  </main>

  <Footer />
</template>

<style scoped>
main{
  margin: 0;
  padding: 0;
}
.main-content {
  min-height: calc(100vh - 140px);
  padding-bottom: 20px;
}
</style>
