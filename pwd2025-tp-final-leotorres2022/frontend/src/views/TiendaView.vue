<template>
  <h1 class="titulo">Tienda</h1>
  <router-link :to="{ name: 'configuraciones' }" class="config-link"
    ><i class="pi pi-cog" style="font-size: 2rem"></i
  ></router-link>
  <div class="productos-grid">
    <div class="tienda-page">
      <div class="producto">
        <img src="@/assets/camiseta.jpg" alt="Camiseta de futbol" />
        <p>Camiseta de fútbol</p>
        <button>comprar</button>
      </div>
      <div class="producto">
        <img src="@/assets/medias.jpg" alt="medias de fútbol" />
        <p>Medias de fútbol</p>
        <button>comprar</button>
      </div>
      <div class="producto">
        <img src="@/assets/short.jpg" alt="Short de fútbol" />
        <p>Short de fútbol</p>
        <button>comprar</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import 'primeicons/primeicons.css'
</script>

<style scoped>
.tienda-page {
  padding: 40px;
  display: grid;
  gap: 40px;
  grid-template-columns: repeat(3, 1fr);
}

.productos-grid {
  width: 100%;
  justify-content: center;
  align-items: center;
}
.titulo {
  text-align: center;
}

.producto {
  background-color: #218838;
  padding: 0 0 1rem 0;
  border-radius: 15px;
  flex: 1 1 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.producto img {
  width: 100%;
  max-width: 400px;
  height: 350px;
  object-fit: cover;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.producto p {

  font-size: 18px;
  text-align: center;
  color: wheat;
  margin: 1rem 0.5rem;
}
.tienda-page h2 {
  text-align: center;
  font-family: 'Arial Rounded MT Bold', 'Arial Rounded', Arial, sans-serif;
}
.config-link {
  display: block;
  margin: auto;
  text-align: center;

  font-size: 20px;
  height: 2em;
  width: 4em;
  background: #169d3e;
  color: #fff;
  border: none;
  border-radius: 8px;
  font-family: 'Arial Rounded MT Bold', 'Arial Rounded', Arial, sans-serif;
  cursor: pointer;
  font-weight: bold;
  transition: background 0.2s;
}
button {
  background-color: #28a745;
  color: white;
  padding: 0.5rem 1rem;
  font-size: 0.75rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition:
    background-color 0.3s ease,
    transform 0.2s ease;
}

button:hover {
  background-color: #94efa7;
  transform: scale(1.05);
  color: #218838;
}
</style>
