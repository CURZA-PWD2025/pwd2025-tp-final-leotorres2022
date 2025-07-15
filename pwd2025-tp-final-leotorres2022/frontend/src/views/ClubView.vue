<template>
<RouterView />
<body>

  <h1>Formando Futuro</h1>

  <div class="card">
    <div class="card-title">🌬️ Nacimiento del Sueño</div>
    <div class="card-text">En Viedma, azotada por el viento patagónico, nació un sueño futbolístico: crear un club que forme jóvenes y les dé oportunidades reales.</div>
  </div>

  <div class="card">
    <div class="card-title">👤 Ulises, el Fundador</div>
    <div class="card-text">Un hombre sencillo con pasión por el fútbol. Aunque no pudo alcanzar la primera división, mantuvo vivo su amor por el deporte.</div>
  </div>

  <div class="card">
    <div class="card-title">🎙️ Su Declaración</div>
    <div class="card-text">“Siempre quise que los chicos tuvieran la oportunidad que yo no tuve.” El objetivo: que se diviertan, aprendan y crezcan como personas.</div>
  </div>

  <div class="card">
    <div class="card-title">🏗️ Primeros Pasos</div>
    <div class="card-text">Un terreno baldío, unos conos y una pelota gastada marcaron el inicio. La energía de Ulises y los chicos encendió la llama.</div>
  </div>

  <div class="card">
    <div class="card-title">🌱 Crecimiento</div>
    <div class="card-text">Más chicos se sumaron. El club logró una cancha, equipamiento y se convirtió en un referente por su labor social y educativa.</div>
  </div>

</body>

</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
const route = useRouter();

</script>
<style scoped>

    body {
      margin: 0;
      padding: 30px;
      font-family: 'Quicksand', sans-serif;
      background: linear-gradient(135deg, #c5e1a5, #81c784);
      color: #1b5e20;
    }

    h1 {
      text-align: center;
      font-size: 2.8rem;
      margin-bottom: 40px;
      color: #2e7d32;
    }

    .card {
      background: rgba(255, 255, 255, 0.9);
      border-radius: 15px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      padding: 20px;
      margin-bottom: 25px;
      transition: transform 0.2s;
    }

    .card:hover {
      transform: scale(1.02);
    }

    .card-title {
      font-weight: bold;
      font-size: 1.3rem;
      margin-bottom: 10px;
      color: #388e3c;
    }

    .card-text {
      font-size: 1.05rem;
      line-height: 1.6;
    }
</style>
