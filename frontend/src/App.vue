<script setup>
import { RouterView } from "vue-router";
import BarraNav from "./components/BarraNav.vue";
</script>

<template>
  <header>
    <BarraNav />

    <RouterView />
  </header>
</template>

<style></style>
