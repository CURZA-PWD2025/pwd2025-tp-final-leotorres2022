<template>
  <div>
<h2>Modificar Compra</h2>
    <form @submit.prevent="editar">
      <div class="detalle-socio">
    <label>descripcion</label>
    <input type="text" v-model="compra.descripcion" class="dato">
    <label>Precio</label>
    <input type="text" v-model="compra.precio" class="dato">
    <label>Cantidad</label>
    <input type="text" v-model="compra.cantidad" class="dato">
    <label>Talle</label>
    <select v-model="compra.talle" required>
      <option v-for="talle in talles" :key="talle.id" :value="talle">
        {{ talle.nombre }}
      </option>
    </select>
    <label>Categoria</label>
    <select v-model="compra.categoria" required>
      <option v-for="categoria in categorias" :key="categoria.id" :value="categoria">
        {{ categoria.nombre }}
      </option>
    </select>
    <label>Nombre Socio</label>
    <select v-model="compra.socio" required>
      <option v-for="socio in socios" :key="socio.id" :value="socio">
        {{ socio.nombre }}
      </option>
    </select>
  </div>
      <button type="submit" class="modificar">Modificar</button>
    </form>

  </div>
  <div class="volver">
    <router-link :to="{name:'compras_list'}"><i class="pi pi-arrow-circle-left" style="font-size: 2rem"></i></router-link>
  </div>

</template>
<script setup lang="ts">
import { toRefs } from 'vue';
import  UseComprasStore from '../../stores/compras'
import { useRoute} from 'vue-router';
import { onMounted } from 'vue';
import UseTallesStore from '../../stores/talles'
import UseSociosStore from '../../stores/socios'
import UseCategoriasStore from '../../stores/categorias'
const route = useRoute()
const { compra,compras} = toRefs(UseComprasStore())
const {update} = UseComprasStore()
const {talles, getAll: getAllTalles} = UseTallesStore()
const {socios, getAll: getAllSocios} = UseSociosStore()
const {categorias, getAll: getAllCategorias} = UseCategoriasStore()


onMounted(async () => {
    const id = route.params.id
  console.log('ID de la compra a editar:', id)
const encontrada=compras.value.find(compra => compra.id == parseInt(id as string))
compra.value =  encontrada ?? { descripcion: '' , talle: undefined, socio: undefined, categoria: undefined,precio: 0, cantidad: 0, id: 0 }
})

const editar = async () => {
   if (!compra.value.descripcion) {
    alert('La descripcion de la es obligatoria')
    }
  else if (compra.value.precio <= 0) {
    alert('El precio debe ser mayor a 0')
  }
  else if (compra.value.cantidad < 0) {
    alert('la cantidad no puede ser negativo')
  }
  else if (!compra.value.talle) {
    alert('Debe seleccionar un Talle')
  }
  else if (!compra.value.categoria) {
     alert('Debe seleccionar una categoria')
  }
   else if (!compra.value.socio){
     alert('Debe ingresar un Nro de Socio')
  }

 else {
    const articulo_json = {
      id: compra.value.id,
      descripcion: compra.value.descripcion,
      precio: Number(compra.value.precio),
      cantidad: Number(compra.value.cantidad),
      talle_id: compra.value.talle?.id,
      categoria_id: compra.value.categoria?.id,
      socio_id: compra.value.socio?.id,
         }
    console.log('Compra  a modificar:', articulo_json,compra.value.id)
    try {
      await update(articulo_json)
      console.log(' modificada correctamente:', articulo_json)
      alert('Compra modificada correctamente')
      // Resetear los campos del formulario
      compra.value.descripcion= ''
      compra.value.precio= 0
      compra.value.cantidad= 0
      compra.value.talle= undefined
      compra.value.categoria= undefined
      compra.value.socio= undefined

    } catch (error) {
      console.error('Error al modificar compra:', error)
      alert('Error al modificar compra. Revisa la consola para más detalles.')
    }
  }
};

</script>

<style scoped>
.detalle-socio {
  max-width: 850px;
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

