<script setup>
import { ref } from "vue";
const libros = ref([
  {
    titulo: "El señor de los anillos 1",
    autor: "J.R.R. Tolkien",
    num_pag: "600",
    portada: "/src/assets/portada1.jpeg",
  },
  {
    titulo: "El señor de los anillos 2",
    autor: "J.R.R. Tolkien",
    num_pag: "540",
    portada: "/src/assets/portada2.jpeg",
  },
  {
    titulo: "El señor de los anillos 3",
    autor: "J.R.R. Tolkien",
    num_pag: "720",
    portada: "/src/assets/portada3.jpeg",
  },
]);
</script>

<template>
  <main>
    <h1>Libros</h1>
    <div class="row">
      <div v-for="(item, i) in libros" :key="i" class="col-sm-2">
        <div class="card">
          <img :src="item.portada" class="card-img-top" alt="..." />
          <div class="card-body">
            <h5 class="card-title">{{ item.titulo }}</h5>
            <p class="card-text">Autor: {{ item.autor }}</p>
            <a href="#" class="btn btn-primary">Calificar</a>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
