<template>

<div class="detalle-categoria">
  <h2><i class="pi pi-tag" style="margin-right: 8px"></i>Detalle de la Categoria</h2>
  <p><i class="pi pi-user" style="margin-right: 8px"></i><strong>Nombre:</strong> <span class="dato">{{ categoria.nombre }}</span></p>
  <p><i class="pi pi-hash" style="margin-right: 8px"></i><strong>ID:</strong> <span class="dato">{{ categoria.id }}</span></p>
</div>

<div class="volver" >
    <router-link :to="{name:'categorias_list'}"><i class="pi pi-arrow-circle-left" style="font-size: 2rem"></i></router-link>
  </div>
</template>
<script setup lang="ts">
import { toRefs } from 'vue';
import  UseCategoriasStore from '../../stores/categorias'
import { useRoute} from 'vue-router';
import { onMounted } from 'vue';
const route = useRoute()
const { categoria: categoria,categorias} = toRefs(UseCategoriasStore())
const {update} = UseCategoriasStore()
onMounted(async () => {
  const id = route.params.id
  console.log('ID de la categoria a editar:', id)
const encontrada= categorias.value.find(categoria => categoria.id == parseInt(id as string))
categoria.value =  encontrada ?? { nombre: '' }
})

</script>


<style scoped>

.detalle-categoria {
  max-width: 600px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(0,0,0,0.1);
  color: #333;
  font-family: 'Segoe UI', sans-serif;
}

.detalle-categoria h2 {
  text-align: center;
  color: #444;
  margin-bottom: 1.5rem;
}

.detalle-categoria p {
  margin: 1rem 0;
  font-size: 1.1rem;
  display: flex;
  align-items: center;
}

.dato {
  margin-left: 8px;
  color: #007BFF;
  font-weight: bold;

}

.volver{
  display: flex;
  justify-content: center;
  align-items: center;
  height: 20vh;
}
</style>

