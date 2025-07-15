<template>
  <div>
    <form @submit.prevent="crear">
      <div >
        <label for="" >Nombre de la Categoria</label>
        <input type="text" name="create" v-model="categoria.nombre">
      </div>
      <button type="submit">Crear Categoria</button>
    </form>

  </div>
    <div class="volver" >
          <router-link :to="{name:'configuraciones'}"><i class="pi pi-arrow-circle-left" style="font-size: 2rem"></i></router-link>
  </div>
</template>

<script setup lang="ts">
import { toRefs} from 'vue'
import  UseCategoriasStore from '../../stores/categorias'
import { onMounted } from 'vue'
const {categoria} = toRefs(UseCategoriasStore())
const limpiarFormulario = () => {
  categoria.value = {
    nombre: '',

  }
}
onMounted(() => {
  limpiarFormulario()
})
const {create} = UseCategoriasStore()
const crear = async ()=> {
  if (!categoria.value.nombre) {
    alert('El nombre de la categoria es obligatorio')
  }
else
  {
    const response = await create(categoria.value)
    categoria.value.nombre= ''
    alert('Categoria creada correctamente')
    console.log(response)
  }
}

</script>

<style scoped>
form {
  max-width: 500px;
  margin: 2rem auto;
  padding: 1.5rem;
  background-color: #f5f5f5;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 0.6rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 0.8rem 1.2rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.volver{
  display: flex;
  justify-content: center;
  align-items: center;
  height: 20vh; 
}


</style>
