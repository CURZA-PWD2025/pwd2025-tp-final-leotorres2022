<template>
   <h1 class="titulo">Tienda </h1>
<router-link :to="{ name: 'configuraciones' }" class="config-link" ><i class="pi pi-cog" style="font-size: 2rem"></i></router-link>
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
}

.productos-grid {
  display: flex;
  gap: 40px;
  width: 100%;
  justify-content: center;
  align-items: center;
}
.titulo
{text-align: center;

}

.producto {
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
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.producto p {
  margin-top: 12px;
  font-weight: bold;
  font-size: 18px;
  text-align: center;
}
.tienda-page h2 {
  text-align: center;
  font-family: "Arial Rounded MT Bold", "Arial Rounded", Arial, sans-serif;
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
  font-family: "Arial Rounded MT Bold", "Arial Rounded", Arial, sans-serif;
  cursor: pointer;
  font-weight: bold;
  transition: background 0.2s;
}
button {
  background-color: #28a745;
  color: white;
  padding: 0.75rem 1.5rem;
  font-size: 1.1rem;
  font-weight: bold;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  transition: background-color 0.3s ease, transform 0.2s ease;
}

button:hover {
  background-color: #218838;
  transform: scale(1.05);
}

</style>
