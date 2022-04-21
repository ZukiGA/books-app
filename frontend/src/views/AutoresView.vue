<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";

const autores = ref([
  {
    nombre: "J.R.R",
    apellido: "Tolkien",
    fecha_nac: "07/04/1892",
  },
  {
    nombre: "Gabriel",
    apellido: "Montiel",
    fecha_nac: "23/09/1989",
  },
]);

onMounted(() => {
  axios
    .get("http://localhost:8000/api/autores")
    .then((res) => {
      console.log(res.data);
      autores.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
});
</script>

<template>
  <div class="container">
    <h1 class="mt-5">Autores</h1>
    <table class="table">
      <thead>
        <tr>
          <th>Nombre</th>
          <th>Apellido</th>
          <th>Fecha de nacimiento</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, i) in autores" :key="i">
          <td>{{ item.nombre }}</td>
          <td>{{ item.apellido }}</td>
          <td>{{ item.fecha_nacimiento }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
