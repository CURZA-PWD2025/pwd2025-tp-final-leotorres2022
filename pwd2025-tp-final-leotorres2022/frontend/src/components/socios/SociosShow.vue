<template>
  <div class="detalle-socio">
    <h2><i class="pi pi-id-card" style="margin-right: 8px"></i>Detalle del Socio</h2>
    <p>
      <i class="pi pi-user" style="margin-right: 8px"></i><strong>Nombre:</strong>
      <span class="dato">{{ socio.nombre }}</span>
    </p>
    <p>
      <i class="pi pi-home" style="margin-right: 8px"></i><strong>Dirección:</strong>
      <span class="dato">{{ socio.direccion }}</span>
    </p>
    <p>
      <i class="pi pi-phone" style="margin-right: 8px"></i><strong>Teléfono:</strong>
      <span class="dato">{{ socio.telefono }}</span>
    </p>
    <p>
      <i class="pi pi-envelope" style="margin-right: 8px"></i><strong>Email:</strong>
      <span class="dato">{{ socio.email }}</span>
    </p>
    <p>
      <i class="pi pi-hash" style="margin-right: 8px"></i><strong>ID:</strong>
      <span class="dato">{{ socio.id }}</span>
    </p>
  </div>

  <div class="volver">
    <router-link :to="{ name: 'socios_list' }"
      ><i class="pi pi-arrow-circle-left" style="font-size: 2rem"></i
    ></router-link>
  </div>
</template>
<script setup lang="ts">
import { toRefs } from 'vue'
import UseSociosStore from '../../stores/socios'
import { useRoute } from 'vue-router'
import { onMounted } from 'vue'
const route = useRoute()
const { socio: socio, socios: socios } = toRefs(UseSociosStore())
onMounted(async () => {
  const id = route.params.id
  const encontrada = socios.value.find((socio) => socio.id == parseInt(id as string))
  socio.value = encontrada ?? { nombre: '', direccion: '', telefono: '', email: '' }
  if (!socio.value) {
    console.error('socio no encontrado')
  }
})
</script>

<style scoped>
.detalle-socio {
  max-width: 600px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  color: #333;
  font-family: 'Segoe UI', sans-serif;
}

.detalle-socio h2 {
  text-align: center;
  color: #444;
  margin-bottom: 1.5rem;
}

.detalle-socio p {
  margin: 1rem 0;
  font-size: 1.1rem;
  display: flex;
  align-items: center;
}

.dato {
  margin-left: 8px;
  color: #007bff;
  font-weight: bold;
}

.volver {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 20vh;
}
</style>
