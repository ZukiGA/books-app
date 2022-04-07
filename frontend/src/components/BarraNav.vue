<script setup>
import { RouterLink } from "vue-router";
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Califica libros</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNavAltMarkup"
        aria-controls="navbarNavAltMarkup"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <RouterLink to="/" tag="a" class="nav-link">Inicio</RouterLink>
          <RouterLink to="/libros" tag="a" class="nav-link">Libros</RouterLink>
          <RouterLink to="/autores" tag="a" class="nav-link"
            >Autores</RouterLink
          >
        </div>
      </div>
    </div>
  </nav>
</template>
