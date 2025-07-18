<template>
  <div>
    <h1 class="titulo">Galería</h1>
    <div class="galeria-grid">
      <div class="galeria-item">
        <img src="@/assets/galeria/11.jpg" alt="Imagen 1" />
      </div>
      <div class="galeria-item">
        <img src="@/assets/galeria/12.jpg" alt="Imagen 2" />
      </div>
      <div class="galeria-item">
        <img src="@/assets/galeria/13.jpg" alt="Imagen 3" />
      </div>
      <div class="galeria-item">
        <img src="@/assets/galeria/14.jpg" alt="Imagen 4" />
      </div>
      <div class="galeria-item">
        <img src="@/assets/galeria/2010.jpg" alt="Imagen 5" />
      </div>
      <div class="galeria-item">
        <img src="@/assets/galeria/cuartos.jpg" alt="Imagen 6" />
      </div>
      <div class="galeria-item">
        <img src="@/assets/galeria/portada.jpg" alt="Imagen 7" />
      </div>
      <div class="galeria-item">
        <img src="@/assets/galeria/vestuario.jpg" alt="Imagen 8" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
h1 {
  grid-column: 1 / -1; /* Ocupa toda la fila */
  text-align: center;
  margin-bottom: 20px;
  font-size: 2rem;
  color: #1d07bf;
}
.galeria-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  padding: 0 40px;
}

.galeria-item {
  width: 100%;
  height: 250px; /* Altura fija para todas */
  overflow: hidden;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.galeria-item img {
  width: 100%;
  height: 100%;
  object-fit: cover; /* Recorta para mantener proporción sin distorsionar */
  display: block;
  transition: transform 0.3s ease;
}

.galeria-item:hover img {
  transform: scale(1.05);
}
</style>
