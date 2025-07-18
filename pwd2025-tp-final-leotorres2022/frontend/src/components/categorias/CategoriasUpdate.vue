<template>
  <div>
    <form @submit.prevent="editar">
      <div class="detalle-socio">
        <label>Nombre</label>
        <input type="text" v-model="categoria.nombre" class="dato" />
      </div>
      <button type="submit" class="modificar">Modificar</button>
    </form>
  </div>
  <div class="volver">
    <router-link :to="{ name: 'categorias_list' }"
      ><i class="pi pi-arrow-circle-left" style="font-size: 2rem"></i
    ></router-link>
  </div>
</template>
<script setup lang="ts">
import { toRefs } from 'vue'
import UseCategoriasStore from '../../stores/categorias'
import { useRoute } from 'vue-router'
import { onMounted } from 'vue'
const route = useRoute()
const { categoria, categorias } = toRefs(UseCategoriasStore())
const { update } = UseCategoriasStore()
onMounted(async () => {
  const id = route.params.id
  console.log('ID de la marca a editar:', id)
  const encontrada = categorias.value.find((categoria) => categoria.id == parseInt(id as string))
  categoria.value = encontrada ?? { nombre: '' }
})

const editar = async () => {
  if (!categoria.value.nombre) {
    alert('El nombre de la categoria es obligatorio')
  } else {
    const response = await update(categoria.value)
    alert('Categoria actualizada correctamente')
    categoria.value.nombre = ''
    console.log(response)
  }
}
</script>

<style scoped>
.detalle-socio {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  color: #333;
  font-family: 'Segoe UI', sans-serif;
  font-size: 1.3rem;
}

.detalle-socio h2 {
  text-align: center;
  color: #444;
  margin-bottom: 1.5rem;
}

.detalle-socio p {
  margin: 1rem 0;
  font-size: 1.3rem;
  display: flex;
  align-items: center;
}

.dato {
  margin-left: 8px;
  color: #007bff;
  font-weight: bold;
  font-size: 1.3rem;
}
.modificar {
  display: block;
  width: 10%;
  padding: 0.6rem;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1.3rem;
  margin: 1rem auto;
  text-align: center;
}
.volver {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 20vh;
}
</style>
