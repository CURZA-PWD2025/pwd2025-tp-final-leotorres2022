<template>
  <div>
<h2>Modificar Socio</h2>
    <form @submit.prevent="editar">
      <div class="detalle-socio">
    <label>Nombre</label>
    <input type="text" v-model="socio.nombre" class="dato">
    <label>Teléfono</label>
    <input type="text" v-model="socio.telefono" class="dato">
    <label>Dirección</label>
    <input type="text" v-model="socio.direccion" class="dato">
    <label>Email</label>
    <input type="email" v-model="socio.email" class="dato">
  </div>
      <button type="submit" class="modificar">Modificar</button>
    </form>

  </div>
  <div class="volver">
    <router-link :to="{name:'socios_list'}"><i class="pi pi-arrow-circle-left" style="font-size: 2rem"></i></router-link>
  </div>

</template>
<script setup lang="ts">
import { toRefs } from 'vue';
import  UseSociosStore from '../../stores/socios'
import { useRoute} from 'vue-router';
import { onMounted } from 'vue';
const route = useRoute()
const { socio,socios} = toRefs(UseSociosStore())
const {update} = UseSociosStore()
onMounted(async () => {
  const id = route.params.id
  console.log('ID del socio a editar:', id)
const encontrada=socios.value.find(socio => socio.id == parseInt(id as string))
socio.value =  encontrada ?? { nombre: '' , direccion: '', telefono: '', email: '' }
})

const editar = async () => {
  if (!socio.value.nombre) {
    alert('El nombre del socio es obligatorio');
  } else {
    const response = await update(socio.value);
    socio.value.nombre= ''
    socio.value.telefono= ''
    socio.value.direccion= ''
    socio.value.email= ''
    alert('Socio actualizado correctamente');
    console.log(response);
  }
};

</script>

<style scoped>
.detalle-socio {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(0,0,0,0.1);
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
  color: #007BFF;
  font-weight: bold;
  font-size: 1.3rem;
}
.modificar {
  display: block;
  width: 10%;
  padding: 0.6rem;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1.3rem;
  margin: 1rem auto;
  text-align: center;
}
.volver{
  display: flex;
  justify-content: center;
  align-items: center;
  height: 20vh; 
}

</style>
