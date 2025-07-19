<template>
  <div>
    <form @submit.prevent="crear">
      <div >
        <label for="" >Nombre del Talle</label>
        <input type="text" name="create" v-model="talle.nombre">
      </div>
      <button type="submit">Crear Talle</button>
    </form>

  </div>
    <div class="volver" >
          <router-link :to="{name:'talles_list'}"><i class="pi pi-arrow-circle-left" style="font-size: 2rem"></i></router-link>
  </div>
</template>

<script setup lang="ts">
import { toRefs} from 'vue'
import  UseTallesStore from '../../stores/talles'
import { onMounted } from 'vue'
const {talle: talle} = toRefs(UseTallesStore())
const limpiarFormulario = () => {
  talle.value = {
    nombre: '',

  }
}
onMounted(() => {
  limpiarFormulario()
})
const {create} = UseTallesStore()
const crear = async ()=> {
  if (!talle.value.nombre) {
    alert('El nombre del talle es obligatorio')
  }
else
  {
    const response = await create(talle.value)
    talle.value.nombre= ''
    alert('Talle creado correctamente')
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
