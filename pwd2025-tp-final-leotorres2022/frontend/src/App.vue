<template>
  <div class="app-container">
    <header><nav class="navbar">
      <ul >
        <li><router-link to="/">HOME</router-link></li>
        <li><router-link :to="{name:'club'}">CLUB</router-link></li>
        <li><router-link :to="{name:'tienda'}">TIENDA</router-link></li>
        <li><router-link :to="{name:'galeria'}">GALERIA</router-link></li>
        <li><router-link :to="{name:'socios_list'}">SOCIOS</router-link></li>
        <li><router-link :to="{name:'compras_list'}">COMPRAS</router-link></li>
        <li style="display: flex; align-items: center; justify-content: center;">
  <i class="pi pi-user" style="font-size: 1.8rem; color: white; margin-right: 8px;"></i>
  <select v-model="modoUsuario" style="font-size: 1rem; padding: 6px; border-radius: 6px;">
  <option value="usuario">Usuario</option>
  <option value="admin">Admin</option>
</select>
</li>

      </ul>
    </nav>

    <div v-if="$route.path === '/'">
    <h1>¿Todavia no sos socio?</h1>
    <button><router-link :to="{name:'socios_create'}">ASOCIATE </router-link></button>
      </div>
    </header>


    <main class="main-content">
      <!-- Solo muestra las imágenes en Home -->
      <div class="imagenes-container" v-if="$route.path === '/'">
        <img src="@/assets/logo-liga.jpg" alt="Logo Liga" class="img-liga" />
        <img src="@/assets/presi.jpg" alt="Presidente" class="img-presi" />
      </div>
      <RouterView />
    </main>
<footer class="footer">
  <div class="footer-grid">

  <div class="footer-section">
  <h4>Sobre Nosotros</h4>
  <p>El Centro de Entrenamiento Formando Futuro es una institución deportiva dedicada a fomentar el fútbol y los valores del deporte en jóvenes y adultos desde 2018. Con una fuerte presencia en la región, impulsamos el desarrollo atlético, la inclusión y el trabajo en equipo dentro y fuera del campo.</p>
</div>


   <div class="footer-section">
  <h4>Contacto</h4>
  <p><i class="pi pi-envelope" style="margin-right: 8px;"></i> contacto@formandofuturo.edu.ar</p>
  <p><i class="pi pi-whatsapp" style="margin-right: 8px;"></i> 2920 123456</p>
  <p><i class="pi pi-map-marker" style="margin-right: 8px;"></i> Blvd. Ituzaingó 270, Viedma, Río Negro</p>
   </div>


    <div class="footer-section">
      <h4>Accesos Rápidos</h4>
      <ul>
          <li><router-link to="/">HOME</router-link></li>
        <li><router-link :to="{name:'club'}">CLUB</router-link></li>
        <li><router-link :to="{name:'tienda'}">TIENDA</router-link></li>
        <li><router-link :to="{name:'galeria'}">GALERIA</router-link></li>
        <li><router-link :to="{name:'socios_list'}">SOCIOS</router-link></li>
        <li><router-link :to="{name:'compras_list'}">COMPRAS</router-link></li>
      </ul>
    </div>

    <div class="footer-section">
      <h4>Seguinos</h4>
      <ul class="social-links">
        <li><a href="https://facebook.com/formando.futuro.ceff" target="_blank"><i class="pi pi-facebook"></i> Formando Futuro</a></li>
        <li><a href="https://instagram.com/formando.futuro.oficial" target="_blank"><i class="pi pi-instagram"></i> Formando Futuro Oficial</a></li>

      </ul>
    </div>

  </div>

  <div class="footer-bottom">
    <p>© 2025 Formando Futuro CEFF — Todos los derechos reservados.</p>
  </div>
</footer>


  </div>
  </template>

<script setup lang="ts">
import 'primeicons/primeicons.css'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import useUserStore from '@/stores/user'
import { computed } from 'vue'
const router = useRouter()
const userStore = useUserStore()

const modoUsuario = computed({
  get: () => userStore.modo,
  set: (val: string) => userStore.setModo(val)
})


</script>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  width: 100vw; /* Asegura el ancho completo */
  min-height: 100vh;
}
.navbar {
  background: #169d3e;
  padding: 0 40px;
  width: 100%;
  box-sizing: border-box;
}

.navbar ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
  align-items: center;
  justify-content: space-between;
}

.navbar li {
  text-align: center;
  flex: 1;
}

.navbar a {
  display: block;
  font-size: 1.8rem;
  padding: 18px 24px;
  text-decoration: none;
  color: white;
  font-weight: bold;
  transition: background-color 0.3s ease, letter-spacing 0.3s ease;
}

.navbar a:hover {
  background-color: #1aae4d; /* Verde más claro en hover */
  letter-spacing: 0.5px;     /* Separación suave de letras */
  text-decoration: underline;
}

/* Estilos para el main */
.main-content {
  flex: 1;
  padding: 40px;

}

.imagenes-container {
  display: flex;
  width: 100%;
  max-width: 1200px;
  height: 640px; /* Más alto */
  gap: 20px;
  margin: 0 auto;
}

.img-presi {
  height: 100%;
  width: 100%;
  border-radius: 12px;
  object-fit: cover;
  background: #fff;
  flex: 2;
}

.img-liga {
  height: 100%;
  width: 100%;
  border-radius: 12px;
  object-fit: contain; /* No deforma el logo */
  background: #fff;
  flex: 1;
}
h1 {
  text-align: center;
  font-family: "Arial Rounded MT Bold", "Arial Rounded", Arial, sans-serif;
}
button {
  display: block;
  margin: 20px auto;
  padding: 12px 32px;
  font-size: 20px;
  color: #fff;
  border: none;
  border-radius: 8px;
  font-family: "Arial Rounded MT Bold", "Arial Rounded", Arial, sans-serif;
  cursor: pointer;
  font-weight: bold;
  transition: background 0.2s;
}

button:hover {
  background: #447453;
}

/* Estilos para el footer */
.footer {
    background-color: #007BFF;
  color: #fff;
    padding: 60px 20px;
  font-family: 'Segoe UI', sans-serif;
}

.footer-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 80px;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  box-sizing: border-box;
}

.footer-section h4 {
  color: #fff;
  margin-bottom: 15px;
  font-size: 20px;
}

.footer-section p,
.footer-section ul,
.footer-section a {
  font-size: 0.8rem;
  line-height: 1.6;
  color: #fff;
  text-decoration: none;
}

.footer-section ul {
  list-style: none;
  padding: 0;
}

.footer-section ul li {
  margin-bottom: 10px;
}

.social-links li {
  display: flex;
  align-items: center;
  gap: 8px;
}

.social-links li i {
  font-size: 1.5rem;
}

.footer-bottom {
  text-align: center;
  margin-top: 50px;
  font-size: 14px;
  color: #fff;
}

/* Responsive estilos */

.navbar ul,
.footer ul {
  height: 44px; /* Más bajo */
}

.navbar a,
.footer a {
  font-size: 15px; /* Más chico */
  padding: 8px 0;
}

.navbar,
.footer {
  padding: 0 20px;
}

@media (max-width: 700px) {
  .navbar ul,
  .footer ul {
    flex-direction: column;
    height: auto;
  }
  .navbar li,
  .footer li {
    margin-bottom: 6px;
  }
  .navbar a,
  .footer a {
    font-size: 14px;
    padding: 8px 0;
  }
}
select {
  background: transparent;
  color: rgb(40, 5, 166);
  border: 1px solid white;
}
</style>
