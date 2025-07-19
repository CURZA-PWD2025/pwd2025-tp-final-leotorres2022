<template>
   <!-- Ícono de configuración -->
  <router-link
     v-if="userStore.modo === 'admin'"   :to="{ name: 'configuraciones' }" class="config-link">
    <i class="pi pi-cog" style="font-size: 2rem"></i>
  </router-link>

  <!-- Lista de productos -->
  <div class="productos-grid">

      <div
        v-for="(producto, index) in productos"
        :key="index"
        class="producto"
      >
        <img :src="producto.imagen" :alt="producto.descripcion" />
        <p>{{ producto.descripcion }}</p>
        <p>${{ producto.precio.toLocaleString() }}</p>

        <i
          class="pi pi-cart-plus"
          style="font-size: 2rem; cursor: pointer"
          @click.stop="seleccionarProducto(producto)"
          aria-label="Agregar al carrito"
        ></i>

    </div>
  </div>
</template>

<script setup lang="ts">
import 'primeicons/primeicons.css'
import { useRouter } from 'vue-router'
import useComprasStore from '@/stores/compras'
import type { Producto } from '@/interfaces/Producto'
import useUserStore from '@/stores/user'
const userStore = useUserStore()
const router = useRouter()
const comprasStore = useComprasStore()



// Productos estáticos
const productos = [
  {
    imagen: new URL('@/assets/camiseta.jpg', import.meta.url).href,
    descripcion: 'Camiseta titular',
    precio: 15000,
    },
  {
    imagen: new URL('@/assets/medias.jpg', import.meta.url).href,
    descripcion: 'Medias de fútbol',
    precio: 6000,

  },
  {
    imagen: new URL('@/assets/conjunto-entrenamiento.jpg', import.meta.url).href,
    descripcion: 'Conjunto de entrenamiento',
    precio: 30000,

  },
    {
    imagen: new URL('@/assets/conjunto-largo.jpeg', import.meta.url).href,
    descripcion: 'Conjunto largo',
    precio: 60000,

  },
  {
    imagen: new URL('@/assets/short.jpg', import.meta.url).href,
    descripcion: 'Short de fútbol',
    precio: 8000,

  }

]


function seleccionarProducto(producto: Producto) {
  comprasStore.seleccionarProducto(producto)
  router.push({ name: 'compras_create' })
}
</script>

<style scoped>


.titulo
{text-align: center;

}


.productos-grid {
  display: flex;
  flex-direction: row;
  gap: 40px;
  overflow-x: auto;
  padding: 1rem;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
}

.producto {
  flex: 0 0 300px;
  scroll-snap-align: start;
}



.producto:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 24px rgba(0,0,0,0.2);
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
.producto i {
  display: block;
  text-align: center;
  margin-top: 12px;
  color: #007BFF;
  transition: color 0.3s ease;
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
