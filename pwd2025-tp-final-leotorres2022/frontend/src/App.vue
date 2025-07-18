<template>
  <div class="app-container">
    <nav class="navbar">
      <ul>
        <li><router-link to="/">HOME</router-link></li>
        <li><router-link :to="{ name: 'club' }">CLUB</router-link></li>
        <li><router-link :to="{ name: 'tienda' }">TIENDA</router-link></li>
        <li><router-link :to="{ name: 'galeria' }">GALERIA</router-link></li>
        <li><router-link :to="{ name: 'socios_list' }">SOCIOS</router-link></li>
      </ul>
    </nav>

    <div v-if="$route.path === '/'">
      <h1>¿Todavia no sos socio?</h1>
      <button><router-link :to="{ name: 'socios_create' }">ASOCIATE </router-link></button>
    </div>

    <main class="main-content">
      <!-- Solo muestra las imágenes en Home -->
      <div class="imagenes-container" v-if="$route.path === '/'">
        <img src="@/assets/logo-liga.jpg" alt="Logo Liga" class="img-liga" />
        <img src="@/assets/presi.jpg" alt="Presidente" class="img-presi" />
      </div>
      <RouterView />
    </main>
    <footer class="footer">
      <section class="info-empresa">
        <h1>Direccion</h1>
        <p>direccion ficticia</p>
        <p>02920 15547412</p>

      </section>
      <section class="nav_footer">
  <ul >
        <li><router-link to="/">HOME</router-link></li>
        <li><router-link :to="{ name: 'club' }">CLUB</router-link></li>
        <li><router-link :to="{ name: 'tienda' }">TIENDA</router-link></li>
        <li><router-link :to="{ name: 'galeria' }">GALERIA</router-link></li>
        <li><router-link :to="{ name: 'socios_list' }">SOCIOS</router-link></li>
      </ul>
</section>
      <section class="redes-sociales">
        <ul class="redes-sociales">
        <li>
          <i class="pi pi-facebook" style="font-size: 1.2rem"></i
            >
          <a href="https://www.facebook.com/formando.futuro.ceff" target="_blank"
            >formando futuro</a>
        </li>
        <li>
          <i class="pi pi-instagram" style="font-size: 1.2rem"></i
            >
          <a
            href="https://www.instagram.com/formando.futuro.oficial?igsh=NWE2dHh3eWI0b3Jp"
            target="_blank"
            >formando futuro oficial</a>
        </li>
        <li>
          <i class="pi pi-whatsapp" style="font-size: 1.2rem"></i
            >
          <a href="https://twitter.com" target="_blank"
            >manda tus consultas y comentarios</a>
        </li>
        <li>
          <i class="pi pi-map-marker" style="font-size: 1.2rem"></i
            >
          <a href="https://youtube.com" target="_blank"
            >mira los partidos y eventos </a>
        </li>
      </ul>
      </section>

    </footer>
  </div>
</template>

<script setup lang="ts">
import 'primeicons/primeicons.css'
</script>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
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
  transition:
    background-color 0.3s ease,
    letter-spacing 0.3s ease;
}

.navbar a:hover {
  background-color: #1aae4d; /* Verde más claro en hover */
  letter-spacing: 0.5px; /* Separación suave de letras */
  text-decoration: underline;
}

.main-content {
  flex: 1;
  padding: 40px;
}

.imagenes-container {
  display: flex;
  width: 100%;
  max-width: 1200px;
  height: 500px; /* Más alto */
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
  font-family: 'Arial Rounded MT Bold', 'Arial Rounded', Arial, sans-serif;
}
button {
  display: block;
  margin: 20px auto;
  padding: 12px 32px;
  font-size: 20px;
  color: #fff;
  border: none;
  border-radius: 8px;
  font-family: 'Arial Rounded MT Bold', 'Arial Rounded', Arial, sans-serif;
  cursor: pointer;
  font-weight: bold;
  transition: background 0.2s;
}

button:hover {
  background: #447453;
}
.footer {
  border-top: #16519d solid 12px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  justify-content: center;
  align-items: center;
  background: #169d3e;
  padding: 2rem;
  width: 100%;
  height: 200px;
  box-sizing: border-box;
  bottom: 0;
}


.footer ul {
  display: flex;
  flex-direction: column;
  list-style: none;
  gap: 0.25rem;

}

.redes-sociales li {
  color: #fff;
  display: grid;
  grid-template-columns: 40px 1fr;
  justify-content: center;
  align-items: center;
}
.info-empresa{
  display: flex;
  justify-content: start;
  flex-direction: column;
  color: #fff;
  h1{
    border-bottom: 1px solid white;

  }
}

.footer a {
  color: #fff;
  text-decoration: none;
  font-size: 12px;
}

.nav_footer  ul li {
  padding: 0 0.25rem;
  }
.nav_footer li:hover{
    width: 100%;
    background-color: #166b30;
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
</style>
