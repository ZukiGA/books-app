<script setup>
import axios, { Axios } from "axios";
import { onMounted, ref } from "vue";

const props = defineProps(["id"]);
const libro = ref();

onMounted(
  axios
    .get("http://localhost:8000/api/libros/" + props.id)
    .then((response) => {
      libro.value = response.data;
    })
    .catch((error) => {
      console.log(error);
    })
);
</script>

<template>
  <div class="container">
    <h1 class="mt-5">{{ libro.titulo }}</h1>
    <img :src="libro.portada" class="img-fluid" alt="..." />
    <p class="col-sm-8">
      Autor: {{ libro.autores[0].nombre }} {{ libro.autores[0].apellido }}
      <br />
      Páginas: {{ libro.num_pag }} <br />
      Género: {{ libro.genero.nombre }} <br />
      Sinopsis: {{ libro.sinopsis }} <br />
    </p>
  </div>
</template>
