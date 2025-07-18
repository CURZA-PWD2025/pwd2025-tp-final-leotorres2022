<template>
  <div class="detalle-talle">
    <h2><i class="pi pi-tag" style="margin-right: 8px"></i>Detalle del Talle</h2>
    <p>
      <i class="pi pi-user" style="margin-right: 8px"></i><strong>Nombre:</strong>
      <span class="dato">{{ talle.nombre }}</span>
    </p>
    <p>
      <i class="pi pi-hash" style="margin-right: 8px"></i><strong>ID:</strong>
      <span class="dato">{{ talle.id }}</span>
    </p>
  </div>

  <div class="volver">
    <router-link :to="{ name: 'talles_list' }"
      ><i class="pi pi-arrow-circle-left" style="font-size: 2rem"></i
    ></router-link>
  </div>
</template>
<script setup lang="ts">
import { toRefs } from 'vue'
import UseTallesStore from '../../stores/talles'
import { useRoute } from 'vue-router'
import { onMounted } from 'vue'
const route = useRoute()
const { talle: talle, talles: talles } = toRefs(UseTallesStore())
const { update } = UseTallesStore()
onMounted(async () => {
  const id = route.params.id
  console.log('ID del talle a editar:', id)
  const encontrada = talles.value.find((talle) => talle.id == parseInt(id as string))
  talle.value = encontrada ?? { nombre: '' }
})
</script>

<style scoped>
.detalle-talle {
  max-width: 600px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  color: #333;
  font-family: 'Segoe UI', sans-serif;
}

.detalle-talle h2 {
  text-align: center;
  color: #444;
  margin-bottom: 1.5rem;
}

.detalle-talle p {
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
